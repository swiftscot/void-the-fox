# Imported Modules
import pygame
import os

# Pygame Initialization
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Void Engine")

# Colours
WHITE = (255,255,255)
LGREY = (150,150,150)
GREY = (50,50,50)
DGREY = (25,25,25)
V01 = (255,51,51)

# Fonts
subfont = pygame.font.SysFont("Arial", 20)

# Variables
running = True # If this is False, the main loop stops, closing the game
gameList = [] # This is an array that will hold all found Void Engine games
gameListInternal = [] # This is an array that will hold all found Void Engine game's internal names
gameSelected = "" # The selected game from the game list

# Check for Void Engine Games
currentDirectory = os.listdir() # This is an array of everything in the root Void Engine folder
for counter in range(len(currentDirectory)): # This is a loop that finds the Void Engine games
  if currentDirectory[counter].find(".") != -1 or currentDirectory[counter].find("vtf_shared") != -1 or currentDirectory[counter].find("venv") != -1:
    print(currentDirectory[counter] + " is not a Void Engine game!")
  else:
    gameInfoFile = open(currentDirectory[counter] + "/gameinfo.txt", "r") # This opens the gameinfo file
    gameInfoContents = gameInfoFile.readlines()
    print(gameInfoContents[0][:-1] + " is a Void Engine game!")
    gameList.append(gameInfoContents[0][:-1]) # This adds the game to the game list
    gameListInternal.append(currentDirectory[counter])

while running: # This is the main loop
  mousex,mousey = pygame.mouse.get_pos()
  mouse1,mouse3,mouse2 = pygame.mouse.get_pressed(num_buttons=3)
  for event in pygame.event.get(): # Checks for pygame events
    if pygame.event == pygame.QUIT:
      running = False

  screen.fill(GREY)
  pygame.draw.rect(screen, DGREY, (5,5,225,435))
  pygame.draw.rect(screen, DGREY, (5,445,225,25))
  # This displays every found Void Engine game and detects if the user hovers / clicks on a game
  for counter in range(len(gameList)):
    screen.blit(subfont.render(gameList[counter], True, WHITE), (10, counter*20+10))
    if mousex > 10 and mousex < 225 and mousey > 10+counter*20 and mousey < 30+counter*20:
      screen.blit(subfont.render(gameList[counter], True, LGREY), (10, counter*20+10))
      if mouse1 == True:
        gameSelected = gameListInternal[counter]

  # This displays all the selected games info and buttons and stuff
  if gameSelected != "":
    if os.path.exists(gameSelected + "/banner.png"):
      pygame.draw.rect(screen, DGREY, (235,5,400,465))
      screen.blit(pygame.image.load(gameSelected + "/banner.png"), (240, 10))
    
  pygame.display.update()
pygame.quit()