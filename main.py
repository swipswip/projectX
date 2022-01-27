import pygame

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

pika_IMG = pygame.image.load("Asset\Sprites\Main_Character\player\idle\player_idle_0.png")
nyaon_IMG = pygame.image.load("nya.png")

pika = pika_IMG.get_rect()
nya = nyaon_IMG.get_rect()
pika.top = sy - pika.height
pika.left = 0
nya.centerx = 900
nya.centery = 900
while True:
    screen.fill((0, 0, 0))
    
    event = pygame.event.poll()
    pygame.key.set_repeat(1, 1)
    if event.type == pygame.QUIT:
        break
    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        pika.left -= 10
    if key_event[pygame.K_RIGHT]:
        pika.left += 10
    if key_event[pygame.K_UP] and g < 1:
        g = 1 #중력 시스템 ON
        jumps = jump
        
    if (pika.top < nya.bottom and nya.top < pika.bottom and pika.left < nya.right and nya.left < pika.right):
        break
    
    if g > 0:
        pika.top = pika.top - jumps
        jumps = jumps - ga
        if pika.top + pika.height >= sy:
            g = 0
            pika.top = sy - pika.height
    
    
    #수정 완료
    screen.blit(pika_IMG, pika)
    screen.blit(nyaon_IMG, nya)
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()
