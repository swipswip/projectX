import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()

pikasize = 305;
pika_IMG = pygame.image.load("pikapika.png")
pika = pika_IMG.get_rect()
pika.centerx = 500
pika.centery = 500

while True:
    screen.fill((0, 0, 0))
    
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            pika.left -= 5
        elif event.key == pygame.K_RIGHT:
            pika.left += 5
        elif event.key == pygame.K_UP:
            pika.top -= 5
        elif event.key == pygame.K_DOWN:
            pika.top += 5
    
    #수정 완료
    screen.blit(pika_IMG, pika)
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()
