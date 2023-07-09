# Imports
import pygame
import datetime

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

# Pre-defined Variables - Colours
PURPLE = (210,0,252)
DPURPLE = (168,0,235)
WHITE = (255,255,255)

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

    # Inputs
    windowSizeWidth,windowSizeHeight = window.get_size()

    # Display and Graphics - Home
    window.fill((DPURPLE))
    pygame.draw.rect(window, PURPLE, (0,0,300,windowSizeHeight))
    window.blit(LOGOTEXT, (305,5))
    window.blit(SPLASH, (305,60))
    for counter in range(len(CHECKLIST)):
        window.blit(FONT.render(CHECKLIST[counter], True, WHITE), (305,100+counter*20))

    # Display and Graphics - Sidebar
    window.blit(FONT.render("Homepage", True, WHITE), (5,5))

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
