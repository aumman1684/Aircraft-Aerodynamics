#----------------------------------------------------
# File written from FAST (Version 1.3)
# Module FAST_HUB (Version 1.3)
# File created: Thu Sep 17 17:00:15 1998
#
# No user comments should be placed above this header
#----------------------------------------------------
file_IO: FILE_ATTRIBUTE MULTI_ZONE ON
file_IO: FILE_FORMAT UNFORMATTED
file_IO: READ_FILE nlrflap_blank.x
file_IO: FILE_TYPE SOLUTION
file_IO: READ_FILE nlrflap.q
file_IO: QUIT_MODULE
viewer: MODULE_START Calculator
calculator: S0 = Mach Number
calculator: S1 = Pressure
calculator: QUIT_MODULE
viewer: MODULE_START Surfer
surfer: NEW_OBJECT
surfer: ZONE 2
