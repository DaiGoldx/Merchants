import pygame
from gameobject import GameObject
from constants import *

class City(GameObject):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, 10, 0)
