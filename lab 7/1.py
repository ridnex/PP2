import pygame
import datetime
import math
pygame.init()


WHITE = (255, 255, 255)
l = 1500
w = 1020

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
    surf.blit(rotated_image, origin)

    # draw rectangle around the image
    #pygame.draw.rect (surf, (255, 0, 0), (*origin, *rotated_image.get_size()),2)

screen = pygame.display.set_mode((l, w))
image = pygame.image.load('mickeyclock.jpeg')
image1 =  pygame.image.load('right.png')
image2 = pygame.image.load('lefth.png')
clock = pygame.time.Clock()
running = True

while running:
    now = datetime.datetime.now()
    m = int(now.strftime("%M"))
    s = int(now.strftime("%S"))
    print(s)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)

    screen.blit(image,(0,0))
    
   
    blitRotate(screen,image2,(690,500),(0,0),145-6*s)
    blitRotate(screen, image1,(690,500), (0,0), 128-6*m)
  

    
    pygame.display.flip()
    clock.tick(1)
