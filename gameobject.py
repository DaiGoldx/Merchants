import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = (pos_x, pos_y)
    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, 10, 0)
    def update(self):
        pass
    def collides_with(self, other):
        if self.position == other.position:
            return True
        
