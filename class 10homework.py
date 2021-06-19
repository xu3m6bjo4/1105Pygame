import pygame
import random

BLACK = (0,0,0)
WHILE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
ze = (50,44,79)
rt = 100
ty = 20

class Ball(pygame.sprite.Sprite):
    def __init__(self,srx,sry,speedx,speedy,radium,color):
        self.image = pygame.Surface([radium * 2,radium * 2],pygame.SRCALPHA,32)    
        self.image = self.image.convert_alpha()
    
        pygame.draw.circle(self.image,color,(radium,radium),radium)
        
        
        self.rect = self.image.get_rect()
        self.rect.x = srx
        self.rect.y = sry
        self.dx = speedx
        self.dy = speedy
        
    def update (self):
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.dx = (-1) * self.dx
        
        if self.rect.top < 0 or self.rect.bottom > screen.get_height():
            self.dy = (-1) * self.dy        
        self.rect.x = self.rect.x + self.dx
        self.rect.y = self.rect.y + self.dy
        
    def draw(self,screen):
        screen.blit(self.image,self.rect)

class Brick(pygame.sprite.Sprite):
    def __init__(self,srx,sry,speedx,speedy,w,h,color):
        super().__init__()
        self.image = pygame.Surface([w,h],pygame.SRCALPHA,32)
        self.image = self.image.convert_alpha()
        
        pygame.draw.rect(self.image,color,[0,0,w,h])
        self.rect = self.image.get_rect()
        self.rect.x = srx
        self.rect.y = sry
        
        self.dx = speedx
        self.dy = speedy
    
    def update(self):
        self.rect.x = self.rect.x + self.dx
        self.rect.y = self.rect.y + self.dy
    def draw(self,screen):
            screen.blit(self.image,self.rect)            
        
        
pygame.init()
size = (700,500)        
screen = pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")

ball = Ball(200,200,25,25,10,BLUE)
t = random.randint(0,700)
u = random.randint(0,150)
coll = pygame.sprite.Group()
coll.add(Brick(t,u,0,0,80,40,RED))
brickGroup = pygame.sprite.Group()
for i in range(10):
    for j in range(5):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        brickGroup.add(Brick(70 * i,30 * j,0,0,70,30,(r,g,b)))
B = False    
score = 0
gameover = False
done = False
clock = pygame.time.Clock()
while not B:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                B = True
while not done:
    screen.fill(WHILE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    if ball.rect.y >= 500:
        gameover = True
    if gameover == True:
        font = pygame.font.Font(None,30)
        text = font.render("Gameover",True,BLACK)
        screen.blit(text,(300,250))
            
    (mouse_x,mouse_y) = pygame.mouse.get_pos()
    panel = Brick(300,400,0,0,rt,ty,ze)
    panel.rect.x = mouse_x
    font = pygame.font.Font(None,30)
    text = font.render("Score:" + str(score),True,BLACK)
    screen.blit(text,(400,400,))
    
    ball.update() 
    ball.draw(screen)
    brickGroup.draw(screen)
    panel.draw(screen)
    coll.draw(screen)
    gh = True
    collideList = pygame.sprite.spritecollide(ball,brickGroup,gh)
    coll1 = pygame.sprite.spritecollide(ball,coll,True)
    for collid in coll1:
        rt = rt + 10
    if len(collideList) > 0:
        #ball.dx = (-1) * ball.dx
        ball.dy = (-1) * ball.dy
    if (pygame.sprite.collide_rect(panel,ball)):
        ball.dy = (-1) * ball.dy
    for collid in collideList:
        score = score + 1
    if score == 10:
        rt = 80
    if score == 15:
        rt = 60
    if score == 20:
        coll.add(Brick(t,u,0,0,80,40,RED))
        coll.draw(screen)
        rt = 55
    if score == 35:
        rt = 25
    clock.tick(10)
    pygame.display.flip()
pygame.quit()
