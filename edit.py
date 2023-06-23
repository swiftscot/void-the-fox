import pygame

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((640,640))
clock = pygame.time.Clock()
running = True
mainMenuActive = True
newGameActive = False

MAINMENULEFT = pygame.image.load("shared/voidmainmenuleft.png")
MAINMENURIGHT = pygame.image.load("shared/voidmainmenuright.png")
NEWGAMEUI = pygame.image.load("shared/voidnewgame.png")

def main_menu(MAINMENULEFT,MAINMENURIGHT):
    screen.blit(MAINMENULEFT, (0,0))
    screen.blit(MAINMENURIGHT, (366,0))

def new_game(NEWGAMEUI):
    screen.blit(NEWGAMEUI, (0,0))

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouseX,mouseY = pygame.mouse.get_pos()
    mouse1,mouse3,mouse2 = pygame.mouse.get_pressed(num_buttons=3)

    if mainMenuActive and newGameActive == False:
        main_menu(MAINMENULEFT,MAINMENURIGHT)
        if mouse1 and mouseX > 60 and mouseY > 435 and mouseX < 314 and mouseY < 465:
            newGameActive = True
    
    if newGameActive:
        new_game(NEWGAMEUI)

    pygame.display.update()
pygame.quit()
