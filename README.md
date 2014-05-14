Love Live! School Idol Festival: Keyboard Controller
====================================================

Keyboard Controller for Love Live! School Idol Festival for Android.
This is done by simulating/sending touch event via ADB.

TL;DR
-----
Do not use it!

Requirements
------------
* [Python 2.7](https://www.python.org/)
* [Pygame 1.9.1](http://www.pygame.org/)
* Android Debug Bridge
 * Ubuntu (and maybe its derivative) users: *sudo apt-get install android-tools-adb*
 * Linux users: There might be ADB available in your repository. Please check by yourself.
 * Windows/OS X/Linux users: [Download ADT Bundle](http://developer.android.com/sdk/index.html) then extract the package. ADB is located in adt-bundle.../sdk/platform-tools/.
* Programming Skills 

Warnings
--------
The currently supported devices are only limited to devices I have...

* ZTE Grand X (ZTE V970M)
* LG Optimus One (LG P500)

Because each devices aren't handling touch event the same way.
So, you need to create a device module for your own device.
You can study from the device modules that already exists in Devices directory.
Also, you need to modify *Devices/DeviceDetector.py* and *Devices/\_\_init\_\_.py* to include your device module too.

Notes
-----
* **You need to enable USB debugging option and connect the device via USB cable.**
* To change keys configuration edit *KeyConfig.py*
* To change path to ADB executable or device serial number edit *Devices/ADB/ADBConfig.py*

###For Windows user
I didn't distribute .exe file for this because it'll need some code modification.
I recommend to download and install Python, Pygame, ADB from the link in the requirements section, then modify some configuration (such as path to ADB executable) and run it.

By the way, I use Ubuntu...

Contacts
--------
[xerodotc's Contacts Detail](http://xerodotc.wordpress.com/contacts/)
