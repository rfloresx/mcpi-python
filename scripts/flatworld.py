#!/usr/bin/env python

import mcpi.block as block

def flatworld(mc):
    print "Cleaning world..."
    mc.setBlocks(-128,0,-128,128,64,128,0)
    mc.setBlocks(-128,0,-128,128,-64,128,block.DIRT.id)
    print "Done"
