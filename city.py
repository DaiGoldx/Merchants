import pygame
from gameobject import GameObject
from constants import *

class City(GameObject):
    def __init__(self, pos_x, pos_y, name):
        super().__init__(pos_x, pos_y, name)
    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, 10, 0)

        