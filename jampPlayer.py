'''
Created on Oct 7, 2013

@author: Otrebor45
'''
import scripts.movePlayer as playerMove
import mcpi.minecraft as minecraft
import server
if __name__ == "__main__":
    mc = minecraft.Minecraft.create(server.address)
    playerMove.jampPlayer(mc.player, 10)