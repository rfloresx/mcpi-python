'''
Created on Oct 5, 2013

@author: Otrebor45
'''
import mcpi.block as block

def createHolloSphere(mc,blocktype):
    radius = 3
    playerPos = mc.player.getPos()
    for x in range(radius*-1,radius):
        for y in range(radius*-1, radius):
            for z in range(radius*-1,radius):
                if x**2 + y**2 + z**2 < (radius -1 )**2:#inside sphere
                    mc.setBlock(playerPos.x + x, playerPos.y + y+1, playerPos.z + z, block.AIR)
                elif x**2 + y**2 + z**2 < radius**2:
                    mc.setBlock(playerPos.x + x, playerPos.y + y+1, playerPos.z + z, blocktype)
                    
def playerBall(mc):
    while True:
        createHolloSphere(mc,block.GLASS)