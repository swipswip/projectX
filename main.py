import pygame
import time

pygame.init()
screen = pygame.display.set_mode()
surf = pygame.display.get_surface()
sx = surf.get_width()
sy = surf.get_height()
jump = 70 #점프력
ga = 10 # 중력가속도
g = 0 #점프 여부 판별
jumps = 0
clock = pygame.time.Clock()


pikawidth = 300
pikaheight = 256


pika_IMG = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
pika_IMG[0] = pygame.image.load("./Asset/Sprites/Main_Character/Player/idle/player_idle_0.png")
bg_IMG = ["", "", "", "", "", ""]
cave = ["", "", "", "", "", ""]

for i in range(1, 11):
    aaa = "./Asset/Sprites/Main_Character/Player/moving/player_run_0" + str(i - 1) + ".png"
    pika_IMG[i] = pygame.image.load(aaa)
    
for i in range(11, 22):
    pika_IMG[i] = pygame.transform.flip(pika_IMG[i - 11], True, False)
    
for i in range(0, 5):
    aaa = "./Asset/Sprites/Cave_Background/bg_cave_" + str(i + 1) + ".png"
    bg_IMG[i] = pygame.image.load(aaa)
    cave[i] = bg_IMG[i].get_rect()
    cave[i].left = 0
    

pika = pika_IMG[0].get_rect()
pika.top = sy - pika.height
pika.left = sx / 2 - pika.width / 2
pis = 0
leftfocus = 1
dd = 0
pikap = 0

def moving(d):
    
    
    global leftfocus, pis, pikap
    #pika.left = pika.left + d * 10
    leftfocus = d
    pis = (pis + 1) % 11
    pikap += d
    for i in range(0, 5):
        ii = 4 - i
        cave[ii].left += -d * i * 2



while True:
    screen.fill((0, 0, 0))
    
    event = pygame.event.poll()
    pygame.key.set_repeat(1, 1)
    if event.type == pygame.QUIT:
        break
    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        moving(-1)
        dd = 11
    elif key_event[pygame.K_RIGHT]:
        moving(1)
        dd = 0
        
    if key_event[pygame.K_UP] and g < 1:
        g = 1 #중력 시스템 ON
        jumps = jump
    #if (pika.top < nya.bottom and nya.top < pika.bottom and pika.left < nya.right and nya.left < pika.right):
        #break
    
    if g > 0:
        pika.top = pika.top - jumps
        jumps = jumps - ga
        if pika.top + pika.height >= sy:
            g = 0
            pika.top = sy - pika.height
    
    
    #수정 완료
    
    for i in range(0, 5):
        ii = 4 - i
        if (sx > cave[ii].left + cave[ii].width):
            screen.blit(bg_IMG[ii], pygame.Rect(cave[ii].left + cave[ii].width, cave[ii].top, cave[ii].left + cave[ii].width + cave[ii].width, cave[ii].height))
            if (cave[ii].left + cave[ii].width <= 0):
                cave[ii].left = 0
        elif (0 <= cave[ii].left):
            screen.blit(bg_IMG[ii], pygame.Rect(cave[ii].left - cave[ii].width, cave[ii].top, cave[ii].left, cave[ii].height))
            if (cave[ii].left + cave[ii].width >= sx):
                cave[ii].left = 0 
                   
        screen.blit(bg_IMG[ii], cave[ii])
        
    screen.blit(pika_IMG[pis + dd], pika)
    
    #screen.blit(nyaon_IMG, nya)
    pygame.display.update()
    clock.tick(20)
    
pygame.quit()
