'''
Created on Oct 5, 2013

@author: Otrebor45
'''
import mcpi.block as block
from mcpi.vec3 import Vec3 as Vec3
from random import randint as rand

def swapBlock(mc,pos1,pos2):
    b1 = mc.getBlockWithData(pos1.x, pos1.y, pos1.z)
    b2 = mc.getBlockWithData(pos2.x, pos2.y, pos2.z)
    mc.setBlock(pos1.x, pos1.y, pos1.z,b2)
    mc.setBlock(pos2.x, pos2.y, pos2.z,b1)
    
def makeNextPos(pos):
    d = rand(0,5)
    if d == 0:#nort
        return Vec3(pos.x+1, pos.y, pos.z)
    if d == 1:#sourt
        return Vec3(pos.x-1, pos.y, pos.z)
    if d == 2:#east
        return Vec3(pos.x+1, pos.y, pos.z+1)
    if d == 3:#west
        return Vec3(pos.x+1, pos.y, pos.z-1)
    if d == 4:#up
        return Vec3(pos.x, pos.y+1, pos.z)
    if d == 5:#down
        return Vec3(pos.x, pos.y-1, pos.z)
        
        
        
def movableBlock(mc,pos1):
    mc.setBlock(pos1.x, pos1.y, pos1.z, block.NETHER_REACTOR_CORE)
    while True:
        pos2 = makeNextPos(pos1)
        swapBlock(mc,pos1,pos2)
        pos1 = pos2
        #time.sleep(1)