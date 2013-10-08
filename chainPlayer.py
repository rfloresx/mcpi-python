'''
Created on Oct 7, 2013

@author: Otrebor45
'''
import time
import math

def distanceBetweenPoints(point1, point2):
    xd = point2.x - point1.x
    yd = point2.y - point1.y
    zd = point2.z - point1.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))



if __name__ == "__main__":
    CHAINTIME = 25
    CHAINLENGTH = 10
    import server 
    
    lock = server.mc.player.getPos()
    stime = time.time()
    ppos = server.mc.player.getPos()
    
    while stime + CHAINTIME > time.time():
        if distanceBetweenPoints( server.mc.player.getPos(), lock  ) > CHAINLENGTH:
            server.mc.player.setPos( ppos.x,ppos.y, ppos.z )
        if distanceBetweenPoints( server.mc.player.getPos(), lock  ) < CHAINLENGTH - 1:
            ppos = server.mc.player.getPos()