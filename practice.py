# Example file showing a basic pygame "game loop"
# 1. IMPORT PYGAME
import pygame
from sys import exit
import random

# 2. INITIALISE PYGAME
pygame.init()

#3. DEFINE DISPLAY SURFACE
screen_width = 400
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
# rename window
pygame.display.set_caption('Runner')
# create clock
clock = pygame.time.Clock()
# Create surface
test_surface = pygame.Surface((100,200))
test_surface.fill((55, 140, 231))
# test_rect = pygame.Rect(100,200,100,100)
test_rect = test_surface.get_rect(center = (200,250))

# 4. KEEP DISPLAY RUNNING WHILE TRUE
while True:
    # 6. EVENT LOOP TO CHECK FOR USER INPUT
    for event in pygame.event.get():
        #check if event is quit
        if event.type == pygame.QUIT:
            pygame.quit()
            #close all Python code
            exit()
    # define display screen color: pygame.Color('color') or RGB tuple
    screen.fill((175,215,70))
    #draw retangle
    # pygame.draw.rect(screen, pygame.Color('red'), test_rect)
    # render surface, blit = block, image, transfer
    screen.blit(test_surface,test_rect)
    

    # 5. DRAW ALL ELEMENTS AND UPDATE DISPLAY
    pygame.display.update()

    #game runs as fast as your computer speed, to make it more consistent, set a max speed (fps)
    clock.tick(60)