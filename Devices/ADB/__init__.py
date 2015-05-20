#!/usr/bin/env python2

'''
Love Live! School Idol Festival: Keyboard Controller
File: Devices/ADB/__init__.py

Copyright (c) 2014 Visatouch Deeying ("xerodotc")
Love Live! School Idol Festival is a trademark of KLab and Bushiroad
'''

import subprocess
import ADBConfig

# adb wait-for-device
def waitDevice():
	if ADBConfig.ADB_DEVICE_SERIAL == None:
		subprocess.call([ADBConfig.ADB_EXECUTABLE, "wait-for-device"])
	else:
		subprocess.call([ADBConfig.ADB_EXECUTABLE, "-s", ADBConfig.ADB_DEVICE_SERIAL, "wait-for-device"])

# adb push <src> <dest>
def push(src, dest):
	if ADBConfig.ADB_DEVICE_SERIAL == None:
		subprocess.call([ADBConfig.ADB_EXECUTABLE, "push", src, dest])
	else:
		subprocess.call([ADBConfig.ADB_EXECUTABLE, "-s", ADBConfig.ADB_DEVICE_SERIAL, "push", src, dest])

# adb shell <cmd>
def shell(cmd):
	try:
		if ADBConfig.ADB_DEVICE_SERIAL == None:
			return subprocess.check_output([ADBConfig.ADB_EXECUTABLE, "shell", cmd])
		else:
			return subprocess.check_output([ADBConfig.ADB_EXECUTABLE, "-s", ADBConfig.ADB_DEVICE_SERIAL, "shell", cmd])
	except Exception as e:
		return None
