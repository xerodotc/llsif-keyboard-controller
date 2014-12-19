#!/usr/bin/env python2

'''
Love Live! School Idol Festival: Keyboard Controller
File: LLSIFKey.py

Copyright (c) 2014 Visatouch Deeying ("xerodotc")
Love Live! School Idol Festival is a trademark of KLab and Bushiroad
'''

import sys, platform, ConfigParser
import pygame
hasPyHook = False
try:
	import pyHook, pythoncom
	hasPyHook = True
except ImportError, e:
	pass
from Devices import Device # Wait for device is already handled here
import UIConfig, KeyConfig

dev = None

def main():
	global hasPyHook, dev
	
	# Initialize ADB and push some touching scripts
	device = Device()
	device.pushScripts()
	
	usePyHook = False
	if hasPyHook and device.PYHOOK:
		usePyHook = True
	
	if usePyHook:
		dev = device
		hooks_manager = pyHook.HookManager()
		hooks_manager.KeyDown = pyHookOnKeyDown
		hooks_manager.KeyUp = pyHookOnKeyUp
		hooks_manager.HookKeyboard()
	
	# Initialize pygame module
	pygame.init()
	pygame.font.init()

	pygame.display.set_mode(UIConfig.WINDOW_SIZE)
	pygame.display.set_caption("Love Live! School Idol Festival: Keyboard Controller")
	screen = pygame.display.get_surface()
	screen.fill(UIConfig.BG_COLOR)
	
	config = ConfigParser.ConfigParser(allow_no_value=True)
	config.read('config.cfg')
	if config.getboolean("Main", "iconify"):
		pygame.display.iconify()

	firstFrame = True

	keyFont = pygame.font.Font(None, UIConfig.KEY_FONT_SIZE)
	pauseFont = pygame.font.Font(None, UIConfig.PAUSE_FONT_SIZE)

	while True:
		try:
			screenUpdate = False
			# Alway update screen for first frame
			if firstFrame:
				screenUpdate = True
				firstFrame = False

			# Detect keyboard input and send to device module for handling
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					keyData = getKey(event.key)
					if keyData == -1:
						sys.exit()
					elif not usePyHook and keyData > -1:
						screenUpdate = True
						device.registerKey(keyData)
				elif event.type == pygame.KEYUP:
					keyData = getKey(event.key)
					if keyData == -1:
						sys.exit()
					elif not usePyHook and keyData > -1:
						screenUpdate = True
						device.unregisterKey(keyData)
			
			if usePyHook:
				pythoncom.PumpWaitingMessages()
				screenUpdate = True

			# Update touch event on devices (up to device module)
			device.updateTouch()

			# Update UI
			if screenUpdate:
				# Pause button
				if device.isKeyPressed(0):
					pygame.draw.rect(screen, UIConfig.PAUSE_BUTTON_PRESSED_COLOR, pygame.Rect(UIConfig.PAUSE_BUTTON_POS, UIConfig.PAUSE_BUTTON_SIZE))
				else:
					pygame.draw.rect(screen, UIConfig.PAUSE_BUTTON_UNPRESSED_COLOR, pygame.Rect(UIConfig.PAUSE_BUTTON_POS, UIConfig.PAUSE_BUTTON_SIZE))
				pygame.draw.rect(screen, UIConfig.PAUSE_BUTTON_BORDER_COLOR, pygame.Rect(UIConfig.PAUSE_BUTTON_POS, UIConfig.PAUSE_BUTTON_SIZE), UIConfig.PAUSE_BUTTON_BORDER_WIDTH)
				text = pauseFont.render("| |", 1, UIConfig.PAUSE_FONT_COLOR)
				textpos = text.get_rect()
				textpos.centerx = UIConfig.PAUSE_BUTTON_POS[0] + (UIConfig.PAUSE_BUTTON_SIZE[0] / 2)
				textpos.centery = UIConfig.PAUSE_BUTTON_POS[1] + (UIConfig.PAUSE_BUTTON_SIZE[1] / 2)
				screen.blit(text, textpos)
				# Each circles
				i = 0
				for c in UIConfig.CIRCLE_POSITION:
					if c == None:
						i += 1
						continue
					if device.isKeyPressed(i):
						pygame.draw.circle(screen, UIConfig.CIRCLE_PRESSED_COLOR, c, UIConfig.CIRCLE_RADIUS)
					else:
						pygame.draw.circle(screen, UIConfig.CIRCLE_UNPRESSED_COLOR, c, UIConfig.CIRCLE_RADIUS)
					pygame.draw.circle(screen, UIConfig.CIRCLE_BORDER_COLOR, c, UIConfig.CIRCLE_BORDER_RADIUS, UIConfig.CIRCLE_BORDER_WIDTH)
					text = keyFont.render(KeyConfig.getKeyName(KeyConfig.KEYS_ARRAY[i]), 1, UIConfig.KEY_FONT_COLOR)
					textpos = text.get_rect()
					textpos.centerx = c[0]
					textpos.centery = c[1]
					screen.blit(text, textpos)
					i += 1
				# Update screen
				pygame.display.flip()
		except KeyboardInterrupt as e:
			break
			
# pyHook Key Handler
def pyHookOnKeyDown(event):
	global dev
	keyData = getKey(event.Ascii)
	if keyData > -1:
		dev.registerKey(keyData)
	#print "KeyDown " + str(event.Ascii)
	return True
def pyHookOnKeyUp(event):
	global dev
	keyData = getKey(event.Ascii)
	if keyData > -1:
		dev.unregisterKey(keyData)
	#print "KeyUp " + str(event.Ascii)
	return True

# Key code to button code
def getKey(key):
	if key == KeyConfig.QUIT:
		return -1
	elif key == KeyConfig.PAUSE:
		return 0
	elif key == KeyConfig.LEFT_4:
		return 1
	elif key == KeyConfig.LEFT_3:
		return 2
	elif key == KeyConfig.LEFT_2:
		return 3
	elif key == KeyConfig.LEFT_1:
		return 4
	elif key == KeyConfig.MIDDLE:
		return 5
	elif key == KeyConfig.RIGHT_1:
		return 6
	elif key == KeyConfig.RIGHT_2:
		return 7
	elif key == KeyConfig.RIGHT_3:
		return 8
	elif key == KeyConfig.RIGHT_4:
		return 9
	return -256

if __name__ == "__main__": main() # Run main function
