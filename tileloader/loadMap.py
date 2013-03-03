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
import pyglet

class mapTile(object):
    def __init__(self,image,x,y):
        self.image = image
        self.x = x
        self.y = y

def loadTileset(tileset):
    tileSetIndex = {}
    tileset = pyglet.image.load(tileset)
    width = tileset.width
    height = tileset.height
    x = 0
    y = tileset.height
    tileNumber = 1
    while y > 0:
        while x < tileset.width:
            tile = tileset.get_region(x, y-32, 32, 32)
            tileSetIndex[tileNumber] = tile
            x += 32
            tileNumber += 1
        x = 0
        y -= 32
    return tileSetIndex

def loadTmx(tmxfile):
    tmxMap = []
    tmx = open(tmxfile, 'r+')
    for line in tmx:
        if "<" not in line:
            line = line.strip('\n')
            tileNum = line.split(',')
            tmxMap.append(tileNum)
    tmxMap = tmxMap[::-1]
    return tmxMap

def renderTiles(tmxMap, tileSet):
    tiles = []
    y = 0
    for yrow in tmxMap:
        x = 0
        for tileIndex in yrow:
            if tileIndex != "":
                tile = mapTile(tileSet[int(tileIndex)],x,y)
                tiles.append(tile)
                x += 32
        y += 32
    return tiles
