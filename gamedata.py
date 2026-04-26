import random
from constants import *

clickable_list = []
random_list = []
def get_clickable_tiles(UNIT, SCREENX, SCREENY):
    for x in range(UNIT, SCREENX - 10 * UNIT, UNIT):
        for y in range(UNIT, SCREENY, UNIT):
            clickable_list.append((x,y))
    return clickable_list
def get_random_location(CLICKABLE_TILES):
    random_list.extend(random.sample(CLICKABLE_TILES, k=5))
    return random_list