Love Live! School Idol Festival: Keyboard Controller
====================================================

Keyboard Controller for Love Live! School Idol Festival for Android.
This is done by simulating/sending touch event via ADB.

TL;DR
-----
Do not use it! It's unpractical and not maintained anymore. It's okay to poke around the source code though.

Requirements
------------
* [Python 2.7](https://www.python.org/)
* [Pygame 1.9.1](http://www.pygame.org/)
* Android Debug Bridge
 * Ubuntu (and maybe its derivative) users: `sudo apt-get install android-tools-adb`
 * Linux users: There might be ADB available in your repository. Please check by yourself.
 * Windows/OS X/Linux users: [Download ADT Bundle](http://developer.android.com/sdk/index.html) then extract the package. ADB is located in `sdk/platform-tools/`.
* [pyHook](http://sourceforge.net/projects/pyhook/) and [pywin32](http://sourceforge.net/projects/pywin32/) (Optional; Used for unfocused window keystroke detection, useful to Bluestacks user)
* Programming Skills 

Warnings
--------
The currently supported devices are only limited to devices I have...

* ZTE Grand X (ZTE V970M)
* LG Optimus One (LG P500)

Because each devices aren't handling touch event the same way.
So, you need to create a device module for your own device.
You can study from the device modules that already exists in Devices directory.
Also, you need to modify `Devices/DeviceDetector.py` and `Devices/\_\_init\_\_.py` to include your device module too.

### Guide for creating touch scripts for your devices
*This is not same as device module file (Python class file)*

* Enable USB debugging and connect your device.
* Run `adb shell getevent`, turn on your device screen, touch the screen many many time and observe an output.
* You should know which device file is for touchscreen at this time, you can observe again by run `adb shell getevent | grep /dev/input/<device file>` (Linux only)
* Reverse engineer it!
* By the way, you can simulate/send event using *sendevent* command on device
* There are some touch scripts already available for some devices located in `Devices/TouchScripts/`

Notes
-----
* **You need to enable USB debugging option and connect the device via USB cable.**
* To change keys configuration edit `KeyConfig.py`
* To change path to ADB executable or device serial number edit `Devices/ADB/ADBConfig.py`

### For Windows user
I didn't distribute .exe file for this because it'll need some code modification.
I recommend to download and install Python, Pygame, ADB from the links in the requirements section, then modify some configuration (such as path to ADB executable) and run it.
