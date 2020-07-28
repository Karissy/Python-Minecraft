from mcpi.minecraft import Minecraft
mc = Minecraft.create()
name = input("message?")
mc.postToChat("["+name+"]"+message)