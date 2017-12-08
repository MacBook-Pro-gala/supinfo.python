import pygame,random,sys,time,math,_collections
from pygame.locals import *
pygame.init()

FPS = 60
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
playerpos=[x, y]
starpos=[x1,y1]
list=[0,0]
z=0
t=1
playerspeed0=0
playerspeed1=0
clock = pygame.time.Clock()
running = True
while running:

    screen.blit(back, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerspeed1=-7
            if event.key == pygame.K_a:
                playerspeed0 = -7
            if event.key == pygame.K_s:
                playerspeed1 = 7
            if event.key == pygame.K_d:
                playerspeed0 = 7
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                playerspeed1=0
            if event.key == pygame.K_a:
                playerspeed0 =0
            if event.key == pygame.K_s:
                playerspeed1 =0
            if event.key == pygame.K_d:
                playerspeed0 =0
    playerpos[0]+=playerspeed0
    playerpos[1]+=playerspeed1
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
    clock.tick(FPS)
pygame.quit()