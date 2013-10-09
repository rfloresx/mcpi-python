'''
Created on Oct 8, 2013

@author: Otrebor45
'''
from mcpi.vec3 import Vec3
import mcpi.block as block

blocksize = 2

def shoes(mc, cpos, block):
    pos = Vec3(cpos.x - blocksize, cpos.y ,cpos.z )
    mc.setBlocks(pos.x,pos.y,pos.z, pos.x +2*blocksize -1, pos.y+blocksize -1, pos.z+blocksize-1, block)

def legs(mc,cpos,block):
    pos = Vec3(cpos.x - blocksize, cpos.y +blocksize,cpos.z )
    mc.setBlocks(pos.x,pos.y,pos.z, pos.x +2*blocksize -1, pos.y+2*blocksize -1, pos.z+blocksize-1, block)
    
def shirt(mc,cpos,block):
    pos = Vec3(cpos.x - blocksize, cpos.y +3*blocksize,cpos.z )
    mc.setBlocks(pos.x,pos.y,pos.z, pos.x +2*blocksize -1, pos.y+2*blocksize - 1, pos.z+blocksize-1, block)
    pos = Vec3(cpos.x - 2*blocksize, cpos.y +5*blocksize,cpos.z )
    mc.setBlocks(pos.x,pos.y,pos.z, pos.x +4*blocksize -1 , pos.y+blocksize - 1 , pos.z+blocksize-1, block)
    
def arms(mc,cpos,block):
    pos = Vec3(cpos.x - 2*blocksize, cpos.y + 3*blocksize,cpos.z )
    mc.setBlocks(pos.x,pos.y,pos.z, pos.x + blocksize-1, pos.y+2*blocksize -1, pos.z+blocksize-1, block)
    pos = Vec3(cpos.x + blocksize, cpos.y + 3*blocksize, cpos.z )
    mc.setBlocks(pos.x,pos.y,pos.z, pos.x + blocksize-1, pos.y+2*blocksize -1, pos.z+blocksize-1, block)

def head(mc,cpos,block):
    pos = Vec3(cpos.x - blocksize, cpos.y + 6*blocksize, cpos.z-blocksize/2)
    mc.setBlocks(pos.x,pos.y,pos.z, pos.x + 2*blocksize-1, pos.y+2*blocksize -1, pos.z+2*blocksize-1, block)
    
def steve(mc,pos):
    w = block.WOOL.id
    shoes(mc,pos,block.Block(w,7 ))
    legs (mc,pos,block.Block(w,11))
    shirt(mc,pos,block.Block(w,3 ))
    arms (mc,pos,block.Block(w,6 ))
    head (mc,pos,block.Block(w,6 ))
    
if __name__ == "__main__":
    import server
    pos = server.mc.player.getPos()
    pos.x += 2*blocksize
    steve(server.mc, pos)
    