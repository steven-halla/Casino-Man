import pygame
from Game.rectanglesprite import RectangleSprite
from Game.BlueRectangleSprite import BlueRectangleSprite
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
pink_rect = RectangleSprite((255, 105, 180), 100, 50)  # Pink color, width 100, height 50

blue_rect = BlueRectangleSprite((0, 0, 255), 100, 50, speed=3, barriers=[pink_rect], screen_width=screen_width, screen_height=screen_height, other_sprites=[red_rect, pink_rect])




# Add Pink Square to sprite group

# Add Pink Square to barriers list for collision detection
barriers = [pink_rect]
last_move_time = time.time()
movement_interval = 0.000001  # For example, move every 50 milliseconds (20 times per second)

# Set initial positions
# For red_rect
pink_rect.rect.x = (screen_width - red_rect.rect.width) // 2
pink_rect.rect.y = (screen_height - red_rect.rect.height) // 2

# For blue_rect
# ... [other code] ...

# Set the blue rectangle's position
# ... [other code] ...

# Set the blue rectangle's position
blue_rect.rect.x = 200  # Set the x position for blue rectangle
blue_rect.rect.y = 700  # Set the y position for blue rectangle

# Set the red rectangle's position to be 80 pixels above the blue rectangle on the same x-axis
red_rect.rect.x = blue_rect.rect.x
red_rect.rect.y = blue_rect.rect.y - 222

# ... [rest of your code] ...


# ... [rest of your code] ...




# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(red_rect)
all_sprites.add(blue_rect)
all_sprites.add(pink_rect)


# Speed of movement
speed = 3
stop_speed = 0


colors = ["blue", "purple"]
color_index = 0
next_color_time = time.time() + 3

game_control = GameControl(red_rect, blue_rect, pink_rect, screen_width, screen_height, speed)
clock = pygame.time.Clock()
start_time = time.time()  # Get the start time
directions = ['up', 'down', 'left', 'right']
current_direction_index = 0  # Start with the first direction in the array
loop_counter = 0

# Main game loop
running = True
while running:
    dx, dy = 0, 0
    current_time = time.time()  # Get the current time in seconds

    elapsed_time = current_time - start_time  # Calculate elapsed time

    loop_counter += 1  # Increment the counter



    barriers = [pink_rect]


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    elapsed_time = time.time() - start_time



    keys = pygame.key.get_pressed()
    game_control.handle_keys(keys)

    # Update sprites
    for sprite in all_sprites:
        sprite.update()

    # Draw everything
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 30 FPS
    clock.tick(30)

# Quit Pygame
pygame.quit()