import pygame
import time
import sys
import random


pygame.init()
screen = pygame.display.set_mode()
surf = pygame.display.get_surface()
sx = surf.get_width()
sy = surf.get_height()
jump = 70 #점프력
ga = 10 # 중력가속도
g = 0 #점프 여부 판별
jumps = 0
bn = 0 #블록 시작 위치
clock = pygame.time.Clock()


pikawidth = 300
pikaheight = 256


pika_IMG = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
pika_IMG[0] = pygame.image.load("./Asset/Sprites/Main_Character/Player/idle/player_idle_0.png")
rndblock_IMG = ["" for i in range(129)]
for i in range(1, 10):
    rndblock_IMG[i] = pygame.image.load("./Tileset/Tileset2/Tileset2_0" + str(i) + ".png")
    rndblock_IMG[i] = pygame.transform.scale(rndblock_IMG[i], (64,64)) ##원본은 256*256 .png
    
for i in range(10, 128):
    rndblock_IMG[i] = pygame.image.load("./Tileset/Tileset2/Tileset2_" + str(i) + ".png")
    rndblock_IMG[i] = pygame.transform.scale(rndblock_IMG[i], (64,64))
        
rndblock = rndblock_IMG[1].get_rect()
##tileset2_01, 02, 03 이런식으로 파일명 되어있어서 나눠놓음


for i in range(1, 11):
    aaa = "./Asset/Sprites/Main_Character/Player/moving/player_run_0" + str(i - 1) + ".png"
    pika_IMG[i] = pygame.image.load(aaa)
    
for i in range(11, 22):
    pika_IMG[i] = pygame.transform.flip(pika_IMG[i - 11], True, False)
    
bg_IMG = pygame.image.load("./asset\Sprites/needs/cave_bg.png")
bg_IMG = pygame.transform.scale(bg_IMG, (sx, sy))
cave = bg_IMG.get_rect()
cave.left = 0


    
block_IMG = pygame.image.load("./Asset/Sprites/Tileset/stonefloor.png")
block = block_IMG.get_rect()
bc = int(sx / block.width + 1) #해상도에 따라 필요한 바닥의 갯수 결정

pika = pika_IMG[0].get_rect()
pika.top = sy - pika.height
pika.left = 250
pis = 0
leftfocus = 1
dd = 0
pikap = 0
t = 0
blockpos = 0
blocknum = 1


def moving(d):
    global leftfocus, pis, pikap, bn
    #pika.left = pika.left + d * 10
    leftfocus = d
    pis = (pis + 1) % 11
    pikap += d
    bn += -d * 12
    if bn <= -(block.width):
        bn += block.width
    elif bn >= block.width:
        bn -= block.width
        
        
        

def printscreen():
                   
    screen.blit(bg_IMG, cave)
        
    screen.blit(pika_IMG[pis + dd], pika)
    
def blockmove():
    global bn
    bs = bn - block.width
    bf = bn
    for i in range(0, bc + 2):
        screen.blit(block_IMG, pygame.Rect(bs, sy - block.height / 3, bf, block.height))
        bs = bs + block.width
        bf = bf + block.width


def blockengage():
    global t, blockpos, blocknum
    t = (t + 1) % 200
    if t == 0:
        blockpos = random.randrange(1, sy)
        blocknum = random.randrange(1, 128)

while True:
    screen.fill((0, 0, 0))
    
    event = pygame.event.poll()
    pygame.key.set_repeat(1, 1)
    if event.type == pygame.QUIT:
        break
    key_event = pygame.key.get_pressed()

    moving(1)
    if key_event[pygame.K_ESCAPE]:
        sys.exit()
    if key_event[pygame.K_UP] and g < 1:
        g = 1 #중력 시스템 ON
        jumps = jump
        
    
    if g > 0:
        pika.top = pika.top - jumps
        jumps = jumps - ga
        if pika.top + pika.height >= sy:
            g = 0
            pika.top = sy - pika.height
    
    
    #수정 완료
    blockengage()
    printscreen()
    blockmove()
    
    screen.blit(rndblock_IMG[blocknum], pygame.Rect(sx-rndblock.width, blockpos, sx, blockpos + rndblock.height))
    #screen.blit(nyaon_IMG, nya)
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
