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
spritex = []
spritey = []
spriteid = []
entities = ["spawn.png", "ally.png", "enemy.png", "dialogue.png", "sfx.png", "music.png", "video.png"]
entityx = []
entityy = []
entitydata = []
selectedSprite = -1
selectedEntity = -1
bgs = []
bgsExisting = []
activeBg = ""
activeBgName = ""
activeBgId = -1
tab = 1
page = 1
camerax = 0
cameray = 0

# colours
WHITE = (255,255,255)
LGREY = (150,150,150)
GREY = (50,50,50)
BLUE = (51,51,255)
LBLUE = (102,102,255)
BLACK = (0,0,0)
V01 = (255,0,0)

# images
voiddash = [pygame.image.load("vtf_shared/leveleditor_sprites/voiddash.png"),pygame.image.load("vtf_shared/leveleditor_sprites/voiddash2.png")]
voidsprite = 0

# fonts
logofont = pygame.font.SysFont("Arial", 80)
sublogofont = pygame.font.SysFont("Arial", 20)
normalfont = pygame.font.SysFont("Arial", 50)

# texts
logotext = logofont.render("Void Engine", True, V01)
sublogotext = sublogofont.render("Level Editor v0.1 - Barebones", True, V01)

# loop
while running == True:
  clock.tick(60)
  tick = tick + 1
  keys = pygame.key.get_pressed()
  mousex,mousey = pygame.mouse.get_pos()
  mouse1,mouse2,mouse3 = pygame.mouse.get_pressed(num_buttons=3)
  pygame.display.set_caption("Void Engine - Level Editor (loaded game: " + gameLoaded + ") (loaded level: " + currentLevel +") (runtime: " + str(math.trunc(tick/3600)) + " minutes)")
  editorxytext = sublogofont.render(str(int(round(mousex/20) + round(camerax/20)/-1)) + ", " + str(round(mousey/20) + round(cameray/20)), True, WHITE)
  editorpagetext = sublogofont.render("Page: " + str(page), True, WHITE)
  editorspritesusedtext = sublogofont.render("Sprites used: " + str(len(spritex)), True, WHITE)
  editorentitesusedtext = sublogofont.render("Entities used: " + str(len(entityx)), True, WHITE)
  editorbgusedtext = sublogofont.render("BG used: " + activeBgName, True, WHITE)
  editorselectedspritetext = sublogofont.render("Sprite/entity selected: ", True, WHITE)
  
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
      if event.key == pygame.K_COMMA:
        page = page - 1
      if event.key == pygame.K_PERIOD:
        page = page + 1
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
        sprites = []
        bgs = []
        for counter in range(len(gameinfocontent)):
          if gameinfocontent[counter].find("sprite---") != -1:
            sprites.append(gameinfocontent[counter][gameinfocontent[counter].find("---")+3:-1])
          if gameinfocontent[counter].find("bg-------") != -1:
            bgs.append(gameinfocontent[counter][gameinfocontent[counter].find("-------")+7:-1])
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
        os.mkdir(newGame + "/videos")
        os.mkdir(newGame + "/sfx")
        gameinfo = open(newGame + "/gameinfo.txt", "x")
        gameinfo.close()
        gameinfo = open(newGame + "/gameinfo.txt", "a")
        gameinfo.write(newGame + "\n")
        gameinfo.close()
        gameinfo = open(newGame + "/gameinfo.txt", "r")
        gameinfocontent = gameinfo.readlines()
        gameLoaded = newGame
        sprites = []
        bgs = []
      elif newGameTyping == True and event.key == pygame.K_BACKSPACE:
        newGame = newGame[:-2]
      if saveTyping == True:
        saveName = saveName + event.unicode
      if saveTyping == True and event.key == pygame.K_RETURN:
        saveTyping = False
        saveName = saveName[:-1]
        menu = False
        currentLevel = saveName
        if os.path.exists(gameLoaded + "/levels/" + saveName + ".vtflevel"):
          os.remove(gameLoaded + "/levels/" + saveName + ".vtflevel")
        saveFile = open(gameLoaded + "/levels/" + saveName + ".vtflevel", "x")
        saveFile.close()
        saveFile = open(gameLoaded + "/levels/" + saveName + ".vtflevel", "a")
        saveFile.write("bg" + str(activeBgId) + "id\n")
        for counter in range(len(spritex)):
          saveFile.write("sprite" + str(spriteid[counter]) + "id" + str(spritex[counter]) + "xc" + str(spritey[counter]) + "yc\n")
        for counter in range(len(entitydata)):
          saveFile.write("entity" + str(entitydata[counter]) + "id" + str(entityx[counter]) + "xc" + str(entityy[counter]) + "yc\n")
        saveFile.close()
      elif saveTyping == True and event.key == pygame.K_BACKSPACE:
        saveName = saveName[:-2]
      if loadTyping == True:
        loadName = loadName + event.unicode
      if loadTyping == True and event.key == pygame.K_RETURN:
        loadTyping = False
        loadName = loadName[:-1]
        menu = False
        currentLevel = loadName
        loadFile = open(gameLoaded + "/levels/" + loadName + ".vtflevel", "r")
        loadFileContents = loadFile.readlines()
        if loadFileContents[0] == "bg-1id\n":
          print("no background")
        else:
          activeBg = pygame.image.load(gameLoaded + "/backgrounds/" + bgs[int(loadFileContents[0][2:loadFileContents[0].find("id")])])
          activeBgName = bgs[int(loadFileContents[0][2:loadFileContents[0].find("id")])]
          activeBgId = int(loadFileContents[0][2:loadFileContents[0].find("id")])
        spriteid = []
        spritex = []
        spritey = []
        entitydata = []
        entityx = []
        entityy = []
        for counter in range(len(loadFileContents)):
          if loadFileContents[counter].find("sprite") != -1:
            spriteid.append(int(loadFileContents[counter][6:loadFileContents[counter].find("id")]))
            spritex.append(int(loadFileContents[counter][loadFileContents[counter].find("id")+2:loadFileContents[counter].find("xc")]))
            spritey.append(int(loadFileContents[counter][loadFileContents[counter].find("xc")+2:loadFileContents[counter].find("yc")]))
          if loadFileContents[counter].find("entity") != -1:
            entitydata.append(int(loadFileContents[counter][6:loadFileContents[counter].find("id")]))
            entityx.append(int(loadFileContents[counter][loadFileContents[counter].find("id")+2:loadFileContents[counter].find("xc")]))
            entityy.append(int(loadFileContents[counter][loadFileContents[counter].find("xc")+2:loadFileContents[counter].find("yc")]))
      elif loadTyping == True and event.key == pygame.K_BACKSPACE:
        loadName = loadName[:-2]

  if keys[pygame.K_RIGHT]:
    camerax = camerax - 20
  if keys[pygame.K_LEFT]:
    camerax = camerax + 20
  if keys[pygame.K_UP]:
    cameray = cameray + 20
  if keys[pygame.K_DOWN]:
    cameray = cameray - 20

  if page < 1:
    page = 1
  elif page > math.trunc(len(sprites)/20)+1 or page > math.trunc(len(bgs)/8)+1:
    page = page - 1
  if menu == True:
    screen.fill(GREY)
    screen.blit(voiddash[voidsprite], (480,500))
    if mousex > 20 and mousex < 130 and mousey > 250 and mousey < 300: # new
      if mouse1 == True and len(gameinfocontent) > 0:
        menu = False
        spritex = []
        spritey = []
        spriteid = []
        entityx = []
        entityy = []
        entitydata = []
        activeBg = ""
        activeBgName = ""
        activeBgId = -1
      menunewtext = normalfont.render("New", True, LGREY)
    else:
      menunewtext = normalfont.render("New", True, WHITE)
    if mousex > 20 and mousex < 145 and mousey > 300 and mousey < 350: # save
      if mouse1 == True and len(gameinfocontent) > 0:
        saveTyping = True
        loadTyping = False
        gameTyping = False
        newGameTyping = False
      menusavetext = normalfont.render("Save: " + saveName, True, LGREY)
    else:
      menusavetext = normalfont.render("Save: " + saveName, True, WHITE)
    if mousex > 20 and mousex < 140 and mousey > 350 and mousey < 400: # load
      if mouse1 == True and len(gameinfocontent) > 0:
        loadTyping = True
        gameTyping = False
        newGameTyping = False
        saveTyping = False
      menuloadtext = normalfont.render("Load: " + loadName, True, LGREY)
    else:
      menuloadtext = normalfont.render("Load: " + loadName, True, WHITE)
    if mousex > 20 and mousex < 130 and mousey > 400 and mousey < 450: # quit
      if mouse1 == True:
        running = False
      menuquittext = normalfont.render("Quit", True, LGREY)
    else:
      menuquittext = normalfont.render("Quit", True, WHITE)
    if mousex > 20 and mousex < 180 and mousey > 500 and mousey < 550: # game
      if mouse1 == True:
        gameTyping = True
        loadTyping = False
        saveTyping = False
        newGameTyping = False
      menugametext = normalfont.render("Game: " + gameLoaded, True, LGREY)
    else:
      menugametext = normalfont.render("Game: " + gameLoaded, True, WHITE)
    if mousex > 20 and mousex < 310 and mousey > 550 and mousey < 600: # game
      if mouse1 == True:
        newGameTyping = True
        loadTyping = False
        saveTyping = False
        gameTyping = False
      menunewgametext = normalfont.render("New Game: " + newGame, True, LGREY)
    else:
      menunewgametext = normalfont.render("New Game: " + newGame, True, WHITE)
    screen.blit(logotext, (85,50))
    screen.blit(sublogotext, (168,145))
    screen.blit(menunewtext, (20,250))
    screen.blit(menusavetext, (20,300))
    screen.blit(menuloadtext, (20,350))
    screen.blit(menuquittext, (20,400))
    screen.blit(menugametext, (20,500))
    screen.blit(menunewgametext, (20,550))
  else:
    screen.fill(WHITE)
    if activeBg != "":
      screen.blit(activeBg, (0 + math.trunc(camerax/20)*20,0 + math.trunc(cameray/20)*20))
    if len(entitydata) > 0:
      for counter in range(len(entitydata)):
        screen.blit(pygame.image.load("vtf_shared/leveleditor_entities/" + entities[entitydata[counter]]), (entityx[counter] + math.trunc(camerax/20)*20,entityy[counter] + math.trunc(cameray/20)*20))
    pygame.draw.rect(screen, GREY, (0,480,640,160))
    screen.blit(voiddash[voidsprite], (480,500))
    if len(spriteid) > 0:
      for counter in range(len(spriteid)):
        screen.blit(pygame.image.load(gameLoaded + "/sprites/" + sprites[spriteid[counter]]), (spritex[counter] + math.trunc(camerax/20)*20,spritey[counter] + math.trunc(cameray/20)*20))
    for counter in range(32):
      pygame.draw.line(screen, (LGREY), (counter*20,0), (counter*20,479))
    for counter in range(24):
      pygame.draw.line(screen, (LGREY), (0,counter*20), (640,counter*20))
    if mousey < 480 and mouse1 == True and selectedSprite != -1:
      spriteNotOkay = False
      for counter in range(len(spritex)):
        if spritex[counter] == math.trunc(mousex/20)*20 - math.trunc(camerax/20)*20 and spritey[counter] == math.trunc(mousey/20)*20 - math.trunc(cameray/20)*20:
          spriteNotOkay = True
      if spriteNotOkay == False:
        spritex.append(math.trunc(mousex/20)*20 - math.trunc(camerax/20)*20)
        spritey.append(math.trunc(mousey/20)*20 - math.trunc(cameray/20)*20)
        spriteid.append(selectedSprite)
    elif mousey < 480 and mouse1 == True and selectedEntity != -1:
      entityNotOkay = False
      for counter in range(len(entityx)):
        if entityx[counter] == math.trunc(mousex/20)*20 - math.trunc(camerax/20)*20 and entityy[counter] == math.trunc(mousey/20)*20 - math.trunc(cameray/20)*20:
          entityNotOkay = True
      if entityNotOkay == False:
        if selectedEntity == 0:
          spawnPlaced = False
          for counter in range(len(entitydata)):
            if entitydata[counter] == 0:
              spawnPlaced = True
          if spawnPlaced == False:
            entityx.append(math.trunc(mousex/20)*20 - math.trunc(camerax/20)*20)
            entityy.append(math.trunc(mousey/20)*20 - math.trunc(cameray/20)*20)
            entitydata.append(0)
    if mousey < 480 and mouse3 == True:
      if len(spriteid) > 0:
        for counter in range(len(spriteid)):
          if spritex[counter] == math.trunc(mousex/20)*20 - math.trunc(camerax/20)*20 and spritey[counter] == math.trunc(mousey/20)*20 - math.trunc(cameray/20)*20:
            spritex.pop(counter)
            spritey.pop(counter)
            spriteid.pop(counter)
            break
        for counter in range(len(entitydata)):
          if entityx[counter] == math.trunc(mousex/20)*20 - math.trunc(camerax/20)*20 and entityy[counter] == math.trunc(mousey/20)*20 - math.trunc(cameray/20)*20:
            entityx.pop(counter)
            entityy.pop(counter)
            entitydata.pop(counter)
            break
    if mousex > 5 and mousex < 70 and mousey > 490 and mousey < 510: # sprites
      editorspritestext = sublogofont.render("Sprites", True, LGREY)
      if mouse1 == True:
        tab = 1
    else:
      editorspritestext = sublogofont.render("Sprites", True, WHITE)
    if mousex > 85 and mousex < 150 and mousey > 490 and mousey < 510: # entities
      editorentitiestext = sublogofont.render("Entities", True, LGREY)
      if mouse1 == True:
        tab = 2
    else:
      editorentitiestext = sublogofont.render("Entities", True, WHITE)
    if mousex > 165 and mousex < 270 and mousey > 490 and mousey < 510: # background
      editorbackgroundstext = sublogofont.render("Background", True, LGREY)
      if mouse1 == True:
        tab = 3
    else:
      editorbackgroundstext = sublogofont.render("Background", True, WHITE)
    if mousex > 285 and mousex < 340 and mousey > 490 and mousey < 510: # import
      editorimporttext = sublogofont.render("Import", True, LGREY)
      if mouse1 == True:
        tab = 4
    else:
      editorimporttext = sublogofont.render("Import", True, WHITE)
    screen.blit(editorxytext, (5, 610))
    screen.blit(editorpagetext, (100, 610))
    screen.blit(editorselectedspritetext, (200, 610))
    screen.blit(editorspritesusedtext, (5,580))
    screen.blit(editorentitesusedtext, (175,580))
    screen.blit(editorbgusedtext, (355,580))
    screen.blit(editorspritestext, (5, 490))
    screen.blit(editorentitiestext, (85, 490))
    screen.blit(editorbackgroundstext, (165, 490))
    screen.blit(editorimporttext, (285, 490))
    if selectedSprite != -1:
      selectedSpriteImg = pygame.image.load(gameLoaded + "/sprites/" + sprites[selectedSprite])
      screen.blit(selectedSpriteImg, (425, 612))
    elif selectedEntity != -1:
      selectedEntityImg = pygame.image.load("vtf_shared/leveleditor_entities/" + entities[selectedEntity])
      screen.blit(selectedEntityImg, (425, 612))
    if tab == 1:
      for counter in range(len(sprites)):
        sprite = pygame.transform.scale(pygame.image.load(gameLoaded + "/sprites/" + sprites[counter]), (40, 40))
        if counter < 10 and page == 1:
          screen.blit(sprite, (counter*40,520))
        elif counter < 10*page and counter >= 10*(page-1):
          screen.blit(sprite, (counter*40-page*200,520))
        if mousex > counter*40 and mousex < counter*40+40 and mousey > 520 and mousey < 560 and mouse1 == True:
          selectedSprite = counter
          selectedEntity = -1
    if tab == 2:
      for counter in range(len(entities)):
        entity = pygame.transform.scale(pygame.image.load("vtf_shared/leveleditor_entities/" + entities[counter]), (40,40))
        screen.blit(entity, (counter*40,520))
        if mousex > counter*40 and mousex < counter*40+40 and mousey > 520 and mousey < 560 and mouse1 == True:
          selectedSprite = -1
          selectedEntity = counter
    if tab == 3:
      for counter in range(len(bgs)):
        if counter < 6 and page == 1:
          bg = pygame.image.load(gameLoaded + "/backgrounds/" + bgs[counter])
          bg = pygame.transform.scale(bg, (80,60))
          screen.blit(bg, (counter*80,520))
        elif counter < 6*page and counter >= 6*(page-1):
          bg = pygame.image.load(gameLoaded + "/backgrounds/" + bgs[counter])
          bg = pygame.transform.scale(bg, (80,60))
          screen.blit(bg, (counter*80-page*480,520))
        if mousex > counter*80 and mousex < counter*80+80 and mousey > 520 and mousey < 580 and mouse1 == True:
          activeBg = pygame.image.load(gameLoaded + "/backgrounds/" + bgs[counter])
          activeBgName = bgs[counter]
          activeBgId = counter
    if tab == 4:
      if mousex > 5 and mousex < 165 and mousey > 520 and mousey < 540: # import sprites
        importspritestext = sublogofont.render("Import Sprites", True, LBLUE)
        if mouse1 == True:
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
            gameinfo.write(str(counter+len(sprites)) + "sprite---" + spritesExisting[counter] + "\n")
          gameinfo.close()
          gameinfo = open(gameLoaded + "/gameinfo.txt", "r")
          gameinfocontent = gameinfo.readlines()
          gameinfo.close()
          sprites = []
          for counter in range(len(gameinfocontent)):
            if gameinfocontent[counter].find("sprite---") != -1:
              sprites.append(gameinfocontent[counter][gameinfocontent[counter].find("---")+3:-1])
      else:
        importspritestext = sublogofont.render("Import Sprites", True, BLUE)
      if mousex > 5 and mousex < 205 and mousey > 540 and mousey < 560:
        importbgtext = sublogofont.render("Import Backgrounds", True, LBLUE)
        if mouse1 == True:
          gameinfo.close()
          gameinfo = open(gameLoaded + "/gameinfo.txt", "a")
          bgsExisting = os.listdir(gameLoaded + "/backgrounds")
          bgsNotExisting = []
          for counter in range(len(bgsExisting)):
            for bgcounter in range(len(bgs)):
              if bgsExisting[counter] == bgs[bgcounter]:
                bgsNotExisting.append(counter)
                break
          ogBgsNotExisting = len(bgsNotExisting)
          for counter in range(len(bgsNotExisting)):
            bgsExisting.pop(bgsNotExisting[counter])
            if counter + 1 != ogBgsNotExisting:
              bgsNotExisting[counter+1] = bgsNotExisting[counter+1] - counter - 1
          for counter in range(len(bgsExisting)):
            gameinfo.write(str(counter+len(bgs) + "bg-------" + bgsExisting[counter] + "\n"))
          gameinfo.close()
          gameinfo = open(gameLoaded + "/gameinfo.txt", "r")
          gameinfocontent = gameinfo.readlines()
          gameinfo.close()
          bgs = []
          for counter in range(len(gameinfocontent)):
            if gameinfocontent[counter].find("bg-------") != -1:
              bgs.append(gameinfocontent[counter][gameinfocontent[counter].find("-------")+7:-1])
      else:
        importbgtext = sublogofont.render("Import Backgrounds", True, BLUE)
      if mousex > 5 and mousex < 145 and mousey > 560 and mousey < 580:
        importmusictext = sublogofont.render("Import Media", True, LBLUE)
      else:
        importmusictext = sublogofont.render("Import Media", True, BLUE)
      screen.blit(importspritestext, (5, 520))
      screen.blit(importbgtext, (5, 540))
      screen.blit(importmusictext, (5, 560))

  pygame.display.update()
pygame.quit()