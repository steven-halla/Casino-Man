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


pink_rect = RectangleSprite((255, 105, 180), 100, 50)  # Pink color, width 100, height 50


# Add Pink Square to sprite group

# Add Pink Square to barriers list for collision detection
barriers = [pink_rect]
last_move_time = time.time()
movement_interval = 0.000001  # For example, move every 50 milliseconds (20 times per second)

# Set initial positions
# For red_rect
red_rect.rect.x = (screen_width - red_rect.rect.width) // 2
red_rect.rect.y = (screen_height - red_rect.rect.height) // 2

# For blue_rect
blue_rect.rect.x = red_rect.rect.x - blue_rect.rect.width - 40
blue_rect.rect.y = (screen_height - blue_rect.rect.height) // 2

pink_rect.rect.x = 200  # Set the x position
pink_rect.rect.y = 300  # Set the y position


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

# Main game loop
running = True
while running:
    barriers = [pink_rect]
    dx, dy = 0, 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    elapsed_time = time.time() - start_time

    # Check if it's time to switch colors
    if time.time() >= next_color_time:
        print("hi")

        current_color = blue_rect.image.get_at((0, 0))
        if current_color == (0, 0, 255, 255):  # If the rectangle is blue
            blue_rect.change_color((128, 0, 128))  # Change it to purple
        else:
            blue_rect.change_color((0, 0, 255))  # Change it back to blue

        # Randomly choose the next direction
        current_direction_index = random.randint(0, len(directions) - 1)
        if current_color == (0, 0, 255):  # If the rectangle is blue
            next_color_time = time.time() + 3  # Set the time for the next color change to 3 seconds
        else:
            next_color_time = time.time() + 2  # Set the time for the next color change to 5 seconds

    # Movement Logic
    direction = directions[current_direction_index]
    current_color = blue_rect.image.get_at((0, 0))

    if direction == 'up':
        if blue_rect.rect.top > 0:
            if current_color == (0, 0, 255):  # If the rectangle is blue
                # Check if the red rectangle is directly above the blue rectangle
                if abs(red_rect.rect.centerx - blue_rect.rect.centerx) < 10:  # Adjust the threshold as needed
                    if red_rect.rect.bottom < blue_rect.rect.top:  # Check if red is above blue
                        # Change the color of the red rectangle to green
                        red_rect.change_color((0, 255, 0))  # Change to green
                        print("Changed red to green")
                    else:
                        print("No LOS")
                else:
                    print("No LOS")
            blue_rect.rect.y -= speed
        else:
            print("Luck you")




    elif direction == 'down':
        if blue_rect.rect.bottom < screen_height:
            if current_color == (0, 0, 255):  # If the rectangle is blue
                # Check if the red rectangle is directly below the blue rectangle
                if abs(red_rect.rect.centerx - blue_rect.rect.centerx) < 10:  # Adjust the threshold as needed
                    if red_rect.rect.top > blue_rect.rect.bottom:  # Check if red is below blue
                        # Change the color of the red rectangle to green
                        red_rect.change_color((0, 255, 0))  # Change to green
                        print("Changed red to green")
                    else:
                        print("No LOS")
                else:
                    print("No LOS")
            blue_rect.rect.y += speed  # Allowing the blue rectangle to move down
        else:
            print("Luck you")


    elif direction == 'left':
        if blue_rect.rect.left > 0:
            if current_color == (0, 0, 255):  # If the rectangle is blue
                # Check if the red rectangle is directly to the left of the blue rectangle
                if abs(red_rect.rect.centery - blue_rect.rect.centery) < 10:  # Adjust the threshold as needed
                    if red_rect.rect.right < blue_rect.rect.left:  # Check if red is to the left of blue
                        # Change the color of the red rectangle to green
                        red_rect.change_color((0, 255, 0))  # Change to green
                        print("Changed red to green")
                    else:
                        print("No LOS")
                else:
                    print("No LOS")
            blue_rect.rect.x -= speed  # Allowing the blue rectangle to move left
        else:
            print("Luck you")

    elif direction == 'right':
        if blue_rect.rect.right < screen_width:
            if current_color == (0, 0, 255):  # If the rectangle is blue
                # Check if the red rectangle is directly to the right of the blue rectangle
                if abs(red_rect.rect.centery - blue_rect.rect.centery) < 10:  # Adjust the threshold to 10 pixels
                    if red_rect.rect.left > blue_rect.rect.right:  # Check if red is to the right of blue
                        # Change the color of the red rectangle to green
                        red_rect.change_color(
                            (0, 255, 0))  # Change to green
                        print("Changed red to green")
                    else:
                        print("No LOS")
                else:
                    print("No LOS")
            blue_rect.rect.x += speed  # Allowing the blue rectangle to move right
        else:
            print("Luck you")

            # Your game loop code here (replace this comment with your game loop logic)

            # Limit the loop's execution speed, e.g., to avoid high CPU usage


    blue_rect.move(dx, dy, barriers, screen_width, screen_height)

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