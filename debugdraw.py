import pygame
from constants import *

def draw_grid_dots(UNIT, screen):
    for x in range(UNIT, SCREEN_WIDTH - 10 * UNIT, UNIT):
        pygame.draw.line(screen, "blue", (x, UNIT), (x, SCREEN_HEIGHT - UNIT))
    for y in range(UNIT, SCREEN_WIDTH - 10 * UNIT, UNIT):
        pygame.draw.line(screen, "blue", (UNIT, y), (SCREEN_WIDTH - 11  *UNIT, y))
    for x in range(UNIT, SCREEN_WIDTH - 10 * UNIT, UNIT):
        for y in range(UNIT, SCREEN_HEIGHT, UNIT):
            pygame.draw.circle(screen, "yellow", (x + 1, y + 1), 1, 0)
    pygame.draw.rect(screen, "white", (SCREEN_WIDTH - 10 * UNIT, 0, SCREEN_WIDTH, SCREEN_HEIGHT)) # 
    pygame.draw.circle(screen, "white", (1 + (SCREEN_WIDTH - 10 * UNIT) / 2, 1 + SCREEN_HEIGHT / 2), 10, 0) # CENTER MAP DOT
    pygame.draw.rect(screen, "red", (0, 0, SCREEN_WIDTH - 10 * UNIT, SCREEN_HEIGHT), UNIT, 0) # MAP BOUNDARIES
