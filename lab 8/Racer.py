from email.headerregistry import ContentDispositionHeader
from turtle import screensize
import pygame
import random, time
 
#Initialzing 
pygame.init()
running = True

#misic
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)
 
#FPS 
clock = pygame.time.Clock()
FPS = 10
 
#colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
w = 400
h = 600
SPEED = 5
SCORE = 0
MONEY = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_score = pygame.font.SysFont("Verdana", 10)
game_over = font.render("Game Over", True, BLACK)

#image
background = pygame.image.load("AnimatedStreet.png")
coin_im = pygame.image.load("coins.png")
 
#Create a white screen 
screen = pygame.display.set_mode((w,h))
screen.fill(WHITE)
pygame.display.set_caption("Game")


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(coin_im, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w-40), 0 )  
    def change_location(self):
        self.rect.center = (random.randint(40, w-40), 0 )
    def move(self):    
        self.rect.move_ip(0,5)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, w - 40), 0)


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w-40), 0)  
 
      def move(self):
        global SCORE
        global SPEED
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, w - 40), 0)
        if SCORE %5 == 0 and SCORE != 0:
            SPEED += 0.5
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        global SPEED
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -15)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0,15)
         
        if self.rect.left > 0:
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-15, 0)
        if self.rect.right < w:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(15, 0)
        

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()
 
#Creating Sprites Groups
coins = pygame.sprite.Group()
coins.add(C1)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)


 
#Game Loop
while running: 
       
    #Cycles through all events occurring  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
 
    screen.blit(background, (0,0))
    scores = font_score.render("SCORE: "+str(SCORE), True, BLACK)
    coint_value = font_score.render("MONEY :" +str(MONEY), True, BLACK)
    screen.blit(scores, (10,10))
    screen.blit(coint_value, (300,10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    
    if pygame.sprite.spritecollideany(P1, coins):
        MONEY += 10
        C1.change_location()
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          screen.fill(RED)
          screen.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          running = False
              
         
    pygame.display.update()
    clock.tick(FPS)
