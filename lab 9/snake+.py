import pygame
import random
pygame.init()

#color
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
YELLOW =(255, 191, 0)

#clock
clock = pygame.time.Clock()
FPS = 10
time_for_big_food = 10*FPS+1  # my time it is just cnt by FPS  10*FPS=10s

#screen
l, w = 1001, 601
screen = pygame.display.set_mode((l,w))
running = True
dx, dy = 0, 0
radius = 10
body = [[10, 10]]
wall = []
condition_kill = False
last_key = str("")

#value
level_value = 1
score_value = 0
#text
font = pygame.font.SysFont("comicsansms", 24)
font_Gameover = pygame.font.SysFont("comicsansms", 72)
text4 = font.render("GAME OVER", True, BLACK)


#random cordinate  
def rondom_c():
    value_x = random.randrange(10, l-10)
    value_y = random.randrange(10, w-10)
    x1, y1 = 10 * round(value_x / 10), 10 * round(value_y /10)
    condition = True
    for i in range(len(body)):
        if body[i][0]==x1 and body[i][1] == y1:
            condition = False
            break
    if level_value == 1:
        for i in range(100,400):
            if x1 == 300 and y1 == i:
                condition = False
                break
    if condition == True:
        return x1, y1
    else:
        x1, y1 = rondom_c()
        return x1, y1

food_x, food_y = rondom_c()
BIG_FOOD_X, BIG_FOOD_Y = rondom_c()

def kill_yourself():
    global condition_kill
    for i in range(len(body)):
        if i!= 0:
            if body[0][0] == body[i][0] and body[0][1] == body[i][1]:
                condition_kill = True
                break
    return condition_kill

def kill_wall_line():
    global condition_kill
    for i in range(100,400):
        if body[0][0] == 300 and body[0][1] == i:
            condition_kill = True
            break
    return condition_kill

def kill_wall():  
    global condition_kill
    for i in range(len(wall)):
        if body[0][0] == wall[i][0] and body[0][1] == wall[i][1]:
            condition_kill = True
            break

    return condition_kill

def GAME_OVER():
    global running
    screen.fill(RED)
    screen.blit(text1, (850,5))
    screen.blit(text2, (850,35))
    screen.blit(text3, (850,65))
    screen.blit(text4, (425,225))

#main
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                body.append([0, 0])
            if event.key == pygame.K_RIGHT and last_key!="K_LEFT":
                dx = 10
                dy = 0
                last_key = "K_RIGHT"

            if event.key == pygame.K_LEFT and last_key!="K_RIGHT":
                dx = -10
                dy = 0
                last_key = "K_LEFT"

            if event.key == pygame.K_UP and last_key!="K_DOWN":
                dx = 0
                dy = -10
                last_key = "K_UP"

            if event.key == pygame.K_DOWN and last_key!="K_UP":
                dx = 0
                dy = 10
                last_key = "K_DOWN"
    #value 
    text1 = font.render("Score: "+str(score_value), True, WHITE)
    text2 = font.render("Level: "+str(level_value), True, WHITE)
    text3 = font.render("FPS: "+str(FPS), True, WHITE)


    #eating
    if body[0][0]==food_x and body[0][1]==food_y:
        food_x, food_y = rondom_c()
        body.append([0, 0])
        score_value += 10
        time_for_big_food = 10*FPS +1

    
    #eating BIF FOOD
    elif body[0][0]==BIG_FOOD_X and body[0][1]== BIG_FOOD_Y:
        BIG_FOOD_X, BIG_FOOD_Y = rondom_c()
        body.append([0, 0])
        score_value += 30
        time_for_big_food = 10*FPS+1


    #level
    last_level = level_value
    level_value = 1 + score_value //50

    
    #body change
    for i in range(len(body) - 1, 0, -1):
        body[i][0] = body[i - 1][0]
        body[i][1] = body[i - 1][1]

    #return to screen
    if body[0][0] > l-11:
        body[0][0] = 10
    if body[0][1] > w-11:
        body[0][1] = 10
    if body[0][1] < 10:
        body[0][1] = w-11
    if body[0][0] < 10:
        body[0][0] = l-11
    
    #body coordination
    body[0][0] += dx
    body[0][1] += dy

    # main screen     
    screen.fill(BLACK)

  
    # Draw score level FPS
    screen.blit(text1, (850,5))
    screen.blit(text2, (850,35))
    screen.blit(text3, (850,65))

    # Draw food
    pygame.draw.circle(screen, WHITE, (food_x, food_y), radius-5)

    if time_for_big_food <= 10*FPS:
        pygame.draw.circle(screen, YELLOW, (BIG_FOOD_X, BIG_FOOD_Y), radius)
        time_for_big_food += 1



    # Draw snake body
    for i, (x, y) in enumerate(body):
        if i!=0:
            pygame.draw.circle(screen, GREEN, (x, y), radius)

    # Draw snake head
    pygame.draw.circle(screen, RED, (body[0][0], body[0][1]), radius)
    
    #level 1
    if level_value == 1:
        pygame.draw.line(screen, BLUE, (300,100),(300, 400), 10)
        if kill_wall_line() == True:
            GAME_OVER()

    # add wall circle & add FPS next level
    if last_level != level_value:
        FPS += 3
        food_x2, food_y2 = rondom_c()
        wall.append([food_x2, food_y2])
        time_for_big_food = 0

    if level_value > 1:
        for i in range(len(wall)):
            pygame.draw.circle(screen, BLUE, (wall[i][0], wall[i][1]), radius-5)
        if kill_wall()== True:
            GAME_OVER()
    
    # Kill yourself
    if kill_yourself()==True:
            GAME_OVER


    pygame.display.flip()

    clock.tick(FPS)
pygame.quit()