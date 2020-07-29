from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

for i in range(10):
    mc.setBlocks(x+i,y-i,z+i,x-i,y-i,z-i,20)