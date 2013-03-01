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
pits = {}
time = 480
artifacts = 0

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

# Play the game!
while time > 0:
    gridx = raw_input("X coord of pit you'd like to dig? ")
    gridy = raw_input("Y coord of pit you'd like to dig? ")
    if 0 < int(gridx) < 11 and 0 < int(gridy) < 11:
        results = digPit(int(gridx), int(gridy))
        time -= results[0]
        artifacts += results[1]
        print "You've found " + str(artifacts) + " artifacts!"
        print "Remaining time: " + str(time/60) + " hours and " + str(time%60) + " minutes."
        print str(len(pits)) + " pits remaining!\n"
    else:
        print "\nNot a valid pit\n"
        
print "\nCongratulations!  You finished a day of archaeology!"
