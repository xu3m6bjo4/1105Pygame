BLACK =(0,0,0)
WHILTE = (255,255,255)
RED = (255,0,0)
score = 0
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
block_sprites_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK,20,15)
    block.rect.x = random.randrange(700)
    block.rect.y = random.randrange(400)
    block_sprites_list.add(block)
    all_sprites_list.add(block)
player = Block(RED,20,20)
player.rect.x = 100
player.rect.y = 100
all_sprites_list.add(player)
play = True
clock = pygame.time.Clock()
font = pygame.font.Font(None,50)
font1 = pygame.font.Font(None,125)
startTime = pygame.time.get_ticks()
gametime = 0
end = False
while play:
    
    if gametime < 10:
        gametime = (pygame.time.get_ticks() - startTime) / 1000
    else:
        end = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    (m_x,m_y) = pygame.mouse.get_pos()
    player.rect.x = m_x
    player.rect.y = m_y
            
    #########################################################################
    if end == False:
        hit_list = pygame.sprite.spritecollide(player,block_sprites_list,True)
    
        for block in hit_list:
            score = score + 1
         
    ####################################################################3ˇ#####
    screen.fill(WHILTE)
    all_sprites_list.draw(screen)
    
    
    text = font.render("Score:" + str(score),True,BLACK)
    screen.blit(text,(10,10))
    time = font.render("Time:" + str(gametime),True,BLACK)
    screen.blit(time,(10,50))
    if gametime > 7 and gametime < 8 :
       # for i in range(50):
            block = Block(BLACK,20,15)
            block.rect.x = random.randrange(700)
            block.rect.y = random.randrange(400)
            block_sprites_list.add(block)
            all_sprites_list.add(block)
   
        
    if end and score <= 49 :
        game = font1.render("GAME OVER!",True,BLACK)
        screen.blit(game,(90,155))
    if score >= 50:
        win = font1.render("GOOD JUB!",True,BLACK)
        screen.blit(win,(90,155))
        text = font1.render("Score:" + str(score),True,BLACK)
        screen.blit(text,(90,255))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
                          
                          

