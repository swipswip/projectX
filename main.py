import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1400))
clock = pygame.time.Clock()

pika = pygame.image.load('pikapika.png')

while True:
    screen.fill((0, 0, 0))
    
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    
    screen.blit(pika, (0, 0))
    
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()
