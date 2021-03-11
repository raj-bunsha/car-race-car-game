import pygame
import math
import random
from pygame.locals import*
import os
import time

class Car(pygame.sprite.Sprite):
    truck = [pygame.image.load(os.path.join('Images', "car"+str(x) + '.png')) for x in range(1,3)]
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.time=0
        self.num=0
        self.angle=0

    def draw(self, win):
        w, h = self.truck[1].get_size()
        win.blit(blitRotate(win,self.truck[1],(self.x,self.y), (w/2,h/2),self.angle)[0],blitRotate(win,self.truck[1],(self.x,self.y), (w/2,h/2),self.angle)[1])
        

def redrawWin():
    win.fill((255,255,255))
    car.draw(win)

    pygame.display.flip()

def blitRotate(surf, image, pos, originPos, angle):

    # calcaulate the axis aligned bounding box of the rotated image
    w, h       = image.get_size()
    box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot 
    pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move   = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)

    # rotate and blit the image
    return (rotated_image, origin)
    
    # draw rectangle around the image
    # pygame.draw.rect(surf, (255, 0, 0), (*origin, *rotated_image.get_size()),2)
    pygame.display.flip()

W,H = 1500, 700
car=Car(500,500,100,100)
clock = pygame.time.Clock()
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('car game')
win.fill((0,0,0))
while True:
    keys=pygame.key.get_pressed()
    car.y-=(keys[K_UP]-keys[K_DOWN])*20*math.sin(math.pi*car.angle/180)
    car.x+=(keys[K_UP]-keys[K_DOWN])*20*math.cos(math.pi*car.angle/180)
    if keys[K_LEFT]==True:
        car.angle+=2
    if keys[K_RIGHT]==True:
        car.angle-=2

    if car.x>W:
        car.x-=W
    if car.y<0:
        car.y+=H
    if car.y>H:
        car.y-=H
    if car.x<0:
        car.x+=W
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pass  
        if event.type == pygame.QUIT: 
            run = False
            pygame.quit()
            quit()
            sys.quit()
    clock.tick(60)
    redrawWin()