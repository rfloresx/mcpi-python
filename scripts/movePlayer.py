'''
Created on Oct 5, 2013

@author: Otrebor45
'''
from mcpi.vec3 import Vec3 as Vec3

import time
from random import randint as rand

def moveNorth(player):
    pos = player.getPos()
    player.setPos(pos.x+1, pos.y, pos.z)
    
def moveSourt(player):
    pos = player.getPos()
    player.setPos(pos.x-1, pos.y, pos.z)
    
def moveEast(player):
    pos = player.getPos()
    player.setPos(pos.x, pos.y, pos.z+1)
    
def moveWest(player):
    pos = player.getPos()
    player.setPos(pos.x, pos.y, pos.z-1)
    
def moveUp(player):
    pos = player.getPos()
    player.setPos(pos.x, pos.y+1, pos.z)
    
def moveDown(player):
    pos = player.getPos()
    player.setPos(pos.x, pos.y-1, pos.z)
    
def jampPlayer(player,t):
    mt = time.time()
    while time.time() <= mt + t:
        dir = rand(0,5)
        if dir == 0:
            moveNorth(player)
        if dir == 1:    
            moveSourt(player)
        if dir == 2:   
            moveEast(player)
        if dir == 3:   
            moveWest(player)
        if dir == 4:   
            moveUp(player)
        if dir == 5:
            moveDown(player)
        time.sleep(.2)

def lauchPlayer(player, dir = Vec3(0,0,0)):
    pos = player.getPos()
    flor = pos.y
    while dir.y > 0 or pos.y > flor:
        pos = player.getPos()
        player.setPos(pos.x + dir.x, pos.y + dir.y, pos.z + dir.z)
        dir.y -= .1
        if dir.y < 0:
            dir.y = 0
        pos = player.getPos()
        #time.sleep(.2)
    
    
    
    
    