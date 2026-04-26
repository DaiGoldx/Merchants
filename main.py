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
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    cities = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    City.containers = (cities, updatable, drawable)
    current_city = None
    abc = None
    city_test = City(200,200)
    city_1 = City(RANDOM_TILES[0][0],RANDOM_TILES[0][1])
    city_2 = City(RANDOM_TILES[1][0],RANDOM_TILES[1][1])
    city_3 = City(RANDOM_TILES[2][0],RANDOM_TILES[2][1])
    city_4 = City(RANDOM_TILES[3][0],RANDOM_TILES[3][1])
    city_5 = City(RANDOM_TILES[4][0],RANDOM_TILES[4][1])
    player = Player(70,70)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        draw_grid_dots(UNIT, screen)
        updatable.update()
        for obj in drawable:
            obj.draw(screen)
        for city in cities:
            if city.collides_with(player):
                if(city != current_city):
                    current_city = city
                    abc = (f"City({city.position[0]}, {city.position[1]}) collided with player")
        text_surface = my_font.render(abc, False, (0, 0, 0))
        screen.blit(text_surface, (22 * UNIT,0))
        pygame.display.flip()
if __name__ == "__main__":
    main()
