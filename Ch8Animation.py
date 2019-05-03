import pygame
from Ball import Ball
from Walls import Wall

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREENWIDTH = 700
SCREENHEIGHT = 500

pygame.init()

# Set the width and height of the screen [width, height]
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

aball = Ball(100, 100, 3, 3, 10, WHITE)
wall01 = Wall(100, 300, 10, 50, RED)

# This is a list of 'sprites.  All the walls
# The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
block_list.add(wall01)


# This is a list of every sprite.
# All walls and the ball as well.
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(aball)
all_sprites_list.add(wall01)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here

    aball.move()
    all_sprites_list.draw(screen)
   # aball.draw(screen)
   # wall01.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()


