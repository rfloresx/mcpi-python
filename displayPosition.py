import time

def disPos(mc):
    #Find out your players position
    playerPos = mc.player.getPos()
    mc.postToChat("Find your position - its x=%s y=%s z=%s" % (int(playerPos.x), int(playerPos.y), int(playerPos.z)))
    #mc.postToChat("Find your position - its x=%.2f y=%.2f z=%.2f" % (playerPos.x, playerPos.y, playerPos.z))
    time.sleep(1)

if __name__ == "__main__":
    import server
    disPos(server.mc)