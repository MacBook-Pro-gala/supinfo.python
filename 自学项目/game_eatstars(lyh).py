import pygame,random,sys,time,math,_collections
from pygame.locals import *
pygame.init()


a=0
delay = 100
interval = 50
pygame.key.set_repeat(delay,interval)
x=320
y=240
x1=random.randint(0,640)
y1=random.randint(0,480)
screen = pygame.display.set_mode([640,480])
plane=pygame.image.load('plane.png')
planerect = plane.get_rect()
back=pygame.image.load('back.jpg')
backrect = back.get_rect()
star_big=pygame.image.load('star_big.png')
star_little=pygame.image.load('star_little.png')
playerpos=[x,y]
starpos=[x1,y1]
list=[0,0]
z=0
t=1
o=1
running = True
while running:

    screen.blit(back, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pygame.key.get_pressed()[pygame.K_w]==0:
                playerpos[1]=playerpos[1]
        else:
                playerpos[1]-=7
        if pygame.key.get_pressed()[pygame.K_a]==0:
                playerpos[0]=playerpos[0]
        else:
                playerpos[0]-=7
        if pygame.key.get_pressed()[pygame.K_s]==0:
                playerpos[1]=playerpos[1]
        else:
                playerpos[1]+=7
        if pygame.key.get_pressed()[pygame.K_d]==0:
                playerpos[0]= playerpos[0]
        else:
                playerpos[0]+=7

    screen.blit(plane, playerpos)
    screen.blit(star_little,(30,20))
    fontObj = pygame.font.SysFont('arial', 48)
    texteSurface = fontObj.render(str(z), False, (0, 0, 0))
    screen.blit(texteSurface, (10, 10))
    if x1-30<playerpos[0]<x1+30 and y1-30<playerpos[1]<y1+30:
        x1 = random.randint(0, 540)
        y1 = random.randint(0, 380)
        starpos = [x1, y1]
        z=z+1
    if list[0] == 0:
        screen.blit(star_big,starpos)

    pygame.display.update(planerect)
    pygame.display.update(backrect)
pygame.quit()

#