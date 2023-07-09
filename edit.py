# Imports
import pygame

# Pygame Initialization
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
pygame.display.set_caption("Void Engine prerelease editor")
pygame.display.set_icon(pygame.image.load("shared/icon.png"))

# Variables
running = True

# Pre-defined Variables
PURPLE = (210,0,252)
DPURPLE = (168,0,235)
WHITE = (255,255,255)

LOGOFONT = pygame.font.Font("shared/Ubuntu-Bold.ttf", 50)
LOGOTEXT = LOGOFONT.render("Void Engine prerelease editor", True, WHITE)
FONT = pygame.font.Font("shared/Ubuntu-Medium.ttf", 20)
SPLASH = FONT.render("Void Engine prerelease still needs a lot of work.", True, WHITE)
CHECKLIST = [
    "Editor:",
    "x User Interface (sidebars, levelgrid)",
    "x Game Creation (creating the directories and gameinfo)",
    "x Importing Assets (sprites, backgrounds, music, etcetra)",
    "x Placing Sprites & Entities",
    "x Saving and Loading Levels",
    "x Modifying Game Info (startmaps, weapons, external alias)",
    "",
    "Client:",
    "x Game Loading (loading sprites, levels, gameinfo)",
    "x User Interface (title screen, ingame ui)",
    "x Client Logic (movement, weapons)",
    "x Debug Console (load maps, noclip, all that)"
]

# Main Loop
while running:

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Inputs
    windowSizeWidth,windowSizeHeight = window.get_size()

    # Display and Graphics
    window.fill((DPURPLE))
    pygame.draw.rect(window, PURPLE, (0,0,300,windowSizeHeight))
    window.blit(LOGOTEXT, (305,5))
    window.blit(SPLASH, (305,60))
    for counter in range(len(CHECKLIST)):
        window.blit(FONT.render(CHECKLIST[counter], True, WHITE), (305,100+counter*20))
    pygame.display.update()
pygame.quit()