#!/usr/bin/env python2

'''
Love Live! School Idol Festival: Keyboard Controller
File: Devices/DeviceDetect.py

Copyright (c) 2014 Visatouch Deeying ("xerodotc")
Love Live! School Idol Festival is a trademark of KLab and Bushiroad
'''

import ADB

def detectDeviceModule():
    deviceBrand = ADB.shell("getprop ro.product.brand").strip().lower()
    deviceModel = ADB.shell("getprop ro.product.model").strip().lower()
    if deviceBrand == "lge":
        if deviceModel == "lg-p500":
            return "lgp500" # LG-P500 (LG Optimus One)
    elif deviceBrand == "zte":
        if deviceModel == "zte v970" or deviceModel == "zte v970m":
            return "ztev970m" # xerodotc: Should be the same for both, but because I have ZTE V970M, I'll use "ztev970m" for module name
