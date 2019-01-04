#Static_Addresses (found by Xbox7887):
Player_Datum_Array_Pointer = 0x2FAD28
Object_Header_Datum_Array_Pointer = 0x2FC6AC
Team_Slayer_Red_Score_Address = 0x276710
Team_Slayer_Blue_Score_Address  = 0x276714
Gametype_Name_Address = 0x2FBA80                 # Will update after gametype is select in menu
Gametype_Name_Address_2 = 0x2FBEEC               # Will update after gametype is select in menu
Xbox_Name_Address = 0x2FB9DC                    
Xbox_Name_Address_2 = 0x2FBE48                   
Xbox_Name_Address_3 = 0x2FBF5C                   
Map_Name_Address = 0x2FBA00                      # Will update when choosing map from menu
Map_Name_Address = 0x2FBE6C                      # Will update when choosing map from menu

#Datum_Array_Header_Fields (found by Xbox7887):
Datum_Array_Name_Offset = 0x0
Datum_Array_First_Element_Pointer_Offset = 0x34
Datum_Array_Element_Max_Count_Offset = 0x20
Datum_Array_Element_Size_Offset = 0x22


#Player_Datum_Array_Value_Offsets:
Player_Name_Offset = 0x4
Kills_Offset = 0x98
Team_Kills_Offset = 0xA8 #(Betrays_+_Suicides?)
Deaths_Offset = 0xAA
Suicides_Offset = 0xAC

#Player_Object_Array_Value_Offsets (found with the help of Devieth):
XCoord_Offset = 0xC #(float)
YCoord_Offset = 0x10 #(float)
ZCoord_Offset = 0x14 #(float)
XVel_Offset = 0x18 #(float)
YVel_Offset = 0x1C #(float)
ZVel_Offset = 0x20 #(float)
Pitch_Offset = 0x24 #(float)
Yaw_Offset = 0x28 #(float)
Roll_Offset = 0x2C #(float)
XScale_Offset = 0x30 #(float)
YScale_Offset = 0x34 #(float)
ZScale_Offset = 0x38 #(float)
Max_Health_Offset = 0x88 #(float,_default_value_is_75)
Max_Shields_Offset = 0x8C #(float,_defaeult_value_is_1)
Health_Percentage_Offset = 0x90 #(float)
Shield_Percentage_Offset = 0x94 #(float)
Time_Elapsed_Offset = 0xA #(Minutes,_possibly_while_player_is_only_alive?)
