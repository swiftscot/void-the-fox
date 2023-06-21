import pygame

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode()
running = True
mainMenuActive = True

MAINMENULEFT = pygame.image.load("shared/voidmainmenuleft.png")
MAINMENURIGHT = pygame.image.load("shared/voidmainmenuright.png")

def main_menu(MAINMENULEFT, MAINMENURIGHT):
  screen.blit(MAINMENULEFT, (0,0))
  screen.blit(MAINMENURIGHT, (366,0))

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  if mainMenuActive:
    main_menu(MAINMENULEFT, MAINMENURIGHT)
    
  pygame.display.update()
pygame.quit()
