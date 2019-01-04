#!/bin/env python3
from qmp import QEMUMonitorProtocol
import sys
import os, os.path
import json
import subprocess
import time
import socket
import struct
import datetime
from memory_mappings_and_offsets import *

#The test class is JayFoxRox's code.
class Test(object):

  def stop(self):
    if self._p:
      self._p.terminate()
      self._p = None

  def run_cmd(self, cmd):
    if type(cmd) is str:
      cmd = {
          "execute": cmd, 
          "arguments": {}
      }
    resp = self._qmp.cmd_obj(cmd)
    if resp is None:
      raise Exception('Disconnected!')
    return resp

  def pause(self):
    return self.run_cmd('stop')

  def cont(self):
    return self.run_cmd('cont')

  def restart(self):
    return self.run_cmd('system_reset')

  def screenshot(self):
    cmd = {
        "execute": "screendump", 
        "arguments": {
            "filename": "screenshot.ppm"
        }
    }
    return self.run_cmd(cmd)

  def isPaused(self):
    resp = self.run_cmd('query-status')
    return resp['return']['status'] == 'paused'

  def read(self, addr, size):
    cmd = {
        "execute": "human-monitor-command", 
        "arguments": { "command-line": "x /%dxb %d" % (size,addr) }
    }
    response = self.run_cmd(cmd)
    lines = response['return'].replace('\r', '').split('\n')
    data_string = ' '.join(l.partition(': ')[2] for l in lines).strip()
    data = bytes(int(b, 16) for b in data_string.split(' '))
    return data


t = Test()
i = 0

#The connection loop is JayFoxRox's code.
while True:
  print('Trying to connect %d' % i)
  if i > 0: time.sleep(1)
  try:
    t._qmp = QEMUMonitorProtocol(('localhost', 4444))
    t._qmp.connect()
  except Exception as e:
    if i > 4:
      raise
    else:
      i += 1
      continue
  break

#These read functions were originally JayFoxRox's
def read_u8(address):
  return int.from_bytes(t.read(address, 1), 'little')

def read_u16(address):
  return int.from_bytes(t.read(address, 2), 'little')

def read_u32(address):
  return int.from_bytes(t.read(address, 4), 'little')

def read_s8(address):
  return int.from_bytes(t.read(address, 1), 'little', signed=True)

def read_s16(address):
  return int.from_bytes(t.read(address, 2), 'little', signed=True)

def read_s32(address):
  return int.from_bytes(t.read(address, 4), 'little', signed=True)

# get player datum array info (found by Xbox7887)
player_datum_array = read_u32(0x2FAD28)
player_datum_array_max_count = read_u16(player_datum_array + Datum_Array_Element_Max_Count_Offset)
player_datum_array_element_size = read_u16(player_datum_array + Datum_Array_Element_Size_Offset)
player_datum_array_first_element_address = read_u32(player_datum_array + Datum_Array_First_Element_Pointer_Offset)

# function to get player's element date (found by Xbox7887)
def get_players_element_data(player_index, offset, number_of_bytes):
  data = t.read(player_datum_array_first_element_address + player_index * player_datum_array_element_size, player_datum_array_element_size)
  return data

# initialize variables
# TODO get player count from memory so it's not hard coded
score1 = -1 #red
score2 = -1 #blue
player_count = 3
player_stat_array = []

# initilize stat array with current values
# TODO clean up offsets by converting to hex
for player_index in range(player_count):
  player_stats = {}
  player_stats['kills'] = read_s8(player_datum_array_first_element_address + player_index * player_datum_array_element_size + Kills_Offset)
  player_stats['team_kills'] = read_s8(player_datum_array_first_element_address + player_index * player_datum_array_element_size + Team_Kills_Offset)
  player_stats['deaths'] = read_s8(player_datum_array_first_element_address + player_index * player_datum_array_element_size + Deaths_Offset)
  player_stats['suicides'] = read_s8(player_datum_array_first_element_address + player_index * player_datum_array_element_size + Suicides_Offset)
  player_stats['name'] = t.read(player_datum_array_first_element_address + player_index * player_datum_array_element_size + Player_Name_Offset,24).decode("utf-16").split('\x00',1)[0]
  player_stats['index'] = player_index
  player_stat_array.append(player_stats)

while True:
    
  score1_new = read_s8(Team_Slayer_Red_Score_Address) # 0x276710 is location of red team score in team slayer games
  score2_new = read_s8(Team_Slayer_Blue_Score_Address) # 0x276714 is location of blue team score in team slayer games

  #if score changes
  if(score1 != score1_new or score2 != score2_new):
    #print it
    print("Red = " + str(score1_new) + ", Blue = " + str(score2_new))
    score1 = score1_new
    score2 = score2_new

    #identify what stats changed
    player_stat_array_new = []
    for player_index in range(player_count):
      player_stats = {}
      player_stats['kills'] = read_s8(player_datum_array_first_element_address + player_index * player_datum_array_element_size + Kills_Offset)
      player_stats['team_kills'] = read_s8(player_datum_array_first_element_address + player_index * player_datum_array_element_size + Team_Kills_Offset)
      player_stats['deaths'] = read_s8(player_datum_array_first_element_address + player_index * player_datum_array_element_size + Deaths_Offset)
      player_stats['suicides'] = read_s8(player_datum_array_first_element_address + player_index * player_datum_array_element_size + Suicides_Offset)
      player_stats['name'] = t.read(player_datum_array_first_element_address + player_index * player_datum_array_element_size + Player_Name_Offset,24).decode("utf-16").split('\x00',1)[0]
      player_stats['index'] = player_index
      player_stat_array_new.append(player_stats)

    #output stat changes
    for player_index in range(player_count):
      if player_stat_array[player_index]['kills'] != player_stat_array_new[player_index]['kills']:
        print(str(player_stat_array[player_index]['name']) + " kills changed from " + str(player_stat_array[player_index]['kills']) + " to " + str( player_stat_array_new[player_index]['kills']))
      if player_stat_array[player_index]['deaths'] != player_stat_array_new[player_index]['deaths']:
        print(str(player_stat_array[player_index]['name']) + " deaths changed from " + str(player_stat_array[player_index]['deaths']) + " to " + str( player_stat_array_new[player_index]['deaths']))
      if player_stat_array[player_index]['team_kills'] != player_stat_array_new[player_index]['team_kills']:
        print(str(player_stat_array[player_index]['name']) + " team_kills changed from " + str(player_stat_array[player_index]['team_kills']) + " to " + str( player_stat_array_new[player_index]['team_kills']))
      if player_stat_array[player_index]['suicides'] != player_stat_array_new[player_index]['suicides']:
        print(str(player_stat_array[player_index]['name']) + " suicides changed from " + str(player_stat_array[player_index]['suicides']) + " to " + str( player_stat_array_new[player_index]['suicides']))
    player_stat_array = player_stat_array_new
  time.sleep(0.1) # wait 100ms
