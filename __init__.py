import server as server
import mcpi.minecraft as minecraft
from mcpi.vec3 import Vec3 as Vec3

import scripts.bunker as bunker
from maze import MakeMaze as maze

#scripts
#make world flat
import scripts.flatworld as flatworld
#make rails
import scripts.railgen as rails

import scripts.ejectcd as eject

import mazeGame as game

import movePlayer as jamm

import cristallBall as ball

import magic as mblock

import minheap as minheap
mc = minecraft.Minecraft.create(server.address)
ppos = mc.player.getPos();
#mc.postToChat("hello")
#mc.player.setPos(0,0,0)

if __name__ == "__main__":
    mc.player.setPos(0,12,0)
    minheap.runSort(mc, Vec3(0,10, 0), 50)
    #game.mazeGame(mc, Vec3(0,0,0)).infMazeGame()
    #flatworld.flatworld(mc)
    #ball.playerBall(mc)
    #mblock.movableBlock(mc, Vec3(0,10,0))
    #jamm.jampPlayer(mc.player, 50)