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
from artifactGen import artifactGen
from diffGen import difficultyGen
from diffGen import nameDiff

class pit(object):
    def __init__(self, x, y):
        self.name = str("pit" + str(x) + "x" + str(y))
        self.x = x
        self.y = y
        self.arts = artifactGen()
        self.diffNum = difficultyGen()
        self.diffName = nameDiff(self.diffNum)
        self.duration = self.arts * 2 + self.diffNum * 5
