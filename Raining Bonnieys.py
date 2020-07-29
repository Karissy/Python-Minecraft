from mcpi.minecraft import Minecraft
import time, random
mc = Minecraft.create()
pos = mc.player.getTilePos()
while True:
   x = pos.x + random.uniform(-20,20)
   y = pos.y + 30
   z = pos.z + random.uniform(-20,20)
   mc.spawnEntity(x,y,z,105)
   time.sleep(0.1)
   