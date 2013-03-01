#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Copyright 2013 Matthew Krohn
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
import genPit
from genPit import pit
import pyglet
from pyglet.window import mouse
from pyglet.gl import *

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

gameWindow = pyglet.window.Window()
siteMap = pyglet.resource.image('resources/map.png')
xMark = pyglet.image.load('resources/x.png')

pits = {}
time = 480
artifacts = 0
gridx = -32
gridy = -32
marks = []

# Function to find the target pit and report what's in it        
def digPit(x,y):
    pitName = str("pit" + str(x) + "x" + str(y))
    if pitName in pits:
        duration = pits[pitName].arts * 2 + pits[pitName].diffNum * 5
        print "\nYou found " + str(pits[pitName].arts) + " artifacts in a pit of " + pits[pitName].diffName + "!"
        print "It took you " + str(duration) + " minutes!"
        arts = pits[pitName].arts
        del pits[pitName]
        return [duration, arts]
    else:
        print "\nYou dug that pit already!"
        return [0, 0]

# Generate a 10x10 grid full of pits.
for i in range (1,11):
    for j in range (1,11):
        dugPit = pit(i,j)
        pits[dugPit.name] = dugPit
        
def pickPit(x, y):
    if 0 < x < 11 and 0 < y < 11:
        results = digPit(x, y)
        global time
        global artifacts
        time -= results[0]
        artifacts += results[1]
        print "You've found " + str(artifacts) + " artifacts!"
        marks.append([gridx, gridy])
        print marks
        if time > 0:
            print "Remaining time: " + str(time/60) + " hours and " + str(time%60) + " minutes."

@gameWindow.event
def on_draw():
    gameWindow.clear()
    siteMap.blit(0,0)
    for mark in marks:
        xMark.blit((mark[0] - 1) * 32, (mark[1] - 1) * 32, 1)

@gameWindow.event
def on_mouse_press(x, y, button, modifiers):
    if time > 0:
        global gridx
        global gridy
        gridx = ((x - x % 32) / 32 + 1)
        gridy = ((y - y % 32) / 32 + 1)
        pickPit(gridx, gridy)
    if time < 0:
        gameWindow.close()
    
pyglet.app.run()

print "\nCongratulations!  You finished a day of archaeology!"
print "You found a total of %d artifacts!" % (artifacts)
