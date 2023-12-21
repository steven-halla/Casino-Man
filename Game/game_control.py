import pygame


class GameControl:
    def __init__(self, red_rect, blue_rect, pink_rect, screen_width, screen_height, speed):
        self.red_rect = red_rect
        self.blue_rect = blue_rect
        self.pink_rect = pink_rect
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = speed



    def handle_keys(self, keys):
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -self.speed
        if keys[pygame.K_RIGHT]:
            dx = self.speed
        if keys[pygame.K_UP]:
            dy = -self.speed
        if keys[pygame.K_DOWN]:
            dy = self.speed

        barriers = [self.blue_rect,
                    self.pink_rect]  # Combine into a single list

        self.red_rect.move(dx, dy,barriers, self.screen_width, self.screen_height)
