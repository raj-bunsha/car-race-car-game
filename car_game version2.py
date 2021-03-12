import pygame
import math
import random
from pygame.locals import*
import os
import time

class Car(pygame.sprite.Sprite):
    truck = [pygame.image.load(os.path.join('Images', "car"+str(x) + '.png')) for x in range(1,4)]
    truck[1]=pygame.transform.scale(truck[2], (78,45))
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
        l=math.sqrt(w*w+h*h)/2
        self.angle*=-math.pi/180
        x1 = self.x + w/2 * math.cos(self.angle) + h/2 *math.sin(self.angle)
        y1 = self.y + w/2 * math.sin(self.angle) - h/2 *math.cos(self.angle)
        x2 = self.x + w/2 * math.cos(self.angle) - h/2 *math.sin(self.angle)
        y2 = self.y + w/2 * math.sin(self.angle) + h/2 *math.cos(self.angle)
        x3 = self.x - w/2 * math.cos(self.angle) + h/2 *math.sin(self.angle)
        y3 = self.y - w/2 * math.sin(self.angle) - h/2 *math.cos(self.angle)
        x4 = self.x - w/2 * math.cos(self.angle) - h/2 *math.sin(self.angle)
        y4 = self.y - w/2 * math.sin(self.angle) + h/2 *math.cos(self.angle)
        self.angle*=-180/math.pi

        circle_x_y1 = (x1,y1)
        circle_x_y2 = (x2,y2)
        circle_x_y3 = (x3,y3)
        circle_x_y4 = (x4,y4)
        if x1>W:
            x1-=W
        if x2>W:
            x2-=W
        if x3>W:
            x3-=W
        if x4>W:
            x4-=W
        if x1<0:
            x1+=W
        if x2<0:
            x2+=W
        if x3<0:
            x3+=W
        if x4<0:
            x4+=W
        if y1>H:
            y1-=H
        if y2>H:
            y2-=H
        if y3>H:
            y3-=H
        if y4>H:
            y4-=H
        if y1<0:
            y1+=H
        if y2<0:
            y2+=H
        if y3<0:
            y3+=H
        if y4<0:
            y4+=H
        circle_radius = 5
        border_width = 0 #0 = filled circle
        colour1 = (59, 76, 62)
        colour2 = (59, 76, 62)
        colour3 = (59, 76, 62)
        colour4 = (59, 76, 62)
        if str(win.get_at((int(x1),int(y1))))==str((59, 76, 62, 255)) :
            colour1 = (81, 207, 104)
        if str(win.get_at((int(x1),int(y1))))==str((81, 207, 104, 255)) :
            colour1 = (59, 76, 62)
        if str(win.get_at((int(x2),int(y2))))==str((59, 76, 62, 255)):
            colour2 = (81, 207, 104)
        if str(win.get_at((int(x2),int(y2))))==str((81, 207, 104, 255)) :
            colour2 = (59, 76, 62)
        if str(win.get_at((int(x3),int(y3))))==str((59, 76, 62, 255)) :
            colour3 = (81, 207, 104)
        if str(win.get_at((int(x3),int(y3))))==str((81, 207, 104, 255)) :
            colour3 = (59, 76, 62)
        if str(win.get_at((int(x4),int(y4))))==str((59, 76, 62, 255)):
            colour4 = (81, 207, 104)
        if str(win.get_at((int(x4),int(y4))))==str((81, 207, 104, 255)) :
            colour4 = (59, 76, 62)
        pygame.draw.circle(win, colour1, circle_x_y1, circle_radius, border_width)
        pygame.draw.circle(win, colour2, circle_x_y2, circle_radius, border_width)
        pygame.draw.circle(win, colour3, circle_x_y3, circle_radius, border_width)
        pygame.draw.circle(win, colour4, circle_x_y4, circle_radius, border_width)

        #print(win.get_at((int(self.x+w/2+1),int(self.y+h/2+1))))
        win.blit(blitRotate(win,self.truck[1],(self.x,self.y), (w/2,h/2),self.angle)[0],blitRotate(win,self.truck[1],(self.x,self.y), (w/2,h/2),self.angle)[1])
        
        # for i in range(2*w):
        #     win.set_at((int(self.x),int(self.y+i)), (255,0,0,100))
        #surface.get_at(posx,posy) is useed to get the color of the point on surface in pygame
        

def redrawWin():
    win.blit(bg,(0,0))
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
    #pygame.draw.rect(surf, (255, 0, 0), (*origin, *rotated_image.get_size()),2)

    # rotate and blit the image
    return (rotated_image, origin)
    
    # draw rectangle around the image
    

W,H = 1500, 700
car=Car(500,500,100,100)
clock = pygame.time.Clock()
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('car game')
bg = pygame.image.load("Images/background.png")
win.blit(bg,(0,0))
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