'''
Created on Oct 6, 2013

@author: Otrebor45
'''
from random import randint as rand
from mcpi.vec3 import Vec3 as Vec3
import mcpi.block as block
            
def runSort(mc,pos,size):
    #make random array
    array = blockArray(mc,pos,size)
    for i in range(0,size):
        array[i] = rand(0,15)
        #time.sleep(.1)
    #time.sleep(.1)
    sortItems(mc, array)
    
def sortItems(mc, array):
    pos = array.spos
    hpos = Vec3(pos.x + 4, pos.y, pos.z)
    size = array.size
    heap = minHeap(mc,hpos,size)
    for i in range(0,size):
        heap.insert( array.remove(i))
    for i in range(0,size):
        array[i] = heap.pop()
        
class minHeap:
    def __init__(self,mc,pos,size):
        self.data = blockArray(mc,pos,size)
        self.count = 0
        
    def swap(self,i1,i2):
        d1 = self.data[i1]
        d2 = self.data[i2]
        self.data[i1] = d2
        self.data[i2] = d1
    
    def parent(self,index):
        return (index-1)/2
    
    def childL(self,index):
        return 2*index+1
    
    def childR(self,index):
        return 2*index +2;
        
    def smalChild(self,index):
        li = self.childL(index)
        ri = self.childR(index)
        if self.count <= li:
            return index;
        if self.count <= ri:
            return li;

        if self.data[li] > self.data[ri]:
            return ri
        else:
            return li
        
    def parentData(self,index):
        return self.data[self.parent(index)]
    
    def insert(self,data):
        if self.count >= self.data.size:
            return False
        index = self.count
        self.data[index] = data
        self.count += 1
        while self.parentData(index) > self.data[index]:
            self.swap(index, self.parent(index))
            index = self.parent(index)
        return True
    
    def pop(self):
        out = self.data[0]
        #last = self.count-1
        self.count -= 1
        if self.count >= 0:
            temp = self.data[self.count]
            self.data[0] = temp
            index = 0
            child = self.smalChild(index)
            while self.data[index] > self.data[child]:
                self.swap(index,child)
                index = child
                child = self.smalChild(index)
        self.data.remove(self.count)
        return out
        
    def empty(self):
        return self.count == 0
    

class blockArray:
    
    def indexToPos(self,index):
        return Vec3(self.spos.x, self.spos.y, self.spos.z+index)
    
    def initArray(self):
        for x in range(0,self.size):
            pos = self.indexToPos(x)
            self.mc.setBlock(pos.x,pos.y,pos.z,block.AIR)
                
    def __init__(self,mc,pos,size):
        self.spos = pos
        self.size = size
        self.mc = mc
        self.initArray()
        
    def __getitem__(self,index):
        pos1 = self.indexToPos(index)
        b = self.mc.getBlockWithData(pos1.x, pos1.y, pos1.z)
        return b.data
    
    def __setitem__(self,index,value):
        pos1 = self.indexToPos(index)
        if value == -1:
            self.mc.setBlock(pos1.x, pos1.y, pos1.z, block.AIR)
        else:
            self.mc.setBlock(pos1.x, pos1.y, pos1.z, block.WOOL.id, value)
          
    def remove(self,index):
        pos = self.indexToPos(index)
        d = self[index]
        self.mc.setBlock(pos.x, pos.y, pos.z, block.AIR)
        return d
        
        
        
if __name__ == "__main__":
    import server
    mc = server.mc
    pos = mc.player.getPos()
    pos.y += 5
    runSort(mc,pos,50)