import pygame
import random
import math
from pygame.constants import QUIT
pygame.init()


#ASA CREEZI O FEREASTRA
screen = pygame.display.set_mode((800, 600))

background = pygame.image.load("background.png")


#TITLU SI LOGO
pygame.display.set_caption("Retro Game")
icon = pygame.image.load("astronaut.png")
pygame.display.set_icon(icon)


#Player1    
player1 = pygame.image.load("space-invaders-1.png")
player1X = 370
player1Y = 480
player1X_change = 0

#Inamici
enemy1 = []
enemy1X = []
enemy1Y = []
enemy1X_change = []
enemy1Y_change = []
num_enemy = 5

for i in range(num_enemy):
    enemy1.append(pygame.image.load("Rau.png"))
    enemy1X.append(random.randint(0, 736)) 
    enemy1Y.append(random.randint(50, 100))  
    enemy1X_change.append(2) 
    enemy1Y_change.append(30) 

#Gloate
bullet = pygame.image.load("bullet2.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"
score = 0

def player(x, y):
    screen.blit(player1, (x,y))

def enemy(x, y, i):
    screen.blit(enemy1[i], (x,y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 16, y + 10))

def collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False



#ASA IL FACI SA STEA DESCHIS PANA CAND APESI PE X
running = True
while running:

  screen.fill((0, 0, 0))
  screen.blit(background, (0,0))
  for event in pygame.event.get():
     if event.type == pygame.QUIT:
         running = False
     #AICI ADAUGAM TASTELE SI FUNCTIILE LOR
     if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT:
             player1X_change = -4
         if event.key == pygame.K_RIGHT:
             player1X_change = 4
         if event.key == pygame.K_SPACE:
             if bullet_state is "ready":
               bulletX = player1X
               fire_bullet(bulletX, bulletY)
     if event.type == pygame.KEYUP:
         if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
             player1X_change = 0

# AICI AVEM MARGINILE CARE NU PERMITE NAVEI SA TREACA DE ELE
  player1X += player1X_change
  if player1X <= 0:
      player1X = 0
  elif player1X >= 736:
      player1X = 736

# AICI PT INAMICI
  for i in range(num_enemy):
    enemy1X[i] += enemy1X_change[i]
    if enemy1X[i] <= 0:
        enemy1X_change[i] = 2
        enemy1Y[i] += enemy1Y_change[i]
    elif enemy1X[i] >= 736:
        enemy1X_change[i] = -2
        enemy1Y[i] += enemy1Y_change[i]

# Coliision
    colision = collision(enemy1X[i], enemy1Y[i], bulletX, bulletY)
    if colision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemy1X[i] = random.randint(0, 735)
        enemy1Y[i] = random.randint(50, 100)

    enemy(enemy1X[i], enemy1Y[i], i)

# AICI PT GLONT
  if bulletY <= 0:
      bulletY = 480
      bullet_state ="ready"

  if bullet_state is "fire":
      fire_bullet(bulletX, bulletY)
      bulletY -= bulletY_change


  player(player1X, player1Y)
  pygame.display.update()


