import scr.server as server
import mcpi.minecraft as minecraft
from mcpi.vec3 import Vec3 as Vec3

import scr.scripts.bunker as bunker
from scr.maze import MakeMaze as maze

#scripts
#make world flat
import scr.scripts.flatworld as flatworld
#make rails
import scr.scripts.railgen as rails

import scr.scripts.ejectcd as eject

import scr.mazeGame as game

import scr.movePlayer as jamm

import scr.cristallBall as ball

import scr.magic as mblock

import scr.minheap as minheap
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