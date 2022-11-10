import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('ship.png')
pygame.display.set_icon(icon)

background=pygame.image.load('back.jpg')

playerImage=pygame.image.load('spaceship.png')
playerX=370
playerY=480
playerX_change = 0

enemyImage=pygame.image.load('alien.png')
enemyX=random.randint(0,800)
enemyY=40 #random.randint(50,150)
enemyX_change = 5
enemyY_change = 40

bulletImage=pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

explosionImage=pygame.image.load('explosion.png')

def player(x,y):
	screen.blit(playerImage,(x,y))
 
def enemy(x,y):
	screen.blit(enemyImage,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage,(x+16,y+10))
 
running = True
while running:
	playerX_change = 0
	screen.fill((100,100,100))
	screen.blit(background,(0,0))
	for event in pygame.event.get():
		pressed = pygame.key.get_pressed()
		if event.type == pygame.QUIT or pressed[pygame.QUIT]:
			running = False
			#pygame.quit()
		if event.type == pygame.KEYDOWN:
			#print("Key is pressed")
			if pressed[pygame.K_LEFT]:
				#print("Left arrow is pressed")
				playerX_change = -10
			if pressed[pygame.K_RIGHT]:
				playerX_change = 10
			if pressed[pygame.K_SPACE]:
				if bullet_state is not "fire":
					fire_bullet(playerX,bulletY)
					bulletX = playerX
		if event.type == pygame.KEYUP:
			if pressed[pygame.K_LEFT] or pressed[pygame.K_RIGHT]:
				playerX_change = 0
	playerX += playerX_change
	if playerX <= 0:
		playerX = 0
	elif playerX >= 736:
		playerX = 736
	player(playerX,playerY)
	
 
	enemyX += enemyX_change
	if enemyX <= 0:
		enemyX_change = 5
		enemyY += enemyY_change
	elif enemyX >= 736:
		enemyX_change = -5
		enemyY += enemyY_change
	elif enemyY >= 400:
		running = False
	
 
	if bullet_state is "fire":
		fire_bullet(bulletX,bulletY)
		bulletY -= bulletY_change
	if bulletY == 0:
		bullet_state = "ready"
		bulletY=480
	if ( bulletY <= enemyY +32 and bulletY >= enemyY ) and ( bulletX >= enemyX and bulletX <= enemyX+64):
		bullet_state = "ready"
		screen.blit(explosionImage,(bulletX,bulletY))
		bulletY=480
		enemyX=random.randint(0,800)
		enemyY=40

	player(playerX,playerY)
	enemy(enemyX,enemyY)
	#pygame.display.update()
	pygame.display.flip()
	clock.tick(120)
