#!/usr/bin/env python2

'''
Love Live! School Idol Festival: Keyboard Controller
File: Devices/__init__.py

Copyright (c) 2014 Visatouch Deeying ("xerodotc")
Love Live! School Idol Festival is a trademark of KLab and Bushiroad
'''

import sys
import ADB
import DeviceConfig

# Wait for device
# (I don't like to handle this here but it's required for device auto-detection)
try:
    print "Waiting for device..."
    ADB.waitDevice()
except KeyboardInterrupt as e:
    sys.exit()

# If device module is already (forced) defined then use it
# otherwise auto-detect
if DeviceConfig.DEVICE_MODULE != None:
    deviceModule = DeviceConfig.DEVICE_MODULE
else:
    from DeviceDetect import detectDeviceModule
    deviceModule = detectDeviceModule()

# Import _Device class according to device module
if deviceModule == "ztev970m":
    from ZTEV970M import _Device
elif deviceModule == "lgp500":
    from LGP500 import _Device
elif deviceModule == "bluestacks":
	from BlueStacks import _Device
else:
    print "Unsupported device"
    raw_input()
    sys.exit()

# Device class stub (extended from device module)
class Device (_Device):
    def __init__(self):
        super(Device, self).__init__()
        self.adb = ADB
