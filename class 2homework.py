import pygame
from math import pi
WHILE = (255,255,255)
ZE = (255,220,220)
BLACK = (0,0,0)
pygame.init()
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")
done = False
clock = pygame.time.Clock()
while not done:
    screen.fill(WHILE)
    pygame.draw.rect
    pygame.draw.polygon
    pygame.draw.circle(screen,ZE,(350,200),200)
    pygame.draw.circle(screen,BLACK,(250,100),25)
    pygame.draw.circle(screen,BLACK,(450,100),25)
    pygame.draw.arc(screen,BLACK,(300,200,100,100),pi,pi*2)
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(10)
    pygame.display.flip()
pygame.quit()