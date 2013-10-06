#!/usr/bin/env python


#import minecraft block module
import mcpi.block as block
import time

def railgen(mc):
    print "cleaning area"
    mc.setBlocks(-128,0,-128,128,64,128,0)
    mc.setBlocks(-128,0,-128,128,-64,128,block.DIRT.id)
    time.sleep(2)
    print "area cleaned"
    #    exit()
    mc.postToChat("Hello you have successfully ran Rail Gen :).")
    # create the station
    mc.setBlock(1,3,0,block.GLOWSTONE_BLOCK.id)
    mc.setBlock(0,0,0,block.STONE_SLAB.id)
    mc.setBlock(-1,1,0,block.DOOR_WOOD.id,0)
    mc.setBlock(-1,2,0,block.DOOR_WOOD.id,8)
    mc.setBlock(0,1,1,block.STONE.id)
    mc.setBlock(0,2,1,block.STONE.id)
    mc.setBlock(0,1,-1,block.STONE.id)
    mc.setBlock(0,2,-1,block.STONE.id)
    mc.setBlock(1,1,1,block.STONE.id)
    mc.setBlock(-1,1,1,block.STONE.id)
    mc.setBlock(0,1,1,block.STONE.id)
    mc.setBlock(1,1,-1,block.STONE.id)
    mc.setBlock(-1,1,-1,block.STONE.id)
    mc.setBlock(-1,2,-1,block.GLOWSTONE_BLOCK.id)
    mc.setBlock(1,2,-1,block.STONE.id)
    mc.setBlock(1,2,1,block.STONE.id)
    mc.setBlock(-1,2,1,block.GLOWSTONE_BLOCK.id)
    mc.setBlock(-1,3,0,block.STONE_SLAB.id)
    mc.setBlock(0,3,0,block.STONE_SLAB.id)
    # Create the path one direction
    mc.setBlocks(129,0,1,0,0,-1,block.STONE_SLAB)
    mc.setBlocks(0,1,2,128,1,2,block.STONE.id)
    mc.setBlocks(128,1,-2,0,1,-2,block.STONE.id)
    mc.setBlocks(128,0,2,0,0,2,block.GLOWSTONE_BLOCK.id)
    mc.setBlocks(128,0,-2,0,0,-2,block.GLOWSTONE_BLOCK.id)

