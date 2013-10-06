#!/usr/bin/env python

# mcpipy.com retrieved from URL below, written by zhuowei
# http://www.minecraftforum.net/topic/1639215-danfrisk-asks-for-physical-reality-does-opening-a-cdrom-from-minecraft-count/

#import subprocess
import time


#ip address of Pi

#ipAddr = "127.0.0.1"
def ejectcd(mc):
    while True:
        hits = mc.events.pollBlockHits()
        if len(hits) > 0:
            mc.postToChat("you have hit: "+len(hits))
        time.sleep(0.1)