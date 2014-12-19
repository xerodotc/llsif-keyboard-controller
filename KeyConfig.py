#!/usr/bin/env python2

'''
Love Live! School Idol Festival: Keyboard Controller
File: KeyConfig.py

Copyright (c) 2014 Visatouch Deeying ("xerodotc")
Love Live! School Idol Festival is a trademark of KLab and Bushiroad
'''

import pygame
from pygame.locals import *

# Key configuration
PAUSE = K_BACKSPACE
QUIT = K_ESCAPE
LEFT_4 = K_a
LEFT_3 = K_s
LEFT_2 = K_d
LEFT_1 = K_f
MIDDLE = K_SPACE
RIGHT_1 = K_j
RIGHT_2 = K_k
RIGHT_3 = K_l
RIGHT_4 = K_SEMICOLON

# Keys array
KEYS_ARRAY = [PAUSE, LEFT_4, LEFT_3, LEFT_2, LEFT_1, MIDDLE, RIGHT_1, RIGHT_2, RIGHT_3, RIGHT_4]

# getKeyName Function
def getKeyName(key):
	if key >= K_a and key <= K_z:
		return chr(key - K_a + 65)
	elif key == K_SPACE:
		return "space"
	return chr(key)
