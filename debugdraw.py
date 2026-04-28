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
            


    pygame.draw.rect(screen, "white", (SCREEN_WIDTH - 10 * UNIT, 0, SCREEN_WIDTH, SCREEN_HEIGHT)) # PLAYER SHEET
    pygame.draw.circle(screen, "white", (1 + (SCREEN_WIDTH - 10 * UNIT) / 2, 1 + SCREEN_HEIGHT / 2), 10, 0) # CENTER MAP DOT
    
def draw_UI(UNIT, screen):
    pygame.draw.rect(screen, "black", (22.5 * UNIT, 0.5 * UNIT, 3 * UNIT, 3 * UNIT)) # avatar space
    pygame.draw.rect(screen, "black", (26 * UNIT, 0.5 * UNIT, 5.5 * UNIT, 3 * UNIT)) # Welcome msg space

    pygame.draw.rect(screen, "blue", (22.5 * UNIT, 4 * UNIT, 9 * UNIT, 2 * UNIT)) # log space

    pygame.draw.rect(screen, "green", (22.5 * UNIT, 6.5 * UNIT, 4 * UNIT, UNIT)) # city name
    pygame.draw.rect(screen, "green", (27.5 * UNIT, 6.5 * UNIT, 4 * UNIT, UNIT)) # city gold
    pygame.draw.rect(screen, "red", (26.75 * UNIT, 6.75 * UNIT, 0.5 * UNIT, 0.5 * UNIT)) # useless buttom to log

    #City Trade
    pygame.draw.rect(screen, "purple", (22.5 * UNIT, 8 * UNIT, 4 * UNIT, 0.5 * UNIT)) # item1 name
    pygame.draw.rect(screen, "red", (26.5 * UNIT, 8 * UNIT, UNIT, 0.5 * UNIT)) # item1 amount available
    pygame.draw.rect(screen, "blue", (27.5 * UNIT, 8 * UNIT, UNIT, 0.5 * UNIT)) # item1 price
    pygame.draw.rect(screen, "red", (29 * UNIT, 8 * UNIT, UNIT, 0.5 * UNIT)) # desired amount
    pygame.draw.rect(screen, "pink", (30 * UNIT, 8 * UNIT, UNIT, 0.5 * UNIT)) # amount x price
    pygame.draw.rect(screen, "black", (31 * UNIT, 8 * UNIT,  0.5 *UNIT, 0.5 * UNIT)) #buy buttom

    pygame.draw.rect(screen, "purple", (22.5 * UNIT, 9 * UNIT, 4 * UNIT, 0.5 * UNIT)) # item2 name
    pygame.draw.rect(screen, "red", (26.5 * UNIT, 9 * UNIT, UNIT, 0.5 * UNIT)) # item2 amount available
    pygame.draw.rect(screen, "blue", (27.5 * UNIT, 9 * UNIT, UNIT, 0.5 * UNIT)) # item2 price
    pygame.draw.rect(screen, "red", (29 * UNIT, 9 * UNIT, UNIT, 0.5 * UNIT)) # desired amount
    pygame.draw.rect(screen, "pink", (30 * UNIT, 9 * UNIT, UNIT, 0.5 * UNIT)) # amount x price
    pygame.draw.rect(screen, "black", (31 * UNIT, 9 * UNIT,  0.5 *UNIT, 0.5 * UNIT)) #buy buttom

    pygame.draw.rect(screen, "purple", (22.5 * UNIT, 10 * UNIT, 4 * UNIT, 0.5 * UNIT)) # item3 name
    pygame.draw.rect(screen, "red", (26.5 * UNIT, 10 * UNIT, UNIT, 0.5 * UNIT)) # item3 amount available
    pygame.draw.rect(screen, "blue", (27.5 * UNIT, 10 * UNIT, UNIT, 0.5 * UNIT)) # item3 price
    pygame.draw.rect(screen, "red", (29 * UNIT, 10 * UNIT, UNIT, 0.5 * UNIT)) # desired amount
    pygame.draw.rect(screen, "pink", (30 * UNIT, 10 * UNIT, UNIT, 0.5 * UNIT)) # amount x price
    pygame.draw.rect(screen, "black", (31 * UNIT, 10 * UNIT,  0.5 *UNIT, 0.5 * UNIT)) #buy buttom

    pygame.draw.rect(screen, "red", (29 * UNIT, 11 * UNIT, UNIT, 0.5 * UNIT)) # total price
    pygame.draw.rect(screen, "black", (30 * UNIT, 11 * UNIT, 1.5 * UNIT, 0.5 * UNIT)) # buy all buttom

    #Player Trade
    pygame.draw.rect(screen, "purple", (22.5 * UNIT, 14 * UNIT, 4 * UNIT, 0.5 * UNIT)) # item1 name
    pygame.draw.rect(screen, "red", (26.5 * UNIT, 14 * UNIT, UNIT, 0.5 * UNIT)) # item1 amount available
    pygame.draw.rect(screen, "blue", (27.5 * UNIT, 14 * UNIT, UNIT, 0.5 * UNIT)) # item1 price
    pygame.draw.rect(screen, "red", (29 * UNIT, 14 * UNIT, UNIT, 0.5 * UNIT)) # desired amount
    pygame.draw.rect(screen, "pink", (30 * UNIT, 14 * UNIT, UNIT, 0.5 * UNIT)) # amount x price
    pygame.draw.rect(screen, "black", (31 * UNIT, 14 * UNIT,  0.5 *UNIT, 0.5 * UNIT)) #sell buttom

    pygame.draw.rect(screen, "purple", (22.5 * UNIT, 15 * UNIT, 4 * UNIT, 0.5 * UNIT)) # item2 name
    pygame.draw.rect(screen, "red", (26.5 * UNIT, 15 * UNIT, UNIT, 0.5 * UNIT)) # item2 amount available
    pygame.draw.rect(screen, "blue", (27.5 * UNIT, 15 * UNIT, UNIT, 0.5 * UNIT)) # item2 price
    pygame.draw.rect(screen, "red", (29 * UNIT, 15 * UNIT, UNIT, 0.5 * UNIT)) # desired amount
    pygame.draw.rect(screen, "pink", (30 * UNIT, 15 * UNIT, UNIT, 0.5 * UNIT)) # amount x price
    pygame.draw.rect(screen, "black", (31 * UNIT, 15 * UNIT,  0.5 *UNIT, 0.5 * UNIT)) #sell buttom

    pygame.draw.rect(screen, "purple", (22.5 * UNIT, 16 * UNIT, 4 * UNIT, 0.5 * UNIT)) # item3 name
    pygame.draw.rect(screen, "red", (26.5 * UNIT, 16 * UNIT, UNIT, 0.5 * UNIT)) # item3 amount available
    pygame.draw.rect(screen, "blue", (27.5 * UNIT, 16 * UNIT, UNIT, 0.5 * UNIT)) # item3 price
    pygame.draw.rect(screen, "red", (29 * UNIT, 16 * UNIT, UNIT, 0.5 * UNIT)) # desired amount
    pygame.draw.rect(screen, "pink", (30 * UNIT, 16 * UNIT, UNIT, 0.5 * UNIT)) # amount x price
    pygame.draw.rect(screen, "black", (31 * UNIT, 16 * UNIT,  0.5 *UNIT, 0.5 * UNIT)) #sell buttom

    pygame.draw.rect(screen, "red", (29 * UNIT, 17 * UNIT, UNIT, 0.5 * UNIT)) # total price
    pygame.draw.rect(screen, "black", (30 * UNIT, 17 * UNIT, 1.5 * UNIT, 0.5 * UNIT)) # sell all buttom

    pygame.draw.rect(screen, "green", (22.5 * UNIT, 12.5 * UNIT, 4 * UNIT, UNIT)) # city name
    pygame.draw.rect(screen, "green", (27.5 * UNIT, 12.5 * UNIT, 4 * UNIT, UNIT)) # player name
    pygame.draw.rect(screen, "red", (26.75 * UNIT, 12.75 * UNIT, 0.5 * UNIT, 0.5 * UNIT)) # useless buttom to log

