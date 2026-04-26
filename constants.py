from gamedata import get_clickable_tiles, get_random_location

#Screen constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
UNIT = 40
CLICKABLE_TILES = get_clickable_tiles(UNIT, SCREEN_WIDTH, SCREEN_HEIGHT)
RANDOM_TILES = get_random_location(CLICKABLE_TILES)

#Players constants
STARTING_GOLD = 100