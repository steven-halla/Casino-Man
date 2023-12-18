import pygame

# Define a Rectangle class that inherits from pygame.sprite.Sprite
class Rectangle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, dx, dy, barriers, screen_width, screen_height):
        # Move each axis separately and check for collisions
        self.rect.x += dx
        self.collide(dx, 0, barriers)
        self.rect.y += dy
        self.collide(0, dy, barriers)

        # Check for screen boundaries
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
        if self.rect.top < 0:
            self.rect.top = 0

    def collide(self, dx, dy, barriers):
        # Check for collision with barriers
        for barrier in barriers:
            if self.rect.colliderect(barrier.rect):
                if dx > 0:  # Moving right; hit the left side of the barrier
                    self.rect.right = barrier.rect.left
                if dx < 0:  # Moving left; hit the right side of the barrier
                    self.rect.left = barrier.rect.right
                if dy > 0:  # Moving down; hit the top side of the barrier
                    self.rect.bottom = barrier.rect.top
                if dy < 0:  # Moving up; hit the bottom side of the barrier
                    self.rect.top = barrier.rect.bottom


# Initialize Pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Red Rectangle")

# Create instances of the Rectangle class
red_rect = Rectangle((255, 0, 0), 100, 50)
blue_rect = Rectangle((0, 0, 255), 100, 50)

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
