import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, name):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = (pos_x, pos_y)
        self.name = name
    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, 10, 0)
    def update(self):
        pass
    def collides_with(self, other):
        if self.position == other.position:
            return True
    def description(self):
        return (f"This is {self.name} and coords: {self.position[0]} : {self.position[1]}")
        
