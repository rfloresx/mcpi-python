#! /usr/bin/python
import mcpi.block as block
import random

""" draw a building

    @author: goldfish"""

def drawBuilding(mc, locx, locy, locz, floors, width, depth, floorheight, wallmaterial, floormaterial ):
    topx = locx+width
    topy = locy+((floorheight+1)*floors)
    topz = locz+depth
    #draw building shell
    mc.setBlocks( locx, locy, locz, topx, topy, topz, wallmaterial )
    mc.setBlocks( locx+1, locy+1, locz+1, topx-1, topy-1, topz-1, block.AIR )
    #draw floors
    if( floors > 1 ):
        for i in range( floors -1 ):
            floorYloc = locy+( (floorheight+1)*(i+1) )
            mc.setBlocks( locx+1, floorYloc, locz+1, topx-1, floorYloc, topz-1, floormaterial )
    #draw door
    doorloc = random.randint( 1, width-2 )
    mc.setBlock( locx, locy+1, locz+doorloc, block.AIR )
    mc.setBlock( locx, locy+2, locz+doorloc, block.AIR )
    #draw front windows
    if( floors > 1 ):
        for i in range( floors-1 ):
            windowYloc = locy+2+( (floorheight+1)*(i+1) )
            for j in range( floorheight-1 ):
                mc.setBlocks( locx, windowYloc+j , locz+1, locx, windowYloc+j, locz+(width-1), block.GLASS_PANE )
    #draw back windows
    if( floors > 1 ):
        for i in range( floors-1 ):
            windowYloc = locy+2+( (floorheight+1)*(i+1) )
            for j in range( floorheight-1 ):
                mc.setBlocks( locx+depth, windowYloc+j , locz+1, locx+depth, windowYloc+j, locz+(width-1), block.GLASS_PANE )

if __name__ == "__main__":
    import server
    pos = server.mc.player.getPos()
    pos.y -= 1
    width = 10
    depth = 10
    drawBuilding(server.mc, pos.x - width/2,pos.y,pos.z - depth/2, 10, width, depth, 5, block.BRICK_BLOCK, block.WOOD)