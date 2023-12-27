import pygame

class RectangleSprite(pygame.sprite.Sprite):
    # def __init__(self, color, width, height):
    #     super().__init__()
    #     self.image = pygame.Surface([width, height])
    #     self.image.fill(color)
    #     self.rect = self.image.get_rect()

    def __init__(self, color, width, height, speed=5):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = speed  #
        self.stop_speed = 0  # New stop_speed attribute



    def move(self, dx, dy, barriers, screen_width, screen_height):
        # Move each axis separately and check for collisions
        self.rect.x += dx
        self.collide(dx, 0, barriers)
        self.rect.y += dy
        self.collide(0, dy, barriers)

        if dx == 0 and dy == 0:
            return

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

    def change_color(self, new_color):
        self.image.fill(new_color)

    def change_direction(self, new_direction):
        self.direction = new_direction
