'''
Created on Oct 7, 2013

@author: Otrebor45
'''

if __name__ == "__main__":
    from mcpi.vec3 import Vec3
    import mazeGame as game
    import server
    server.mc.player.setPos(1,0,1)
    gm = game.mazeGame(server.mc,Vec3(0,0,0))
    gm.invMazeGame()