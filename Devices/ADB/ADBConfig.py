#!/usr/bin/env python2

'''
Love Live! School Idol Festival: Keyboard Controller
File: Devices/ADB/ADBConfig.py

Copyright (c) 2014 Visatouch Deeying ("xerodotc")
Love Live! School Idol Festival is a trademark of KLab and Bushiroad
'''

import ConfigParser

config = ConfigParser.ConfigParser(allow_no_value=True)
config.read('config.cfg')

#ADB_EXECUTABLE = "adb" # Path to ADB executable (or how you launch ADB)
#ADB_DEVICE_SERIAL = None # Device serial number, set to None to autoconnect for single device

ADB_EXECUTABLE = config.get("ADB", "adb-exe")
ADB_DEVICE_SERIAL = config.get("ADB", "adb-serial")
