import pygame
import os

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((640,640))

saveName = ""
saveTyping = False
loadName = ""
loadTyping = False
gameLoaded = ""
gameTyping = False
newGame = ""
newGameTyping = False

WHITE = (255,255,255)
LGREY = (150,150,150)
GREY = (50,50,50)
BLACK = (0,0,0)

logofont = pygame.font.SysFont("Arial", 80)
sublogofont = pygame.font.SysFont("Arial", 20)
normalfont = pygame.font.SysFont("Arial", 50)

logotext = logofont.render("Void the Fox", True, WHITE)
sublogotext = sublogofont.render("Level Editor prerelease-31May23", True, WHITE)
menunewtext = normalfont.render("New", True, WHITE)
menusavetext = normalfont.render("Save: " + saveName, True, WHITE)
menuloadtext = normalfont.render("Load: " + loadName, True, WHITE)
menuquittext = normalfont.render("Quit", True, WHITE)
menugametext = normalfont.render("Game: " + gameLoaded, True, WHITE)
menunewgametext = normalfont.render("New Game: " + newGame, True, WHITE)

running = True
menu = True
clock = pygame.time.Clock()
while running == True:
  clock.tick(60)
  keys = pygame.key.get_pressed()
  mouse_x,mouse_y = pygame.mouse.get_pos()
  mouse_1,mouse_2,mouse_3 = pygame.mouse.get_pressed(num_buttons=3)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        if menu == True:
          menu = False
        else:
          menu = True
      if gameTyping == True:
        gameLoaded = gameLoaded + event.unicode
      if gameTyping == True and event.key == pygame.K_RETURN:
        gameTyping = False
        gameLoaded = gameLoaded[:-1]
        gameinfo = open(gameLoaded + "/gameinfo.txt", "r")
        gameinfocontent = gameinfo.readlines()
      elif gameTyping == True and event.key == pygame.K_BACKSPACE:
        gameLoaded = gameLoaded[:-2]
      if newGameTyping == True:
        newGame = newGame + event.unicode
      if newGameTyping == True and event.key == pygame.K_RETURN:
        newGameTyping = False
        newGame = newGame[:-1]
        os.mkdir(newGame)
        os.mkdir(newGame + "/levels")
        os.mkdir(newGame + "/music")
        os.mkdir(newGame + "/sprites")
        os.mkdir(newGame + "/backgrounds")
        gameinfo = open(newGame + "/gameinfo.txt", "x")
        gameinfo.close()
        gameinfo = open(newGame + "/gameinfo.txt", "a")
        gameinfo.write(newGame)
        gameinfo.close()
        gameinfo = open(newGame + "/gameinfo.txt", "r")
        gameinfocontent = gameinfo.readlines()
        gameLoaded = newGame
      elif newGameTyping == True and event.key == pygame.K_BACKSPACE:
        newGame = newGame[:-2]
      if saveTyping == True:
        saveName = saveName + event.unicode
      if saveTyping == True and event.key == pygame.K_RETURN:
        saveTyping = False
        saveName = saveName[:-1]
        menu = False
      elif saveTyping == True and event.key == pygame.K_BACKSPACE:
        saveName = saveName[:-2]
      if loadTyping == True:
        loadName = loadName + event.unicode
      if loadTyping == True and event.key == pygame.K_RETURN:
        loadTyping = False
        loadName = loadName[:-1]
        menu = False
      elif loadTyping == True and event.key == pygame.K_BACKSPACE:
        loadName = loadName[:-2]

  if menu == True:
    screen.fill(GREY)
    if mouse_x > 20 and mouse_x < 130 and mouse_y > 250 and mouse_y < 300: # new
      if mouse_1 == True:
        menu = False
      menunewtext = normalfont.render("New", True, LGREY)
    else:
      menunewtext = normalfont.render("New", True, WHITE)
    if mouse_x > 20 and mouse_x < 145 and mouse_y > 300 and mouse_y < 350: # save
      if mouse_1 == True:
        saveTyping = True
      menusavetext = normalfont.render("Save: " + saveName, True, LGREY)
    else:
      menusavetext = normalfont.render("Save: " + saveName, True, WHITE)
    if mouse_x > 20 and mouse_x < 140 and mouse_y > 350 and mouse_y < 400: # load
      if mouse_1 == True:
        loadTyping = True
      menuloadtext = normalfont.render("Load: " + loadName, True, LGREY)
    else:
      menuloadtext = normalfont.render("Load: " + loadName, True, WHITE)
    if mouse_x > 20 and mouse_x < 130 and mouse_y > 400 and mouse_y < 450: # quit
      if mouse_1 == True:
        running = False
      menuquittext = normalfont.render("Quit", True, LGREY)
    else:
      menuquittext = normalfont.render("Quit", True, WHITE)
    if mouse_x > 20 and mouse_x < 180 and mouse_y > 500 and mouse_y < 550: # game
      if mouse_1 == True:
        gameTyping = True
      menugametext = normalfont.render("Game: " + gameLoaded, True, LGREY)
    else:
      menugametext = normalfont.render("Game: " + gameLoaded, True, WHITE)
    if mouse_x > 20 and mouse_x < 310 and mouse_y > 550 and mouse_y < 600: # game
      if mouse_1 == True:
        newGameTyping = True
      menunewgametext = normalfont.render("New Game: " + newGame, True, LGREY)
    else:
      menunewgametext = normalfont.render("New Game: " + newGame, True, WHITE)
    screen.blit(logotext, (70,50))
    screen.blit(sublogotext, (155,130))
    screen.blit(menunewtext, (20,250))
    screen.blit(menusavetext, (20,300))
    screen.blit(menuloadtext, (20,350))
    screen.blit(menuquittext, (20,400))
    screen.blit(menugametext, (20,500))
    screen.blit(menunewgametext, (20,550))
  else:
    screen.fill(WHITE)
  pygame.display.update()
pygame.quit()