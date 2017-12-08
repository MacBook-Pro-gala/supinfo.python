import pygame,random,sys,time,math
from pygame.locals import *
pygame.init()
#
#
x3=600
y3=random.randint(60,400)
x2=0
y2=0
acc=[0,0]
arrows=[]
x=y=100
pygame.init()
delay = 100
interval = 50
pygame.key.set_repeat(delay,interval)
weight=640
height=480
screen = pygame.display.set_mode([640,480])
playerpos=[x,y]
airplane=pygame.image.load('airplane.jpg').convert_alpha()
arrow=pygame.image.load('attack.png').convert_alpha()
arrow=pygame.transform.smoothscale(arrow,(40,40))#缩放图片
background=pygame.image.load('background.jpg').convert_alpha()
background2=pygame.image.load('background.jpg').convert_alpha()
airplane2=pygame.image.load('airplane2.jpg').convert_alpha()
ennemi=pygame.image.load('ennemi.jpg').convert_alpha()
pygame.display.set_caption('星球大战')
clock = pygame.time.Clock()
#
enneminumber = USEREVENT + 1
pygame.time.set_timer(enneminumber, 1000)
#
running = True
while running:
#
#
#
    screen.blit(background,(x2,y2))
    screen.blit(background2,(x2+640, y2))
    x2=x2-1
    if x2<-640:
        x2=0
#
#
#
#
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerpos[1]-=7



            elif event.key == pygame.K_a:
                playerpos[0] -= 7

            elif event.key == pygame.K_s:
                playerpos[1] += 7


            elif event.key == pygame.K_d:
                playerpos[0] += 7
#
#
#
            elif event.key == pygame.K_w and event.key == pygame.K_a:
                playerpos[1] -= 3.5
                playerpos[0] -= 3.5
            elif event.key == pygame.K_w and event.key == pygame.K_d:
                playerpos[1] -= 3.5
                playerpos[0] += 3.5
            elif event.key == pygame.K_s and event.key == pygame.K_a:
                playerpos[1] += 3.5
                playerpos[0] -= 3.5
            elif event.key == pygame.K_s and event.key == pygame.K_d:
                playerpos[1] += 3.5
                playerpos[0] += 3.5
        elif event.type == enneminumber:
            screen.blit(ennemi, (x3, y3))
#
#
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            acc[1] += 1
            arrows.append(
                [math.atan2(position[1] - (playerpos1[1] + 13), position[0] - (playerpos1[0] + 13)), playerpos1[0] + 16,
                 playerpos1[1] + 13])
#
#
#
    for bullet in arrows:
        index = 0
        velx = math.cos(bullet[0]) * 0.5
        vely = math.sin(bullet[0]) * 0.5
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
            arrows.pop(index)
        else:
            index += 1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360 - projectile[0] * 57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))
#
#
#
#
#
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1] - (playerpos[1] + 32), position[0] - (playerpos[0] + 26))
    playerrot = pygame.transform.rotate(airplane, 360 - angle * 57.29)#使图片旋转
    playerpos1 = (playerpos[0] - playerrot.get_rect().width / 2, playerpos[1] - playerrot.get_rect().height / 2)
    screen.blit(playerrot, playerpos1)
#


    time_passed = clock.tick()
    time_passed_seconds=time_passed/1000.0
    distance_moved = time_passed_seconds*25
    y3=y3-distance_moved
    x3=x3-distance_moved
#
#
    pygame.display.update()
