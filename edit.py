# Imports
import pygame
import datetime
import os

# Pygame Initialization
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
pygame.display.set_caption("Void Engine prerelease editor")
pygame.display.set_icon(pygame.image.load("shared/icon.png"))
clock = pygame.time.Clock()

# Variables
running = True
tick = 0
seconds = 0
minutes = 0
hours = 0
homepageWindow = True
newGameWindow = False
textInput = ""
textInputActive = False

# Functions
def close_all_windows():
    global homepageWindow
    global newGameWindow
    global textInput
    global textInputActive
    homepageWindow = False
    newGameWindow = False
    textInput = ""
    textInputActive = True

# Pre-defined Variables - Colours
PURPLE = (210,0,252)
DPURPLE = (168,0,235)
WHITE = (255,255,255)
LGREY = (200,200,200)

# Pre-defined Variables - Fonts and Text
LOGOFONT = pygame.font.Font("shared/Ubuntu-Bold.ttf", 50)
LOGOTEXT = LOGOFONT.render("Void Engine prerelease editor", True, WHITE)
FONT = pygame.font.Font("shared/Ubuntu-Medium.ttf", 20)
SPLASH = FONT.render("Void Engine prerelease still needs a lot of work.", True, WHITE)
CHECKLIST = [
    "Editor:",
    "o User Interface (sidebars, levelgrid, metadata)",
    "o Game Creation (creating the directories and gameinfo)",
    "o Importing Assets (sprites, backgrounds, music, etcetra)",
    "o Placing Sprites & Entities",
    "o Saving and Loading Levels",
    "o Modifying Game Info (startmaps, weapons, external alias)",
    "",
    "Client:",
    "o Game Loading (loading sprites, levels, gameinfo)",
    "o User Interface (title screen, ingame ui)",
    "o Client Logic (movement, weapons)",
    "o Debug Console (load maps, noclip, all that)"
]

# Main Loop
while running:
    # Pygame
    clock.tick(60)

    # Runtime Logic
    tick = tick + 1
    if tick == 60:
        tick = 0
        seconds = int(seconds) + 1
    if int(seconds) == 60:
        seconds = 0
        minutes = int(minutes) + 1
    if int(minutes) == 60:
        minutes = 0
        hours = int(hours) + 1
    if len(str(seconds)) != 2:
        seconds = "0" + str(seconds)
    if len(str(minutes)) != 2:
        minutes = "0" + str(minutes)
    if len(str(hours)) != 2:
        hours = "0" + str(hours)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and textInputActive == True:
            if event.key == pygame.K_RETURN:
                textInputActive = False
            elif event.key == pygame.K_BACKSPACE:
                textInput = textInput[:-1]
            else:
                textInput = textInput + event.unicode


    # Inputs
    windowSizeWidth,windowSizeHeight = window.get_size()
    mouseX,mouseY = pygame.mouse.get_pos()
    mouse1,mouse3,mouse2 = pygame.mouse.get_pressed(num_buttons=3)

    # Display and Graphics - Home
    if homepageWindow:
        window.fill(DPURPLE)
        window.blit(LOGOTEXT, (305,5))
        window.blit(SPLASH, (305,60))
        for counter in range(len(CHECKLIST)):
            window.blit(FONT.render(CHECKLIST[counter], True, WHITE), (305,100+counter*20))
    elif newGameWindow:
        window.fill(DPURPLE)
        window.blit(LOGOFONT.render("New Game", True, WHITE), (305,5))
        window.blit(FONT.render("Please enter the new game's internal name: " + textInput, True, WHITE), (305,55))
        for counter in range(len(status)):
            window.blit(FONT.render(status[counter], True, WHITE), (305,75+counter*20))
        if textInputActive == False and newGameCreated == False:
            status.append("Starting " + textInput + " creation process...")
            os.mkdir(textInput)
            status.append("Created " + textInput + " directory.")
            os.mkdir(textInput + "/backgrounds")
            status.append("Created " + textInput + "/backgrounds directory.")
            os.mkdir(textInput + "/chapters")
            status.append("Created " + textInput + "/chapters directory.")
            os.mkdir(textInput + "/gamemodes")
            status.append("Created " + textInput + "/gamemodes directory.")
            os.mkdir(textInput + "/levels")
            status.append("Created " + textInput + "/levels directory.")
            os.mkdir(textInput + "/music")
            status.append("Created " + textInput + "/music directory.")
            os.mkdir(textInput + "/sprites")
            status.append("Created " + textInput + "/sprites directory.")
            os.mkdir(textInput + "/weapons")
            status.append("Created " + textInput + "/weapons directory.")
            gameInfo = open(textInput + "/gameinfo.ve", "x")
            gameInfo.close()
            status.append("Created " + textInput + "/gameinfo.ve file.")
            newGameCreated = True
            status.append("Done.")


    # Display and Graphics - Sidebar
    pygame.draw.rect(window, PURPLE, (0,0,300,windowSizeHeight))
    if mouseX > 5 and mouseX < 105 and mouseY > 5 and mouseY < 25:
        window.blit(FONT.render("Homepage", True, LGREY), (5,5))
        if mouse1:
            close_all_windows()
            homepageWindow = True
    else:
        window.blit(FONT.render("Homepage", True, WHITE), (5,5))

    if mouseX > 5 and mouseX < 105 and mouseY > 45 and mouseY < 65:
        window.blit(FONT.render("New Game", True, LGREY), (5,45))
        if mouse1:
            close_all_windows()
            newGameWindow = True
            newGameCreated = False
            status = []
    else:
        window.blit(FONT.render("New Game", True, WHITE), (5,45))
    window.blit(FONT.render("Edit Game", True, WHITE), (5,65))
    window.blit(FONT.render("Load Game", True, WHITE), (5,85))

    window.blit(FONT.render("New Level", True, WHITE), (5,125))
    window.blit(FONT.render("Save Level", True, WHITE), (5,145))
    window.blit(FONT.render("Load Level", True, WHITE), (5,165))

    window.blit(FONT.render("New Weapon", True, WHITE), (5,205))
    window.blit(FONT.render("Save Weapon", True, WHITE), (5,225))
    window.blit(FONT.render("Load Weapon", True, WHITE), (5,245))

    window.blit(FONT.render("New Chapter (SP Only)", True, WHITE), (5,285))
    window.blit(FONT.render("Save Chapter (SP Only)", True, WHITE), (5,305))
    window.blit(FONT.render("Load Chapter (SP Only)", True, WHITE), (5,325))

    window.blit(FONT.render("New Gamemode (MP Only)", True, WHITE), (5,365))
    window.blit(FONT.render("Save Gamemode (MP Only)", True, WHITE), (5,385))
    window.blit(FONT.render("Load Gamemode (MP Only)", True, WHITE), (5,405))

    window.blit(FONT.render("Running for " + str(hours) + ":" + str(minutes) + "." + str(seconds), True, WHITE), (5,windowSizeHeight-45))
    window.blit(FONT.render(str(datetime.datetime.now())[:str(datetime.datetime.now()).find(".")], True, WHITE), (5,windowSizeHeight-25))

    pygame.display.update()
pygame.quit()
