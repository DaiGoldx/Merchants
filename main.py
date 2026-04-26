import pygame
from constants import *
from debugdraw import draw_grid_dots
from gameobject import GameObject
from player import Player
from gamedata import get_clickable_tiles
from city import City

def main():
    print("Hello from merchants!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    City.containers = (updatable, drawable)

    city_test = City(200,200)
    city_1 = City(RANDOM_TILES[0][0],RANDOM_TILES[0][1])
    city_2 = City(RANDOM_TILES[1][0],RANDOM_TILES[1][1])
    city_3 = City(RANDOM_TILES[2][0],RANDOM_TILES[2][1])
    city_4 = City(RANDOM_TILES[3][0],RANDOM_TILES[3][1])
    city_5 = City(RANDOM_TILES[4][0],RANDOM_TILES[4][1])
    test = Player(70,70)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        draw_grid_dots(UNIT, screen)
        updatable.update()
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
if __name__ == "__main__":
    main()
