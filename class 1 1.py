import pygame

BLACK = (0,0,0)
WHILE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
QQ = (77,44,0)
pygame.init()
size = (700,500)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")
done = False
while not done:
    screen.fill(RED)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
pygame.quit()