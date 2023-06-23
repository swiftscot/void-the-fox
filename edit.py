import pygame
import os

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Void Engine Editor")
screenSizeW,screenSizeH = screen.get_size()
clock = pygame.time.Clock()
running = True
fileDropdown = False
toolsDropdown = False
spriteWindowX = 40
spriteWindowY = screenSizeH-520
spriteWindow = True
spriteWindowMoving = False
entityWindowX = 400
entityWindowY = screenSizeH-520
entityWindow = True
entityWindowMoving = False
newGameWindow = False
newGame = ""
gameLoaded = ""
entick = 0
sptick = 0

NAMESMILE = pygame.font.Font('shared/Name Smile.otf', 30)
WHITE = (255,255,255)
GREY = (50,50,50)
DPURPLE = (75,0,97)
PURPLE = (196,0,252)
LPURPLE = (227,128,255)
RED = (255,0,0)
GREEN = (0,255,0)
LBLUE = (50,50,255)

def graphics():
	screen.fill(WHITE)
	for counter in range(int(round(screenSizeW/10)*10)):
		pygame.draw.line(screen, GREY, (counter*40,0), (counter*40, screenSizeH))
	for counter in range(int(round(screenSizeH/10)*10)):
		pygame.draw.line(screen, GREY, (0,counter*40+30), (screenSizeW, counter*40+30))
	if spriteWindow:
		pygame.draw.rect(screen, PURPLE, (spriteWindowX, spriteWindowY, 320, 30))
		pygame.draw.rect(screen, LPURPLE, (spriteWindowX, spriteWindowY+30, 320, 450))
		screen.blit(NAMESMILE.render("Sprites", True, WHITE), (spriteWindowX,spriteWindowY+1))
		pygame.draw.rect(screen, RED, (spriteWindowX+290, spriteWindowY, 30, 30))
		screen.blit(NAMESMILE.render("X", True, WHITE), (spriteWindowX+291,spriteWindowY+1))
		pygame.draw.rect(screen, LBLUE, (spriteWindowX+180,spriteWindowY,110,30))
		screen.blit(NAMESMILE.render("Move", True, WHITE), (spriteWindowX+182,spriteWindowY+1))
	if entityWindow:
		pygame.draw.rect(screen, PURPLE, (entityWindowX, entityWindowY, 320, 30))
		pygame.draw.rect(screen, LPURPLE, (entityWindowX, entityWindowY+30, 320, 450))
		screen.blit(NAMESMILE.render("Entities", True, WHITE), (entityWindowX,entityWindowY+1))
		pygame.draw.rect(screen, RED, (entityWindowX+290, entityWindowY, 30, 30))
		screen.blit(NAMESMILE.render("X", True, WHITE), (entityWindowX+291,entityWindowY+1))
		pygame.draw.rect(screen, LBLUE, (entityWindowX+180,entityWindowY,110,30))
		screen.blit(NAMESMILE.render("Move", True, WHITE), (entityWindowX+182,entityWindowY+1))
	if newGameWindow:
		pygame.draw.rect(screen, PURPLE, (40, 70, 480, 30))
		pygame.draw.rect(screen, LPURPLE, (40, 100, 480, 40))
		pygame.draw.rect(screen, DPURPLE, (45, 105, 470, 30))
		screen.blit(NAMESMILE.render("New Game", True, WHITE), (40,71))
		screen.blit(NAMESMILE.render(newGame, True, WHITE), (45,106))

	pygame.draw.rect(screen, PURPLE, (0,0,screenSizeW,30))
	screen.blit(NAMESMILE.render("File", True, WHITE), (0,0))
	screen.blit(NAMESMILE.render("Tools", True, WHITE), (100,0))
	if fileDropdown:
		pygame.draw.rect(screen, PURPLE, (0,30,240,240))
		screen.blit(NAMESMILE.render("New Level", True, WHITE), (0,30))
		screen.blit(NAMESMILE.render("Save Level", True, WHITE), (0,60))
		screen.blit(NAMESMILE.render("Load Level", True, WHITE), (0,90))
		screen.blit(NAMESMILE.render("New Game", True, WHITE), (0,150))
		screen.blit(NAMESMILE.render("Load Game", True, WHITE), (0,180))
		screen.blit(NAMESMILE.render("Quit Editor", True, WHITE), (0,240))
	elif toolsDropdown:
		pygame.draw.rect(screen, PURPLE, (100,30,300,120))
		screen.blit(NAMESMILE.render("Sprites", True, WHITE), (100,30))
		screen.blit(NAMESMILE.render("Entities", True, WHITE), (100,60))
		screen.blit(NAMESMILE.render("Backgrounds", True, WHITE), (100,90))
		screen.blit(NAMESMILE.render("Game Manager", True, WHITE), (100,120))
	if gameLoaded == "":
		screen.blit(NAMESMILE.render("You must first load a game. (File > New Game or File > Load Game)", True, GREEN), (240,0))

def input(mouseX,mouseY,mouse1,mouse2):
	global fileDropdown
	global toolsDropdown
	global running
	global spriteWindowX
	global spriteWindowY
	global spriteWindow
	global spriteWindowMoving
	global entityWindowX
	global entityWindowY
	global entityWindow
	global entityWindowMoving
	global newGame
	global newGameWindow
	global gameLoaded
	global sptick
	global entick
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if newGameWindow and event.key == pygame.K_RETURN:
				newGameWindow = False
				os.mkdir(newGame)
				os.mkdir(newGame + "/backgrounds")
				os.mkdir(newGame + "/levels")
				os.mkdir(newGame + "/music")
				os.mkdir(newGame + "/sfx")
				os.mkdir(newGame + "/sprites")
				os.mkdir(newGame + "/videos")
				gameLoaded = newGame
			elif newGameWindow and event.key == pygame.K_BACKSPACE:
				newGame = newGame[:-1]
			elif newGameWindow:
				newGame += event.unicode
	if spriteWindow:
		if mouseX > spriteWindowX+290 and mouseX < spriteWindowX+320 and mouseY > spriteWindowY and mouseY < spriteWindowY+30 and mouse1:
			spriteWindow = False
		if mouseX > spriteWindowX+180 and mouseX < spriteWindowX+290 and mouseY > spriteWindowY and mouseY < spriteWindowY+30 and mouse1:
			spriteWindowMoving = True
		if spriteWindowMoving:
			if sptick <= 10:
				sptick = sptick + 1
			spriteWindowX = mouseX-150
			spriteWindowY = mouseY-15
		if sptick >= 10 and mouse1:
			sptick = 0
			spriteWindowMoving = False
	if entityWindow:
		if mouseX > entityWindowX+290 and mouseX < entityWindowX+320 and mouseY > entityWindowY and mouseY < entityWindowY+30 and mouse1:
			entityWindow = False
		if mouseX > entityWindowX+180 and mouseX < entityWindowX+290 and mouseY > entityWindowY and mouseY < entityWindowY+30 and mouse1:
			entityWindowMoving = True
		if entityWindowMoving:
			if entick <= 10:
				entick = entick + 1
			entityWindowX = mouseX-150
			entityWindowY = mouseY-15
		if entick >= 10 and mouse1:
			entick = 0
			entityWindowMoving = False
	if mouseX < 100 and mouseY < 30:
		fileDropdown = True
		toolsDropdown = False
	if fileDropdown:
		if mouseY > 270 or mouseX > 300:
			fileDropdown = False
		if mouseY > 150 and mouseY < 180 and mouseX > 0 and mouseX < 240 and mouse1:
			newGameWindow = True
		if mouseY > 240 and mouseY < 270 and mouseX > 0 and mouseX < 240 and mouse1:
			running = False
	if mouseX > 100 and mouseX < 240 and mouseY < 30:
		fileDropdown = False
		toolsDropdown = True
	if toolsDropdown:
		if mouseY > 150 or mouseX > 400 or mouseX < 100:
			toolsDropdown = False
		if mouseY > 30 and mouseY < 60 and mouseX > 100 and mouseX < 400 and mouse1:
			spriteWindow = True
			spriteWindowX = 40
			spriteWindowY = screenSizeH-520
		if mouseY > 60 and mouseY < 90 and mouseX > 100 and mouseX < 400 and mouse1:
			entityWindow = True
			entityWindowX = 400
			entityWindowY = screenSizeH-520

while running:
	clock.tick(60)
	mouseX,mouseY = pygame.mouse.get_pos()
	mouse1,mouse3,mouse2 = pygame.mouse.get_pressed(num_buttons=3)

	graphics()
	input(mouseX,mouseY,mouse1,mouse2)
	pygame.display.update()
pygame.quit()