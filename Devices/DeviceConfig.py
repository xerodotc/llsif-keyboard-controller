#!/usr/bin/env python2

'''
Love Live! School Idol Festival: Keyboard Controller
File: Devices/DeviceConfig.py

Copyright (c) 2014 Visatouch Deeying ("xerodotc")
Love Live! School Idol Festival is a trademark of KLab and Bushiroad
'''

import ConfigParser

config = ConfigParser.ConfigParser(allow_no_value=True)
config.read('config.cfg')

# If you want to force a device module set this, otherwise auto-detect
DEVICE_MODULE = None
if config.getboolean("Main", "bluestacks"):
	DEVICE_MODULE = "bluestacks"

# Touch scripts directory
TOUCH_SCRIPTS_DIR = "TouchScripts/"

# Device specific config
ZTEV970M_SINGLE_TOUCH_PRIORITY = False # For ZTE V970M if you're playing easy song turn this on, otherwise turn this off
LGP500_SINGLE_TOUCH_PRIORITY = False # For LG-P500 leaving this off is a better choice
BLUESTACKS_SINGLE_TOUCH_PRIORITY = False
BLUESTACKS_USE_PYHOOK = True
