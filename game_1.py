import pygame
import random
import math
from pygame import mixer 

pygame.init()
disp = pygame.display.set_mode((800,600))
bullet = mixer.Sound(r'C:\Users\91708\Desktop\Alien Attack python\bullet.wav') 
collision = mixer.Sound(r'C:\Users\91708\Desktop\Alien Attack python\collision.wav')


bg = pygame.image.load(r"C:\Users\91708\Desktop\Alien Attack python\2.jpg")
mixer.music.load(r'C:\Users\91708\Desktop\Alien Attack python\background.mp3')
mixer.music.play(-1)


img_1 = pygame.image.load(r"C:\Users\91708\Desktop\Alien Attack python\s_1.png") 
px = 20
py = 480
px_change = 0
py_change = 0



img_2 = []
ex = []
ey = []
ey_change = []
for i in range(0,5):
    img_2.append(pygame.image.load(r"C:\Users\91708\Desktop\Alien Attack python\alien.png"))
    ex.append(random.randint(50,750))
    ey.append(random.randint(20,100))
    ey_change.append(0.5)
    
    ##print(ex,ey) printing array index value of ex and ey
    ##ex_change = 5  not used as our enemy will only fall on y axis direction and not x axis

img_3 = pygame.image.load(r"C:\Users\91708\Desktop\Alien Attack python\bullet.png")
bx=0
by=480
by_change = 0
state = 0

score_val = 0
score_font = pygame.font.SysFont("comicsansms", 35)

game_over_font = pygame.font.SysFont("comicsansms", 70)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            px_change = -7
            py_change = 0
        
        elif event.key == pygame.K_RIGHT:
            px_change = 7
            py_change = 0
            
        elif event.key == pygame.K_SPACE:
            if state == 0:
                bullet.play()
                bx = px
                state = 1
                by_change = -15
            
            
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            px_change = 0
            py_change = 0
    px = px + px_change
    
    by = by + by_change

    if px > 736:
        px = 736
    if px < 0 :
        px =0
        
    disp.fill((0,0,0))
    disp.blit(bg,(0,0))
    if state == 1 :
        disp.blit(img_3,(bx,by))
        if by <= 0:
            by = 480
            state = 0
            
    
    for i in range(0,5):
        if (ey[i]>=480):
            over = game_over_font.render("GAME OVER",True,(145,0,145))
            disp.blit(over,(200,200))
            for j in range(0,5):
                ey[j] = 2000

        x_dist = (bx-ex[i])**2
        y_dist = (by -ey[i])**2
        dist = math.sqrt(x_dist + y_dist)
        if (dist<30):
            collision.play()
            ex[i] = random.randint(50,750)
            ey[i] = random.randint(20,100)
            score_val = score_val + 1
           
        ey[i] = ey[i] + ey_change[i]
        score = score_font.render("SCORE : "+str(score_val),True,(0,255,0))
        disp.blit(score,(10,10))
        disp.blit(img_2[i],(ex[i],ey[i]))
    disp.blit(img_1,(px,py))
    pygame.display.flip()
        
pygame.quit()