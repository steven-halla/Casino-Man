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


game_control = GameControl(red_rect, blue_rect, screen_width, screen_height, speed)
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if blue_movement > 0 and (time.time() - last_move_time) > movement_interval:
        blue_rect.rect.y -= speed  # Move up by the global speed
        blue_movement -= speed  # Decrement the remaining movement distance
        last_move_time = time.time()

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
