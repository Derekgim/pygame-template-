import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

# Create a Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Object Variables
player = pygame.Rect((50, 50, 100, 100))


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Clear the screen
    screen.fill((0, 0, 0))
    
    #Object Render
    pygame.draw.rect(screen, ("green"), player)

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()