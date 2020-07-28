from mcpi.minecraft import Minecraft 
import time
mc -= Minecraft.create()
while True:
    x,y,z - mc.player.getTilePos()
    setBlock(x,y,z,38)
    