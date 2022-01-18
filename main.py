import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()

pikasize = 305;
pika_IMG = pygame.image.load("pikapika.png")
nyaon_IMG = pygame.image.load("nya.png")
pika = pika_IMG.get_rect()
nya = nyaon_IMG.get_rect()
pika.centerx = 500
pika.centery = 500
nya.centerx = 800
nya.centery = 800
while True:
    screen.fill((0, 0, 0))
    
    event = pygame.event.poll()
    pygame.key.set_repeat(1, 1)
    if event.type == pygame.QUIT:
        break
    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        pika.left -= 5
    elif key_event[pygame.K_RIGHT]:
        pika.left += 5
    elif key_event[pygame.K_UP]:
        pika.top -= 5
    elif key_event[pygame.K_DOWN]:
        pika.top += 5
    
    #수정 완료
    screen.blit(pika_IMG, pika)
    screen.blit(nyaon_IMG, nya)
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()
