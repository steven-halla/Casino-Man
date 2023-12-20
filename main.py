import pygame
from Game.rectanglesprite import RectangleSprite
import random


from Game.game_control import GameControl



pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Red Rectangle")

# Create instances of the Rectangle class
red_rect = RectangleSprite((255, 0, 0), 100, 50)
blue_rect = RectangleSprite((0, 0, 255), 100, 50)

# Set initial positions
red_rect.rect.x = (screen_width - red_rect.rect.width) // 2
red_rect.rect.y = (screen_height - red_rect.rect.height) // 2
blue_rect.rect.x = red_rect.rect.x - blue_rect.rect.width - 40
blue_rect.rect.y = red_rect.rect.y

# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(red_rect)
all_sprites.add(blue_rect)

# Speed of movement
speed = 1


game_control = GameControl(red_rect, blue_rect, screen_width, screen_height, speed)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    blue_los_left = blue_rect.rect.left
    blue_los_right = blue_rect.rect.right
    blue_los_top = blue_rect.rect.top

    # Check if the red rectangle is within the LOS area and above the blue rectangle
    if blue_los_left < red_rect.rect.centerx < blue_los_right and red_rect.rect.bottom < blue_los_top:
        red_rect.change_color(
            (0, 255, 0))  # Change to green if within LOS and above
    else:
        red_rect.change_color((255, 0, 0))



        # Check for key presses and delegate to game control
    keys = pygame.key.get_pressed()
    game_control.handle_keys(keys)

    # Update sprites
    all_sprites.update()

    # Draw everything
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()
# Quit Pygame
pygame.quit()
