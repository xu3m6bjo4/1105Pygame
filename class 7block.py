BLACK =(0,0,0)
WHILTE = (255,255,255)
RED = (255,0,0)

import pygame
import random
class Block(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

pygame.init()
screen = pygame.display.set_mode([700,400])

all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK,20,15)
    block.rect.x = random.randrange(700)
    block.rect.y = random.randrange(400)
    all_sprites_list.add(block)
block1 = Block(RED,20,20)
block1.rect.x = 100
block1.rect.y = 100
all_sprites_list.add(block1)
play = True;
clock = pygame.time.Clock()

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    screen.fill(WHILTE)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
                          
                          

