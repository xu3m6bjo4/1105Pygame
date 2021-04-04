import pygame
import random


BLACK = (0,0,0)
WHILE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
ze = (50,44,79)
pygame.init()
size = (700,500)
AS = (34,56,233)
color = WHILE

screen = pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")

count = 100
circle_x = 350
circle_y = 0
rect_x = 300
rect_y = 200

circle_list = []
point = []
point.append(circle_x)
point.append(circle_y)
for i in range(0,count):
        point = []
        circle_x = random.randint(20,680)
        circle_y = random.randint(-500,0)
        point.append(circle_x)
        point.append(circle_y)
        circle_list.append(point)


done = False
clock = pygame.time.Clock()
while not done:
    screen.fill(BLACK)
    
    pygame.draw.rect(screen,AS,[rect_x,rect_y,100,100])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type ==  pygame.KEYDOWN:
            if event.key == pygame.K_a:
                rect_x = 100
                rect_y = 100
            if event.key == pygame.K_SPACE:
                
                AS = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                color = (255,255,255)
                print("K_SPACE Press")
            if event.key == pygame.K_z:
               color = (0,0,0)
                
            if event.key == pygame.K_DOWN:
                rect_y = rect_y + 5
                print("K_DOWN Prees ")
            if event.key == pygame.K_UP:
                rect_y= rect_y - 5
                print("K_UP Prees")
            if event.key == pygame.K_LEFT:
                rect_x = rect_x - 5
                print("K_LEFT Prees")
            if event.key == pygame.K_RIGHT:
                rect_x = rect_x + 5
                print("K_RIGHT Prees")
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos[0])
            print(pos[1])
            rect_x = pos[0]
            rect_y = pos[1]
            
            color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            
            
    circle_y = circle_y + 1
    if circle_y > 700:
        circle_y = 0
    for i in range(0,count):
        x = circle_list[i][0]
        y = circle_list[i][1] 
        
        y = y + 1
        circle_list[i][1] =  circle_list[i][1] + 1
        pygame.draw.circle(screen,color,(x,y),10)
        
    
        
    clock.tick(50)
    pygame.display.flip()
pygame.quit()