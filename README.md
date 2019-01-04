# XboxHaloGameLogger
A script to keep tracking of game statistics with Halo 1 for the original xbox.

# Credits
I did almost none of the heavy lifting on this. Xbox7887 & JayFoxRox helped me figure out how to set up QMP, read memory addresses, and told me where to go at pretty much every step. Devieth and Mintograde helped me out by sharing some of their knowledge from Halo 1 and Halo PC.

# Notes

- Static Addresses:
  - Player Datum Array Pointer: 0x2FAD28
  - Object Header Datum Array Pointer: 0x2FC6AC
  - Team Slayer Red Score: 0x276710
  - Team Slayer Blue Score: 0x276714
  
- Datum Array Header Fields:
  - Name Offset: 0x0
  - First Element Pointer Offset: 0x32
  - Element Max Count Offset: 0x20
  - Element Size Offset: 0x22
  
- Player Datum Array Value Offsets:
  - Player Name: 0x4
  - Kills: 0x98
  - Team Kills (Betrays + Suicides?): 0xA8
  - Deaths: 0xAA
  - Suicides: 0xAC
  
- Player Object Array Value Offsets:
  - XCoord: 0xC (float)
  - YCoord: 0x10 (float)
  - ZCoord: 0x14 (float)
  - XVel: 0x18 (float)
  - YVel: 0x1C (float)
  - ZVel: 0x20 (float)
  - Pitch: 0x24 (float)
  - Yaw: 0x28 (float)
  - Roll: 0x2C (float)
  - XScale: 0x30 (float)
  - YScale: 0x34 (float)
  - ZScale: 0x38 (float)
  - Max Health: 0x88 (float, default value is 75)
  - Max Shields: 0x8C (float, defaeult value is 1)
  - Health %: 0x90 (float)
  - Shield %: 0x94 (float)
  - Time Elapsed (Minutes, possibly while player is only alive?): 0xA
  
  
