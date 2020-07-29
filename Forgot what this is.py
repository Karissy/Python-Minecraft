from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
while True:
    hits = mc.events.pollBlockHits()
    if len(hits)>0:
        hit = hits[0]
        x,y,z = hit.pos.x,hit.pos.y, hit.pos.z
        blockID = getBlock()
        print ("Congratulations! You found the block which ID is " +str(blockID) "!!")
        mc.postToChat("Congratulations! You found the block with the ID" +str(blockID)"!!")