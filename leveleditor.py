import pygame
import os
import math

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((640,640))

# names
saveName = ""
saveTyping = False
loadName = ""
loadTyping = False
gameLoaded = ""
gameTyping = False
newGame = ""
newGameTyping = False
currentLevel = ""

# variables
running = True
menu = True
clock = pygame.time.Clock()
tick = 0 
gameinfocontent = []
sprites = []
spritesExisting = []
tab = 1
neverImported = True

# colours
WHITE = (255,255,255)
LGREY = (150,150,150)
GREY = (50,50,50)
BLUE = (51,51,255)
LBLUE = (102,102,255)
BLACK = (0,0,0)

# images
voiddash = [pygame.image.load("vtf_shared/leveleditor_sprites/voiddash.png"),pygame.image.load("vtf_shared/leveleditor_sprites/voiddash2.png")]
voidsprite = 0

# fonts
logofont = pygame.font.SysFont("Arial", 80)
sublogofont = pygame.font.SysFont("Arial", 20)
normalfont = pygame.font.SysFont("Arial", 50)

# texts
logotext = logofont.render("Void the Fox", True, WHITE)
sublogotext = sublogofont.render("Level Editor prerelease-31May23", True, WHITE)

# loop
while running == True:
  clock.tick(60)
  tick = tick + 1
  keys = pygame.key.get_pressed()
  mouse_x,mouse_y = pygame.mouse.get_pos()
  mouse_1,mouse_2,mouse_3 = pygame.mouse.get_pressed(num_buttons=3)
  pygame.display.set_caption("Void the Fox - Level Editor (loaded game: " + gameLoaded + ") (loaded level: " + currentLevel +") (runtime: " + str(math.trunc(tick/3600)) + " minutes)")
  if round(mouse_y/20) > 24:
    gridmouse_y = 24
  else:
    gridmouse_y = round(mouse_y/20)
  editorxytext = sublogofont.render(str(round(mouse_x/20)) + ", " + str(gridmouse_y), True, WHITE)

  if tick % 5 == 0:
    if voidsprite == 0:
      voidsprite = 1
    else:
      voidsprite = 0
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE and len(gameinfocontent) > 0:
        if menu == True:
          menu = False
        else:
          menu = True
      if event.key == pygame.K_PAUSE:
        if "" > 5:
          break
      if gameTyping == True:
        gameLoaded = gameLoaded + event.unicode
      if gameTyping == True and event.key == pygame.K_RETURN:
        gameTyping = False
        gameLoaded = gameLoaded[:-1]
        gameinfo = open(gameLoaded + "/gameinfo.txt", "r")
        gameinfocontent = gameinfo.readlines()
        for counter in range(len(gameinfocontent)):
          if gameinfocontent[counter].find("sprite---") != -1:
            sprites.append(gameinfocontent[counter][9:-1])
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
        gameinfo.write(newGame + "\n")
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
        currentLevel = saveName
      elif saveTyping == True and event.key == pygame.K_BACKSPACE:
        saveName = saveName[:-2]
      if loadTyping == True:
        loadName = loadName + event.unicode
      if loadTyping == True and event.key == pygame.K_RETURN:
        loadTyping = False
        loadName = loadName[:-1]
        menu = False
        currentLevel = loadName
      elif loadTyping == True and event.key == pygame.K_BACKSPACE:
        loadName = loadName[:-2]

  if menu == True:
    screen.fill(GREY)
    screen.blit(voiddash[voidsprite], (480,500))
    if mouse_x > 20 and mouse_x < 130 and mouse_y > 250 and mouse_y < 300: # new
      if mouse_1 == True and len(gameinfocontent) > 0:
        menu = False
      menunewtext = normalfont.render("New", True, LGREY)
    else:
      menunewtext = normalfont.render("New", True, WHITE)
    if mouse_x > 20 and mouse_x < 145 and mouse_y > 300 and mouse_y < 350: # save
      if mouse_1 == True and len(gameinfocontent) > 0:
        saveTyping = True
        loadTyping = False
        gameTyping = False
        newGameTyping = False
      menusavetext = normalfont.render("Save: " + saveName, True, LGREY)
    else:
      menusavetext = normalfont.render("Save: " + saveName, True, WHITE)
    if mouse_x > 20 and mouse_x < 140 and mouse_y > 350 and mouse_y < 400: # load
      if mouse_1 == True and len(gameinfocontent) > 0:
        loadTyping = True
        gameTyping = False
        newGameTyping = False
        saveTyping = False
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
        loadTyping = False
        saveTyping = False
        newGameTyping = False
      menugametext = normalfont.render("Game: " + gameLoaded, True, LGREY)
    else:
      menugametext = normalfont.render("Game: " + gameLoaded, True, WHITE)
    if mouse_x > 20 and mouse_x < 310 and mouse_y > 550 and mouse_y < 600: # game
      if mouse_1 == True:
        newGameTyping = True
        loadTyping = False
        saveTyping = False
        gameTyping = False
      menunewgametext = normalfont.render("New Game: " + newGame, True, LGREY)
    else:
      menunewgametext = normalfont.render("New Game: " + newGame, True, WHITE)
    screen.blit(logotext, (85,50))
    screen.blit(sublogotext, (168,130))
    screen.blit(menunewtext, (20,250))
    screen.blit(menusavetext, (20,300))
    screen.blit(menuloadtext, (20,350))
    screen.blit(menuquittext, (20,400))
    screen.blit(menugametext, (20,500))
    screen.blit(menunewgametext, (20,550))
  else:
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREY, (0,480,640,160))
    screen.blit(voiddash[voidsprite], (480,500))
    if mouse_x > 5 and mouse_x < 70 and mouse_y > 490 and mouse_y < 510: # sprites
      editorspritestext = sublogofont.render("Sprites", True, LGREY)
      if mouse_1 == True:
        tab = 1
    else:
      editorspritestext = sublogofont.render("Sprites", True, WHITE)
    if mouse_x > 85 and mouse_x < 150 and mouse_y > 490 and mouse_y < 510: # entities
      editorentitiestext = sublogofont.render("Entities", True, LGREY)
      if mouse_1 == True:
        tab = 2
    else:
      editorentitiestext = sublogofont.render("Entities", True, WHITE)
    if mouse_x > 165 and mouse_x < 270 and mouse_y > 490 and mouse_y < 510: # background
      editorbackgroundstext = sublogofont.render("Background", True, LGREY)
      if mouse_1 == True:
        tab = 3
    else:
      editorbackgroundstext = sublogofont.render("Background", True, WHITE)
    if mouse_x > 285 and mouse_x < 340 and mouse_y > 490 and mouse_y < 510: # import
      editorimporttext = sublogofont.render("Import", True, LGREY)
      if mouse_1 == True:
        tab = 4
    else:
      editorimporttext = sublogofont.render("Import", True, WHITE)
    screen.blit(editorxytext, (5, 610))
    screen.blit(editorspritestext, (5, 490))
    screen.blit(editorentitiestext, (85, 490))
    screen.blit(editorbackgroundstext, (165, 490))
    screen.blit(editorimporttext, (285, 490))
    if tab == 1:
      for counter in range(len(sprites)):
        sprite = pygame.image.load(gameLoaded + "/sprites/" + sprites[counter])
        screen.blit(sprite, (counter*20,520))
    if tab == 4:
      if mouse_x > 5 and mouse_x < 165 and mouse_y > 520 and mouse_y < 540: # import sprites
        if neverImported == True:
          importspritestext = sublogofont.render("Import Sprites", True, LBLUE)
        else:
          importspritestext = sublogofont.render("Done!", True, LBLUE)
        if mouse_1 == True and neverImported == True:
          neverImported = False
          gameinfo.close()
          gameinfo = open(gameLoaded + "/gameinfo.txt", "a")
          spritesExisting = os.listdir(gameLoaded + "/sprites")
          spritesNotExisting = []
          for counter in range(len(spritesExisting)):
            for spritescounter in range(len(sprites)):
              if spritesExisting[counter] == sprites[spritescounter]:
                spritesNotExisting.append(counter)
                break
          ogSpritesNotExisting = len(spritesNotExisting)
          for counter in range(len(spritesNotExisting)):
            spritesExisting.pop(spritesNotExisting[counter])
            if counter + 1 != ogSpritesNotExisting:
              spritesNotExisting[counter+1] = spritesNotExisting[counter+1] - counter - 1
          for counter in range(len(spritesExisting)):
            gameinfo.write("sprite---" + spritesExisting[counter] + "\n")
          gameinfo.close()
          gameinfo = open(gameLoaded + "/gameinfo.txt", "r")
          gameinfocontent = gameinfo.readlines()
          gameinfo.close()
          sprites = []
          for counter in range(len(gameinfocontent)):
            if gameinfocontent[counter].find("sprite---") != -1:
              sprites.append(gameinfocontent[counter][9:-1])
      else:
        if neverImported == True:
          importspritestext = sublogofont.render("Import Sprites", True, BLUE)
        else:
          importspritestext = sublogofont.render("Done!", True, BLUE)
      screen.blit(importspritestext, (5, 520))

  pygame.display.update()
pygame.quit()