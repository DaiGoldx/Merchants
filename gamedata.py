import pygame
from constants import *
clickable_list = []
def get_clickable_tiles():
    for y in range(UNIT, SCREEN_WIDTH - 10 * UNIT, UNIT):
        for x in range(UNIT, SCREEN_HEIGHT, UNIT):
            clickable_list.append((x,y))
    return clickable_list