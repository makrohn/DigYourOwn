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

import random

# Determine how hard it is to dig a pit.
difficulty = {5: 'clay', 4: 'rocky till', 3: 'roots', 2: "silt", 1: "beach sand"}
def difficultyGen():
    numDiff = random.randint(1,5)
    return numDiff
def nameDiff(numDiff):
    nameDiff = difficulty[numDiff]
    return nameDiff
