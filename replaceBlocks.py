'''
Created on Oct 7, 2013

@author: Otrebor45
'''
from mcpi.vec3 import Vec3
def replaceBlocks(mc, fromBlock,toBlock):
    size = Vec3(5,2,5)
    pos = mc.player.getPos()
    for x in range( -int(size.x), int(size.x)):
        for y in range(-int(size.y), int(size.y)):
            for z in range(-int(size.z),int(size.z)):
                if mc.getBlockWithData(pos.x+x,pos.y+y,pos.z+z).id == fromBlock.id:
                    mc.setBlock(pos.x+x,pos.y+y,pos.z+z,toBlock)
                    
if __name__ == "__main__":
    import server
    import mcpi.block as block
    replaceBlocks(server.mc,block.DIRT, block.GLASS)