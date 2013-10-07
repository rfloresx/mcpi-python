'''
Created on Oct 4, 2013

@author: Otrebor45
'''
from mcpi.vec3 import Vec3 as Vec3
import mcpi.block as block
import random
import time
from random import randint as rand

    # Create a function for picking a random direction.
def randDir():
    r = rand(0,3)
    if r == 0: rv = (0,-1) # Up.
    if r == 1: rv = (0,1) # Down.
    if r == 2: rv = (-1,0) # Left.
    if r == 3: rv = (1,0) # Right.
    return rv

def makeWall(mc, x, y, z, h = 3, block = block.STONE):
    for i in range(0,h):
        mc.setBlock(x,y+i,z,block)

def clearArrea(mc,spos, epos):
    for x in range(0, int(epos.x)):
        for z in range(0, int(epos.z)):
            for y in range(0,int(epos.y)):
                mc.setBlock(spos.x+x,spos.y+y,spos.z+z, block.AIR)
    
class MakeMaze:
    def __init__(self,mci, sizex = 35, sizey = 5, sizez =35):
        self.mc = mci
        self.ppos = mci.player.getPos()
        self.ppos.y = self.ppos.y - 3
        self.mazeXSize = sizex
        self.mazeYSize = sizey
        self.mazeZSize = sizez
        self.maxWallLen = 2
        
    def initMaze(self,w,h):
        # Create a 2 dimensional array.
        self.maze = [[0]*h for x in range(w)]
    
        # Create four walls around the maze.
        # 1=wall, 0=walkway.
        for x in range(0,h):
            self.maze[x][0] = self.maze[x][h-1] = 1
            makeWall(self.mc, self.ppos.x+x, self.ppos.y, self.ppos.z+0)
            makeWall(self.mc, self.ppos.x+x, self.ppos.y, self.ppos.z+h-1)
        for y in range(0,w):
            self.maze[0][y] = self.maze[w-1][y] = 1
            makeWall(self.mc, self.ppos.x + 0, self.ppos.y, self.ppos.z+y)
            makeWall(self.mc, self.ppos.x+w-1, self.ppos.y, self.ppos.z+y)
        for x in range(0,w):
            for z in range(0,h):
                self.mc.setBlock(self.ppos.x+x, self.ppos.y-1,self.ppos.z+z, block.STONE)
               
        # Make every other cell a starting point.
        # 2=starting point.
        # Also create a list of these points to speed up the main loop.
        self.spl = []
        for y in range(2,h-2,2):
            for x in range(2,w-2,2):
                self.maze[x][y] = 2
                self.spl.append((x,y))
        # Shuffle the list of points and we can choose a random point by
        # simply "popping" it off the list.
        random.shuffle(self.spl)
        
    def makeMaze(self):
        self.mc.postToChat("look down")
        p = self.ppos
        self.mc.player.setPos(Vec3(p.x + self.mazeXSize/2, p.y + self.mazeYSize + 10, p.z +self.mazeZSize/2 ) )
        time.sleep(1)
        print "making maze"
        epos = Vec3(self.mazeXSize,self.mazeYSize, self.mazeZSize)
        clearArrea(self.mc, self.ppos, epos)
        time.sleep(2)
        self.initMaze(self.mazeXSize,self.mazeZSize)
        time.sleep(1)
        
        
        # Loop until we have no more starting points (2's in the empty maze)
        while filter(lambda x: 2 in x, self.maze):
            # Get the X and Y values of the first point in our randomized list.
            rx = self.spl[0][0]
            ry = self.spl[0][1]
            # Pop the first entry in the list, this deletes it and the rest move down.
            self.spl.pop(0)
            # Check to see if our chosen point is still a valid starting point.
            ud = False
            if self.maze[rx][ry] == 2:
                ud = True
                # Pick a random wall length up to the maximum.
                rc = rand(0, self.maxWallLen)
                # Pick a random direction.
                rd = randDir()
                fc = rd
                loop = True
                while loop:
                    # Look in each direction, if the current wall being built is stuck inside itself start again.
                    if self.maze[rx][ry-2] == 3 and self.maze[rx][ry+2] == 3 and self.maze[rx-2][ry] == 3 and self.maze[rx+2][ry] == 3:
                        #
                        # Code to clear maze area required
                        #
                        self.initMaze( self.mazeXSize, self.mazeZSize)
                        break
                    # Look ahead to see if we're okay to go in this direction.....
                    cx = rx + (rd[0]*2)
                    cy = ry + (rd[1]*2)
                    nc = self.maze[cx][cy]
                    if nc != 3:
                        for i in range(0,2):
                            i = i
                            self.maze[rx][ry] = 3
                            makeWall(self.mc, self.ppos.x+rx, self.ppos.y, self.ppos.z+ry)
                            rx += rd[0]
                            ry += rd[1]
                    # .....if not choose another direction.
                    else: rd = randDir()
                    # If we hit an existing wall break out of the loop.
                    if nc == 1: loop = False
                    # Update our wall length counter. When this hits zero pick another direction.
                    # This also makes sure the new direction isn't the same as the current one.
                    rc -= 1
                    if rc <= 0:
                        rc = rand(0, self.maxWallLen)
                        dd = rd
                        de = (fc[0]*-1,fc[1]*-1)
                        while dd == rd or rd == de:
                            rd = randDir()
            # The latest wall has been built so change all 3's (new wall) to 1's (existing wall)
            if ud:
                for x in range(0, self.mazeXSize):
                    for y in range(0, self.mazeZSize):
                        if self.maze[x][y] == 3: self.maze[x][y] = 1
        print "maze is done"
        
        
        
if __name__ == "__main__":
    import server
    mc = server.mc
    MakeMaze(mc).makeMaze()
    
    
    