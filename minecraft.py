import mcpi.minecraft as minecraft
from mcpi import block
import time
import random

mc = minecraft.Minecraft.create()
basex,basey,basez = 0,0,0

def start():
    clear_area()
    mc.player.setPos(basex,75,basez)
    
    for x in range(32):
        for z in range(8):
            offsetx,offsetz = x * random.randint(11,13), basez + z * random.randint(11,13)
            site_blocks = []
            
            for val in range(offsetx-2,offsetx+10):
                for aval in range(offsetz-2,offsetz+10):
                    site_blocks.append((val,aval))
                                
            if all(map(lambda w: mc.getBlock(w[0],1,w[1]) == 0,site_blocks)):
                 build_house(basex + offsetx, basey, basez + offsetz)
    
    # block_choice()
    
def block_choice():
    for x in range(500):
        mc.setBlock(x,20,0,x)

def build_house(basex,basey,basez):
    site_empty = True
    n_floors = random.randint(1,5)
    
    for floor in range(n_floors):
        basey = floor * 5
        
        mc.setBlocks(basex,basey-1,basez,basex+7,basey-1,basez+7,5)
        if not floor == 0: mc.setBlocks(basex+3,basey-1,basez+3,basex+4,basey-1,basez+4,0)
        
        walls = ['b','b','b','b']
        
        if floor == 0: walls[random.randint(0,3)] = 'd'
        for i in range(1,4):
            if random.randint(0,1) and walls[i] == 'b': walls[i] = 'w'
    
        build_wall(basex,basey,basez,walls[0],'x')
        build_wall(basex,basey,basez+7,walls[1],'x')
        build_wall(basex,basey,basez,walls[2],'z')
        build_wall(basex+7,basey,basez,walls[3],'z')
        
    basey = (n_floors * 5) - 1
    mc.setBlocks(basex-1,basey,basez-1,basex+8,basey,basez+8,4)
    mc.setBlocks(basex,basey+1,basez,basex+7,basey+1,basez+7,4)
    mc.setBlocks(basex+1,basey+2,basez+1,basex+6,basey+2,basez+6,4)
    mc.setBlocks(basex+2,basey+3,basez+2,basex+5,basey+3,basez+5,4)


def clear_area():
    area_r = 400
    mc.setBlocks(-area_r,-1,-area_r,area_r,0,area_r,2)
    mc.setBlocks(-area_r,0,-area_r,area_r,100,area_r,0)

def build_wall(basex,basey,basez,w_type,dirn):
    if dirn == 'x':
        for x in range(8):
            for y in range(4):
                mc.setBlock(basex+x,basey+y,basez,5 if x not in [0,7] else 17)                
    elif dirn == 'z':
        for z in range(8):
            for y in range(4):
                mc.setBlock(basex,basey+y,basez+z,5 if z not in [0,7] else 17)                
    if w_type == 'd':
        if dirn == 'x':
            mc.setBlock(basex+3,basey,  basez,0)
            mc.setBlock(basex+3,basey+1,basez,0)
            mc.setBlock(basex+4,basey,  basez,0)
            mc.setBlock(basex+4,basey+1,basez,0)
        elif dirn == 'z':
            mc.setBlock(basex,basey,  basez+3,0)
            mc.setBlock(basex,basey+1,basez+3,0)
            mc.setBlock(basex,basey,  basez+4,0)
            mc.setBlock(basex,basey+1,basez+4,0)
            
    elif w_type == 'w':
        if dirn == 'x':
            mc.setBlock(basex+2,basey+2,basez,20)
            mc.setBlock(basex+2,basey+1,basez,20)
            mc.setBlock(basex+3,basey+2,basez,20)
            mc.setBlock(basex+3,basey+1,basez,20)
            mc.setBlock(basex+4,basey+2,basez,20)
            mc.setBlock(basex+4,basey+1,basez,20)
            mc.setBlock(basex+5,basey+2,basez,20)
            mc.setBlock(basex+5,basey+1,basez,20)
        elif dirn == 'z':
            mc.setBlock(basex,basey+2,basez+2,20)
            mc.setBlock(basex,basey+1,basez+2,20)
            mc.setBlock(basex,basey+2,basez+3,20)
            mc.setBlock(basex,basey+1,basez+3,20)
            mc.setBlock(basex,basey+2,basez+4,20)
            mc.setBlock(basex,basey+1,basez+4,20)
            mc.setBlock(basex,basey+2,basez+5,20)
            mc.setBlock(basex,basey+1,basez+5,20)
        
start()


