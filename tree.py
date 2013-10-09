'''
Created on Oct 8, 2013

@author: Otrebor45
'''
from mcpi.vec3 import Vec3
import mcpi.block as block

def spawnTree(mc,rpos,stem,leaf):
    pos = Vec3(rpos.x+1, rpos.y, rpos.z)
    height = 4
    for y in range(0,height):
        if y == int(height/2)+1:
            makeLeaf(mc, pos, height/2+1,leaf)
        mc.setBlock(pos.x, pos.y, pos.z,stem)
        pos.y+=1

def makeLeaf(mc, pos, radius, leaf):    
    for y in range(0, radius):
        for x in range(radius*-1,radius):        
            for z in range(radius*-1,radius):
                if x**2 + y**2 + z**2 < radius**2-1:
                    mc.setBlock(pos.x + x, pos.y + y, pos.z - z, leaf)
                    
                    
if __name__ == "__main__":
    import server
    spawnTree(server.mc,server.mc.player.getPos(),block.WOOD,block.LEAVES)