import pygame
from constants import *

def draw_grid_dots(UNIT, screen):
    pygame.draw.rect(screen, "red", (0, 0, SCREEN_WIDTH - 10 * UNIT, SCREEN_HEIGHT), int(UNIT/2), 0) # MAP BOUNDARIES

    for x in range(UNIT, SCREEN_WIDTH - 10 * UNIT, UNIT):
        pygame.draw.line(screen, "blue", (x, UNIT), (x, SCREEN_HEIGHT - UNIT))
    for y in range(UNIT, SCREEN_WIDTH - 10 * UNIT, UNIT):
        pygame.draw.line(screen, "blue", (UNIT, y), (SCREEN_WIDTH - 11  *UNIT, y)) # grid with locations centers

    for x in range(int(UNIT/2), SCREEN_WIDTH - 10 * UNIT, UNIT):
        pygame.draw.line(screen, "purple", (x, int(UNIT / 2)), (x, SCREEN_HEIGHT - int(UNIT / 2)))
    for y in range(int(UNIT/2), SCREEN_WIDTH - 10 * UNIT, UNIT):
        pygame.draw.line(screen, "purple", (int(UNIT / 2), y), (SCREEN_WIDTH - 10.5 * UNIT, y)) # clickable area per location

    for x in range(UNIT, SCREEN_WIDTH - 10 * UNIT, UNIT):
        for y in range(UNIT, SCREEN_HEIGHT, UNIT):
            pygame.draw.circle(screen, "yellow", (x + 1, y + 1), 1, 0) #location centers

    pygame.draw.rect(screen, "white", (SCREEN_WIDTH - 10 * UNIT, 0, SCREEN_WIDTH, SCREEN_HEIGHT)) # PPLAYER SHEET
    pygame.draw.circle(screen, "white", (1 + (SCREEN_WIDTH - 10 * UNIT) / 2, 1 + SCREEN_HEIGHT / 2), 10, 0) # CENTER MAP DOT
    
