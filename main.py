import pygame
from Game.rectanglesprite import RectangleSprite
import random
import time



from Game.game_control import GameControl

blue_movement = 444  # Total movement distance in pixels


pygame.init()

screen_width = 800
screen_height = 850
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Red Rectangle")

# Create instances of the Rectangle class
red_rect = RectangleSprite((255, 0, 0), 100, 50)
blue_rect = RectangleSprite((0, 0, 255), 100, 50)
last_move_time = time.time()
movement_interval = 0.000001  # For example, move every 50 milliseconds (20 times per second)

# Set initial positions
# For red_rect
red_rect.rect.x = (screen_width - red_rect.rect.width) // 2
red_rect.rect.y = (screen_height - red_rect.rect.height) // 2

# For blue_rect
blue_rect.rect.x = red_rect.rect.x - blue_rect.rect.width - 40
blue_rect.rect.y = (screen_height - blue_rect.rect.height) // 2


# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(red_rect)
all_sprites.add(blue_rect)

# Speed of movement
speed = 5

colors = ["blue", "purple"]
color_index = 0
next_color_time = time.time() + 3

game_control = GameControl(red_rect, blue_rect, screen_width, screen_height, speed)
clock = pygame.time.Clock()
start_time = time.time()  # Get the start time

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False



    elapsed_time = time.time() - start_time

    # Check if it's time to switch colors
    if time.time() >= next_color_time:
        color_index = (color_index + 1) % len(
            colors)  # Toggle between "blue" and "purple"
        current_color = colors[color_index]
        print(current_color)

        # Set the time for the next color change
        next_color_time = time.time() + 3






            # Your game loop code here (replace this comment with your game loop logic)

            # Limit the loop's execution speed, e.g., to avoid high CPU usage

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

    # Limit the frame rate to 30 FPS
    clock.tick(30)

# Quit Pygame
pygame.quit()