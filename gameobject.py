import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.position = (pos_x, pos_y)
    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, 10, 0)
    def update(self):
        mouse_buttom = pygame.mouse.get_pressed()[0]
        if(mouse_buttom == True):
            self.position = pygame.mouse.get_pos()
        
