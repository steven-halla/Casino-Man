import pygame

from Game.GameController import GameController
from Game.ObstacleRectangle import ObstacleRectangle
from Game.PlayerRectangle import PlayerRectangle
from Game.RectangleSprite import RectangleSprite
import random
import time




blue_movement = 444  # Total movement distance in pixels


pygame.init()

screen_width = 800
screen_height = 850
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Red Rectangle")
# Create an instance of PlayerRectangle instead of RectangleSprite
player_rect = PlayerRectangle((255, 0, 0), 16, 16, speed=3)

# Set the initial position of player_rect
center_x = screen_width // 2
center_y = screen_height // 2
player_rect.rect.x = center_x - (player_rect.rect.width // 2)
player_rect.rect.y = center_y - (player_rect.rect.height // 2)

# Create and position obstacle_rect as before
obstacle_rect = ObstacleRectangle(100, 50)  # Width and height of obstacle
obstacle_rect.rect.x = player_rect.rect.x  # Align horizontally with player
obstacle_rect.rect.y = player_rect.rect.y + player_rect.rect.height + 50

# Add both player_rect and obstacle_rect to the all_sprites group
all_sprites = pygame.sprite.Group()
all_sprites.add(player_rect)
all_sprites.add(obstacle_rect)


speed = 3
stop_speed = 0
color_index = 0
next_color_time = time.time() + 3

clock = pygame.time.Clock()
start_time = time.time()  # Get the start time
loop_counter = 0
game_control = GameController()

# Main game loop
running = True
while running:
    # Handle events through GameController
    game_control.update()

    # Exit if necessary
    if game_control.isExitPressed:
        running = False

    for sprite in all_sprites:
        if isinstance(sprite, PlayerRectangle):
            sprite.update(game_control, screen_width, screen_height)
        else:
            sprite.update()

    loop_counter += 1  # Increment the counter


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    elapsed_time = time.time() - start_time



    keys = pygame.key.get_pressed()

    # Update sprites
    game_control.update()

    # Update player rectangle
    for sprite in all_sprites:
        if isinstance(sprite, PlayerRectangle):
            sprite.update(game_control, screen_width, screen_height)

    # Draw everything
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 30 FPS
    clock.tick(30)

# Quit Pygame
pygame.quit()