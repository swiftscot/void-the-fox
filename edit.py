import pygame

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
fileDropdown = False
gameLoaded = ""

NAMESMILE = pygame.font.Font('shared/Name Smile.otf', 30)
WHITE = (255,255,255)
GREY = (50,50,50)
PURPLE = (196,0,252)
GREEN = (0,255,0)

def graphics(fileDropdown):
	screen.fill(WHITE)
	for counter in range(int(round(screenSizeW/10)*10)):
		pygame.draw.line(screen, GREY, (counter*40,0), (counter*40, screenSizeH))
	for counter in range(int(round(screenSizeH/10)*10)):
		pygame.draw.line(screen, GREY, (0,counter*40+30), (screenSizeW, counter*40+30))
	pygame.draw.rect(screen, PURPLE, (0,0,screenSizeW,30))
	screen.blit(NAMESMILE.render("File", True, WHITE), (0,0))
	screen.blit(NAMESMILE.render("Tools", True, WHITE), (100,0))
	screen.blit(NAMESMILE.render("Help", True, WHITE), (240,0))
	if fileDropdown:
		pygame.draw.rect(screen, PURPLE, (0,30,300,240))
		screen.blit(NAMESMILE.render("New Level", True, WHITE), (0,30))
		screen.blit(NAMESMILE.render("Save Level", True, WHITE), (0,60))
		screen.blit(NAMESMILE.render("Load Level", True, WHITE), (0,90))
		screen.blit(NAMESMILE.render("New Game", True, WHITE), (0,150))
		screen.blit(NAMESMILE.render("Load Game", True, WHITE), (0,180))
		screen.blit(NAMESMILE.render("Import Assets", True, WHITE), (0,240))
	if gameLoaded == "":
		screen.blit(NAMESMILE.render("You must first load a game. (File > New Game or File > Load Game)", True, GREEN), (350,0))

def input(mouseX,mouseY,mouse1,mouse2):
	global fileDropdown
	if mouseX < 100 and mouseY < 30:
		fileDropdown = True
	if mouseY > 270 or mouseX > 300:
		fileDropdown = False

while running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	mouseX,mouseY = pygame.mouse.get_pos()
	mouse1,mouse3,mouse2 = pygame.mouse.get_pressed(num_buttons=3)
	screenSizeW,screenSizeH = screen.get_size()

	graphics(fileDropdown)
	input(mouseX,mouseY,mouse1,mouse2)
	pygame.display.update()
pygame.quit()