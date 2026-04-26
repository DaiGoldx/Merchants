import pygame
from constants import *
from debugdraw import draw_grid_dots
from gameobject import GameObject

def main():
    print("Hello from merchants!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    test = GameObject(70,70)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        draw_grid_dots(UNIT, screen)
        test.update()
        test.draw(screen)
        pygame.display.flip()
if __name__ == "__main__":
    main()
