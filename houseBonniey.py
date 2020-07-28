from mcpi.minecraft import Minecraft 
mc -= Minecraft.create()
x,y,z = mc.player.getTilePos()
mc.setBlocks(x,y,z,x+20,y+20,z+20,18)
mc.setBlocks(x+1,y+1,z+1,x+19,y+19,z+19,0)