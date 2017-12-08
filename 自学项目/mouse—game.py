import pygame,random,sys,time,math,_collections
from pygame.locals import *
pygame.init()
xspeed=0
yspeed=0
screen = pygame.display.set_mode([640,480])
back=pygame.image.load('back.jpg')
plane=pygame.image.load('plane.png')
x=320
y=240
playerpos=[x,y]
position=playerpos
fpsClock = pygame.time.Clock()
while True:
    screen.blit(back, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button ==1:
                position = pygame.mouse.get_pos()
    if playerpos[0]in range(position[0]-10,position[0]+10) and playerpos[1]in range(position[1]-10,position[1]+10):
        screen.blit(plane, playerpos)
        pygame.display.update()
    else:
        if position[0]>playerpos[0]:
            xspeed=10
        else:
            xspeed=-10
        if position[1]>playerpos[1]:
            yspeed=10
        else:
            yspeed=-10
        playerpos[0]+=xspeed
        playerpos[1]+=yspeed
        screen.blit(plane, playerpos)
        pygame.display.update()
        fpsClock.tick(60)
    ##########