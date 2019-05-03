import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, width=0, height=0, color=[255,255,255]):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # --- Class Attributes ---
        # Wall position
        self.x = x
        self.y = y

        # Wall's width/height
        self.width = width
        self.height = height

        # Wall color
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])