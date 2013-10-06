
import mcpi.block as block

def flatMap(mc):
    # write the rest of your code here...
    print "erasing 50x50 block..."
    mc.postToChat("Erasing a 50x50 block...")
    mc.setBlocks(-50,-10,-50,50,10,50,block.AIR.id)
    mc.setBlocks(-50,0,-50,50,-10,50,block.SANDSTONE.id)
    mc.postToChat("Done Erasing a 50x50 block!")
    print "Done Erasing a 50x50 block!"


