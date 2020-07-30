from mcpi.minecraft import Minecraft
import time 
mc = Minecraft.create()
while True:
    mc.executeCommand("time add 50")
    time.sleep(10)