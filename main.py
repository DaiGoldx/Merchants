import pygame
from constants import *
from debugdraw import draw_grid_dots, draw_UI
from gameobject import GameObject
from player import Player
from gamedata import get_clickable_tiles
from city import City

def spawn_cities():
        for x in range(0,5,1):
            city = City(RANDOM_TILES[x][0],RANDOM_TILES[x][1],"Generated City")
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
    current_player_pos = None
    abc = None
    ac = None
    ab = None
    city_test = City(200,200,"First City")
    spawn_cities()
    player = Player(70,70,"Player")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        draw_grid_dots(UNIT, screen)
        draw_UI(UNIT, screen)
        updatable.update()
        for obj in drawable:
            obj.draw(screen)
        if (current_player_pos != player.position):
            current_player_pos = player.position
            ab = None       
        for city in cities:
            if city.collides_with(player):
                if(city != current_city):
                    current_city = city
                    abc = (f"City({city.position[0]}, {city.position[1]}) collided with player")
                    ab = player.description()
                    player.gold -= 1     
        ac = (f"Players: {player.gold} gold")

        text_surface = my_font.render(abc, False, (0, 0, 0))
        screen.blit(text_surface, (22 * UNIT,0))
        text_surface2 = my_font.render(ac, False, (0, 0, 0))
        screen.blit(text_surface2, (22 * UNIT,UNIT))
        text_surface3 = my_font.render(ab, False, (0, 0, 0))
        screen.blit(text_surface3, (22 * UNIT,UNIT * 2))
        pygame.display.flip()
if __name__ == "__main__":
    main()
