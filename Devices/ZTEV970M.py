#!/usr/bin/env python2

'''
Love Live! School Idol Festival: Keyboard Controller
Device module for ZTE V970 or ZTE V970M (ZTE Grand X)
File: Devices/ZTEV970M.py

Copyright (c) 2014 Visatouch Deeying ("xerodotc")
Love Live! School Idol Festival is a trademark of KLab and Bushiroad
ZTE Grand X is a trademark of ZTE Corporation

P.S. ZTE V970M is based on MT6577 chipset
ZTE V970 is based on MT6577 too BUT some might based on Tegra 2 (not sure about it)
'''

import DeviceConfig

class _Device(object):
    # Initialize some variables
    def __init__(self):
        self.keyEventReg = []
        self.keyCodeReg = [False, False, False, False, False, False, False, False, False, False]
        self.touchReg = [None, None]
        self.touchTimer = -1
        self.touchTimerFor = 0
        self.touchRegister = False
        self.adb = None

        self.DEVICE_MODULE = "ztev970m"
        self.TOUCH_SCRIPTS_DIR = "Devices/" + DeviceConfig.TOUCH_SCRIPTS_DIR + self.DEVICE_MODULE + "/"
        self.TOUCH_SCRIPTS_TOUCH0 = "t0" # Single touch p0
        self.TOUCH_SCRIPTS_TOUCH1 = "t1" # Single touch p1
        self.TOUCH_SCRIPTS_TOUCH01 = "t01" # Multitouch p0 p1
        self.TOUCH_SCRIPTS_RELEASE = "r" # Release all
        self.TOUCH_SCRIPTS_FILELIST = [self.TOUCH_SCRIPTS_RELEASE, self.TOUCH_SCRIPTS_TOUCH0, self.TOUCH_SCRIPTS_TOUCH1, self.TOUCH_SCRIPTS_TOUCH01]
        self.TOUCH_POSITION = [(520, 863), (405, 142), (276, 169), (166, 241), (93, 351), (68, 480), (93, 610), (166, 719), (276, 792), (405, 817)]
        self.PYHOOK = False

    # Register key (KeyPress)
    def registerKey(self, keyData):
        if keyData < 0:
            return
        if self.keyCodeReg[keyData]:
            return
        self.keyEventReg.append(keyData)
        self.keyCodeReg[keyData] = True
        self.touchRegister = True
        # Debug
        #print self.keyEventReg
        #print self.keyCodeReg

    # Unregister key (KeyRelease)
    def unregisterKey(self, keyData):
        if keyData < 0:
            return
        if not self.keyCodeReg[keyData]:
            return
        self.keyEventReg.remove(keyData)
        self.keyCodeReg[keyData] = False
        self.touchRegister = True
        # Debug
        #print self.keyEventReg
        #print self.keyCodeReg

    # Decide to holdback event registration or trigger event registration
    # (Optimization for multitouch)
    def updateTouch(self):
        if self.touchRegister != True:
            return
        try:
            if DeviceConfig.ZTEV970M_SINGLE_TOUCH_PRIORITY:
                self.registerTouch()
                self.touchRegister = False
        except Exception as e:
            pass
        if len(self.keyEventReg) == 2:
            self.touchTimer = -1
            self.registerTouch()
            self.touchRegister = False
        elif len(self.keyEventReg) <= 0:
            self.touchTimer = -1
            self.registerTouch()
            self.touchRegister = False
        else:
            if self.touchTimer < 0 or len(self.keyEventReg) != self.touchTimerFor:
                self.touchTimer = 10000
                self.touchTimerFor = len(self.keyEventReg)
            elif self.touchTimer == 0:
                self.registerTouch()
                self.touchTimer = -1
                self.touchRegister = False
            else:
                self.touchTimer -= 1

    # Register touch events then send to devices
    def registerTouch(self):
        touches = []
        if len(self.keyEventReg) > 0:
            touches.append(self.keyEventReg[0])
        if len(self.keyEventReg) > 1:
            touches.append(self.keyEventReg[1])
        update = False
        if self.touchReg[0] != None and not (self.touchReg[0] in touches):
            self.touchReg[0] = None
            update = True
        if self.touchReg[1] != None and not (self.touchReg[1] in touches):
            self.touchReg[1] = None
            update = True
        if update:
            self.sendTouch()
        update = False
        for touch in touches:
            if touch in self.touchReg:
                continue
            if self.touchReg[0] == None:
                update = True
                self.touchReg[0] = touch
            elif self.touchReg[1] == None:
                update = True
                self.touchReg[1] = touch
        if update:
            self.sendTouch()

    # Send touch events by executing touch scripts on devices
    def sendTouch(self):
        if self.touchReg[0] == None and self.touchReg[1] == None:
            self.adb.shell("/data/local/tmp/LLSIFKeyTouchScripts/" + self.TOUCH_SCRIPTS_RELEASE)
        elif self.touchReg[0] != None and self.touchReg[1] != None:
            args = " "
            args += str(self.TOUCH_POSITION[self.touchReg[0]][0]) + " "
            args += str(self.TOUCH_POSITION[self.touchReg[0]][1]) + " "
            args += str(self.TOUCH_POSITION[self.touchReg[1]][0]) + " "
            args += str(self.TOUCH_POSITION[self.touchReg[1]][1])
            self.adb.shell("/data/local/tmp/LLSIFKeyTouchScripts/" + self.TOUCH_SCRIPTS_TOUCH01 + args)
        elif self.touchReg[0] != None:
            args = " "
            args += str(self.TOUCH_POSITION[self.touchReg[0]][0]) + " "
            args += str(self.TOUCH_POSITION[self.touchReg[0]][1])
            self.adb.shell("/data/local/tmp/LLSIFKeyTouchScripts/" + self.TOUCH_SCRIPTS_TOUCH0 + args)
        elif self.touchReg[1] != None:
            args = " "
            args += str(self.TOUCH_POSITION[self.touchReg[1]][0]) + " "
            args += str(self.TOUCH_POSITION[self.touchReg[1]][1])
            self.adb.shell("/data/local/tmp/LLSIFKeyTouchScripts/" + self.TOUCH_SCRIPTS_TOUCH1 + args)

    # Check if key is pressed (for UI only)
    def isKeyPressed(self, keyData):
        if keyData < 0:
            return False
        return self.keyCodeReg[keyData]

    # Upload touch scripts to devices
    def pushScripts(self):
        self.adb.shell("test -d /data/local/tmp || mkdir /data/local/tmp")
        self.adb.shell("test -d /data/local/tmp/LLSIFKeyTouchScripts || mkdir /data/local/tmp/LLSIFKeyTouchScripts")
        for file in self.TOUCH_SCRIPTS_FILELIST:
            self.adb.push(self.TOUCH_SCRIPTS_DIR + file, "/data/local/tmp/LLSIFKeyTouchScripts/")
            self.adb.shell("chmod 777 /data/local/tmp/LLSIFKeyTouchScripts/" + file)
