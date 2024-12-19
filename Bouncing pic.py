import sys
import pygame
from pygame.locals import *

pygame.init()
# Resolution is ignored on Android
surface = pygame.display.set_mode((640, 480))

ball = pygame.image.load("pydroball.png")
'''
ball = pygame.transform.scale(ball,(300,300))

ball = pygame.transform.rotate(ball,270)
'''
ballrect = ball.get_rect()
clock = pygame.time.Clock()


width = surface.get_width()
height = surface.get_height()

speed = [6, 6]
while True:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
    
    surface.fill(Color('black'))
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    surface.blit(ball, ballrect)
    pygame.display.flip()
    clock.tick(60)