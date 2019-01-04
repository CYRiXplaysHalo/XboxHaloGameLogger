# XboxHaloGameLogger
A script to keep tracking of game statistics with Halo 1 for the original xbox.

# Files

- memory_mappings_and_offset.py
  - Stores all known addresses and offsets
- qmp.py
  - Interfaces with game run in XQEMU via QMP
- halo_stat_basic.py
  - Simple stat scoring example. Has only been tested on splitscreen so far.

# Credits
I did almost none of the heavy lifting on this. Xbox7887 & JayFoxRox helped me figure out how to set up QMP, read memory addresses, and told me where to go at pretty much every step. Devieth and Mintograde helped me out by sharing some of their knowledge from Halo 1 and Halo PC.

# TODO

- Find assists stat offset
- Find player count memory address
- Test system link matches
- Build moderate stat logger which includes more context about each player
- Build verbose stat logger which tracks player coordinates
