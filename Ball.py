import pygame

SCREENWIDTH = 700
SCREENHEIGHT = 500

class Ball(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, dx=0, dy=0, size=0, color=[255,255,255]):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # --- Class Attributes ---
        # Ball position
        self.x = x
        self.y = y

        # Ball's vector
        self.dir_x = dx
        self.dir_y = dy

        # Ball size
        self.size = size

        # Ball Image
        self.image = pygame.Surface([size, size])

        # Ball color
        self.color = color

    # --- Class Methods ---
    def move(self):
        self.x += self.dir_x
        self.y += self.dir_y
        if self.x + self.size > SCREENWIDTH or self.x < 5:  self.dir_x *= -1
        if self.y + self.size > SCREENHEIGHT or self.y < 5:  self.dir_y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)