Love Live! School Idol Festival: Keyboard Controller
====================================================

Keyboard Controller for Love Live! School Idol Festival for Android.
This is done by simulating/sending touch event via ADB.

TL;DR
-----
Do not use it!

Requirements
------------
* Python 2.7
* Pygame 1.9.1
* ADB
* Programming Skills 

Warnings
--------
The currently supported devices are only limited to devices I have...

* ZTE Grand X (ZTE V970M)
* LG Optimus One (LG P500)

Because each devices aren't handling touch event the same way.
So, you need to create a device module for your own device.
You can study from the device modules that already exists in Devices directory.
Also, you need to modify **Devices/DeviceDetector.py** and **Devices/\_\_init\_\_.py** to include your device module too.

Notes
-----
* To change keys configuration edit **KeyConfig.py**
* To change path to ADB executable or device serial number edit **Devices/ADB/ADBConfig.py**

Contacts
--------
[xerodotc's Contacts Detail](http://xerodotc.wordpress.com/contacts/)
