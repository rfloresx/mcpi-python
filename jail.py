'''
Created on Oct 7, 2013

@author: Otrebor45
'''
import time
from mcpi.vec3 import Vec3
def jailPlayer(mc, posI, blocktype):
    size = 6
    pos = Vec3(posI.x-size/2, posI.y-size/2, posI.z-size/2)
    for x in range(0,size+1):
        for y in range(0,size+1):
            for z in range(0,size+1):
                if x == 0 or y == 0 or z == 0:
                    mc.setBlock(pos.x+x, pos.y+y,pos.z+z, blocktype)
                if x == size or y == size or z == size:
                    mc.setBlock(pos.x+x, pos.y+y,pos.z+z, blocktype) 
                
            
        

if __name__ == "__main__":
    jailtime = 25
    import server
    import mcpi.block as block
    stime = time.time()
    pos = server.mc.player.getPos()
    while stime + jailtime >= time.time():
        jailPlayer(server.mc, pos, block.FENCE)