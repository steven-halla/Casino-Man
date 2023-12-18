import pygame
from Game.rectanglesprite import RectangleSprite

# ... rest of your main.py code ...


# ... rest of your main.py code ...



# Define a Rectangle class that inherits from pygame.sprite.Sprite

# Initialize Pygame
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

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Reset movement direction
    dx, dy = 0, 0

    # Check for key presses and set movement direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dx = -speed
    if keys[pygame.K_RIGHT]:
        dx = speed
    if keys[pygame.K_UP]:
        dy = -speed
    if keys[pygame.K_DOWN]:
        dy = speed

    # Move the red rectangle and handle collisions with the blue rectangle and screen boundaries
    red_rect.move(dx, dy, [blue_rect], screen_width, screen_height)

    # Update sprites
    all_sprites.update()

    # Draw everything
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()
# Quit Pygame
pygame.quit()
