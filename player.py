import pygame
from gameobject import GameObject
from constants import *


class Player(GameObject):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
    def in_area(self, x_1, y_1, x_2, y_2):
        return (
            self.position[0] >= x_1
            and self.position[0] <= x_2
            and self.position[1] >= y_1
            and self.position[1] <= y_2
        )       
    def update(self):
        mouse_buttom1 = pygame.mouse.get_pressed()[0]
        if(mouse_buttom1 == True):
            self.position = pygame.mouse.get_pos()
            for tile in CLICKABLE_TILES:
                if(self.in_area(tile[0] - 20, tile[1] - 20, tile[0] + 20, tile[1] + 20)):
                   self.position = tile



            
        