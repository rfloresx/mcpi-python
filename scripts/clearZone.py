#! /usr/bin/python
import mcpi.block as block

""" clearZone clears an area and sets a stone floor
    takes two x,z pairs clears everything above 0y and then sets
    a stone floor at -1y
    @author: goldfish"""

def clearZone(mc, alocx, alocz, blocx, blocz ):
    mc.setBlocks( alocx, 0, alocz, blocx, 64, blocz, block.AIR )
    mc.setBlocks( alocx, -1, alocz, blocx, -1, blocz, block.STONE )


