
import mcpi.block as block

def flatMap(mc, pos):
    # write the rest of your code here...
    print "erasing 50x50 block..."
    mc.postToChat("Erasing a 50x50 block...")
    mc.setBlocks(pos.x-50,-10,pos.z-50, pos.x+50, 10,pos.z+50,block.AIR.id)
    mc.setBlocks(pos.x-50, 00,pos.z-50, pos.x+50,-10,pos.z+50,block.DIRT.id)
    mc.postToChat("Done Erasing a 50x50 block!")
    print "Done Erasing a 50x50 block!"

if __name__ == "__main__":
    import server
    flatMap(server.mc, server.mc.player.getPos())

