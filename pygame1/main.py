import pygame, sys
from pygame.locals import *

#some define
FPS = 30
y = 400
x= 500
SIZE = 110
big_star1 = (50, 50)
big_star2 = (400, 200)
displayed = list()
displayed.append(1)
displayed.append(1)
star_number = 0

pygame.init();
clock = pygame.time.Clock()
surface = pygame.display.set_mode((640, 480))
font = pygame.font.SysFont("'Comic Sans MS'", 32)

pygame.display.set_caption("Hello Supinfo !!!")

back = pygame.image.load("back.jpg")
plane = pygame.image.load("plane.png")
big = pygame.image.load("star_big.png")
small = pygame.image.load("star_little.png")

while True:
    text = font.render(str(star_number), False, (0,0,0))

    surface.blit(back, (0, 0))
    surface.blit(plane, (x, y))
    surface.blit(text, (0,0))
    surface.blit(small, (30, 8))
    if displayed[0] == 1:
        surface.blit(big, big_star1)
    if displayed[1] == 1:
        surface.blit(big, big_star2)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                y -= 5
            if event.key == K_DOWN:
                y += 5
            if event.key == K_LEFT:
                x -= 5
            if event.key == K_RIGHT:
                x += 5
    print("X = ",x, " Y = ", y)
    if (y <= big_star2[1]+110 and y >= big_star2[1]) and (x <= big_star2[0]+110 and x >= big_star2[0]) and displayed[1] == 1:
        displayed[1] = 0
        star_number += 1
    if (y <= big_star1[1]+110 and y >= big_star1[1]) and (x <= big_star1[0]+110 and x >= big_star1[0]) and displayed[0] == 1:
        displayed[0] = 0
        star_number += 1
    pygame.display.update()
    clock.tick(FPS)
