from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
while True:
    hits = mc.events.pollBlockHits()
    if len(hits)>0:
        hit = hits[0]
        x,y,z = hit.pos.x,hit.pos.y, hit.pos.z
        #blockID = getBlock()
        mc.setBlock(x,y,z,46)