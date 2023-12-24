import pygame

from Game.PinkRectangleSprite import PinkRectangleSprite
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
# pink_rect = RectangleSprite((255, 105, 180), 100, 50)  # Pink color, width 100, height 50

# blue_rect = BlueRectangleSprite((0, 0, 255), 100, 50, speed=3, barriers=[pink_rect], screen_width=screen_width, screen_height=screen_height, other_sprites=[red_rect, pink_rect])
# Create the pink rectangle instance before the blue rectangle
# pink_rect = PinkRectangleSprite(pink_width, pink_height, pink_color, pink_speed)
# Define the properties for the PinkRectangleSprite
pink_color = (255, 20, 147)  # RGB color for pink

# Create an instance of PinkRectangleSprite
pink_rect = PinkRectangleSprite(
    width=100,  # Width of the blue rectangle
    height=50,
    color=pink_color,
)

# Now create the blue rectangle and pass the pink rectangle to it
# Assuming the necessary variables are already defined and initialized:
# pink_rect = instance of PinkRectangleSprite
# red_rect = instance of another sprite class
# screen_width = width of your game screen
# screen_height = height of your game screen

# Now create the blue rectangle
blue_rect = BlueRectangleSprite(
    color=(0, 0, 255),  # Blue color
    width=100,          # Width of the blue rectangle
    height=50,          # Height of the blue rectangle
    speed=3,            # Speed of the blue rectangle
    barriers=[pink_rect],  # List containing the pink rectangle as a barrier
    screen_width=screen_width,  # Screen width
    screen_height=screen_height, # Screen height
    other_sprites=[red_rect, pink_rect],  # List containing red and pink rectangles as other sprites
    pink_rect=pink_rect  # Pink rectangle for LOS blocking
)




# Add Pink Square to sprite group

# Add Pink Square to barriers list for collision detection
barriers = [pink_rect]
last_move_time = time.time()
movement_interval = 0.000001  # For example, move every 50 milliseconds (20 times per second)

# Set initial positions
# For red_rect
# ... [previous code] ...

# Center the pink rectangle in the middle of the screen
pink_rect.rect.x = (screen_width - pink_rect.rect.width) // 2
pink_rect.rect.y = (screen_height - pink_rect.rect.height) // 2

# Position the red rectangle 20 pixels above the pink rectangle
red_rect.rect.x = pink_rect.rect.x + 50 # Align horizontally with the pink rectangle
red_rect.rect.y = pink_rect.rect.y - red_rect.rect.height - 20

# Position the blue rectangle 20 pixels below the pink rectangle
blue_rect.rect.x = pink_rect.rect.x  # Align horizontally with the pink rectangle
blue_rect.rect.y = pink_rect.rect.y + pink_rect.rect.height + 20

# ... [rest of your code] ...


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