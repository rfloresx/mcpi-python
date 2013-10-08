'''
Created on Oct 7, 2013

@author: caseybrichardson
'''
from mcpi.vec3 import Vec3 as Vec3
import mcpi.minecraft as minecraft
import mcpi.block as block
import server
import random
import sys

def clearArea(mc,spos, epos, blockClear = block.AIR.id, blockReplace = block.AIR.id, deleteAll = True):
    for x in range(int(spos.x), int(epos.x)):
        for y in range(int(spos.y),int(epos.y)):
            for z in range(int(spos.z), int(epos.z)):
                if mc.getBlockWithData(x, y, z).id == blockClear or deleteAll:
                    mc.setBlock(x, y, z, blockReplace)
    
def checkValid(id):
    return (id >= 0 and id <= 98) or id == 102 or id == 103 or id == 107 or id == 246 or id == 247
        

if __name__ == "__main__":
    length = len(sys.argv)

    mc = minecraft.Minecraft.create(server.address)
    startPos = mc.player.getPos()
    endPos = mc.player.getPos()
    const = 4;
    startPos.x = startPos.x - const
    startPos.y = startPos.y - const
    startPos.z = startPos.z - const
    endPos.x = endPos.x + const
    endPos.y = endPos.y + const
    endPos.z = endPos.z + const
    
    if length == 1:
        clearArea(mc, startPos, endPos)
    elif length == 2:
        if checkValid(int(sys.argv[1])):
            clearArea(mc, startPos, endPos, int(sys.argv[1]), block.AIR.id, False)
        else:
            print "Invalid block type!"
    elif length >= 3:
        if checkValid(int(sys.argv[1])) and checkValid(int(sys.argv[2])):
            clearArea(mc, startPos, endPos, int(sys.argv[1]), int(sys.argv[2]), False)  