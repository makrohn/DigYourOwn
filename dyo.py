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
pits = []
dugPits = []
time = 480
artifacts = 0
class pit(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.arts = genPit.artifactGen()
        self.diffNum = genPit.difficultyGen()
        self.diffName = genPit.nameDiff(self.diffNum)
for i in range (1,11):
    for j in range (1,11):
        dugPit = pit(i,j)
        pits.append(dugPit)
def digPit(x,y):
    for dugPit in dugPits:
        if dugPit.x == x and dugPit.y == y:
            print "You dug that pit already!"
            return 0
    for dugPit in pits:
        if dugPit.x == x and dugPit.y == y:
#            print dugPit.x
#            print dugPit.y
#            print dugPit.arts
#            print dugPit.diffNum
            dugPits.append(dugPit)
            pits.remove(dugPit)
#            print dugPit.diffName
            duration = dugPit.arts * 2 + dugPit.diffNum * 5
            print "You found " + str(dugPit.arts) + " artifacts in a pit of " + dugPit.diffName + "!"
            print "It took you " + str(duration) + " minutes!"
            return duration
#for dugPit in pits:
#    print dugPit.arts
#    print dugPit.diffNum
#    print dugPit.diffName
#    print dugPit.x
#    print dugPit.y
print len(pits)
while time > 0:
    gridx = raw_input("X coord of pit you'd like to dig? ")
    gridy = raw_input("Y coord of pit you'd like to dig? ")
    if 0 < int(gridx) < 11 and 0 < int(gridy) < 10:
        time -= digPit(int(gridx), int(gridy))
        print "Remaining time: " + str(time)
        print str(len(pits)) + " pit remaining!"
    else:
        print "Not a valid pit"
print "Congratulations!  You finished a day of archaeology!"
