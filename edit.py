import pygame

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
mainMenuActive = True
newGameActive = False

NAMESMILE = pygame.font.SysFont('Name Smile', 30)
WHITE = (255,255,255)
PURPLE = (196,0,252)
GREY = (50,50,50)

def graphics():
	screen.fill(WHITE)
	for counter in range(int(round(screenSizeW/10)*10)):
		pygame.draw.line(screen, GREY, (counter*40,0), (counter*40, screenSizeH))
	for counter in range(int(round(screenSizeH/10)*10)):
		pygame.draw.line(screen, GREY, (0,counter*40+30), (screenSizeW, counter*40+30))
	pygame.draw.rect(screen, PURPLE, (0,0,screenSizeW,30))
	screen.blit(NAMESMILE.render("File", True, WHITE), (0,0))
	screen.blit(NAMESMILE.render("Tools", True, WHITE), (100,0))
	screen.blit(NAMESMILE.render("Help", True, WHITE), (240,0))

while running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	mouseX,mouseY = pygame.mouse.get_pos()
	mouse1,mouse3,mouse2 = pygame.mouse.get_pressed(num_buttons=3)
	screenSizeW,screenSizeH = screen.get_size()

	graphics()
	pygame.display.update()
pygame.quit()
