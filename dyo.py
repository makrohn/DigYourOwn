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
def digPit():
    print str(genPit.artifactGen()), 'Artifacts'
    difficulty = genPit.difficultyGen()
    print difficulty
    print genPit.nameDiff(difficulty)
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
#for dugPit in pits:
#    print dugPit.arts
#    print dugPit.diffNum
#    print dugPit.diffName
#    print dugPit.x
#    print dugPit.y
print len(pits)
gridx = raw_input("X coord of pit you'd like to dig? ")
gridy = raw_input("Y coord of pit you'd like to dig? ")
for dugPit in pits:
    if dugPit.x == int(gridx) and dugPit.y == int(gridy):
        print dugPit.x
        print dugPit.y
        print dugPit.arts
        print dugPit.diffNum
        pits.remove(dugPit)
        print dugPit.diffName
print len(pits)
