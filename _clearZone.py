#! /usr/bin/python
import mcpi.block as block

""" clearZone clears an area and sets a stone floor
    takes two x,z pairs clears everything above 0y and then sets
    a stone floor at -1y
    @author: goldfish"""

def clearZone(mc,pos,size ):
    mc.setBlocks( pos.x, pos.y, pos.z, pos.x+size.x, pos.y+size.y, pos.z+size.z, block.AIR )
    #mc.setBlocks( pos.x, -1, alocz, blocx, -1, blocz, block.STONE )

if __name__ == "__main__":
    from mcpi.vec3 import Vec3
    import server
    pos = server.mc.player.getPos()
    size = Vec3(50,5,50)
    pos.x -= size.x/2
    pos.z -= size.z/2
    clearZone(server.mc, pos, size)