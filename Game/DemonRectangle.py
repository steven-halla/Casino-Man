import pygame
from .RectangleSprite import RectangleSprite
import random



class DemonRectangle(RectangleSprite):
    def __init__(self, color, width, height, speed=5, barriers=None,
                 screen_width=0, screen_height=0, other_sprites=None,
                 pink_rect=None):
        super().__init__(color, width, height, speed)
        self.pink_rect = pink_rect

        self.barriers = barriers
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.other_sprites = other_sprites  # Other sprites for interaction
        self.directions = ['up', 'down', 'left', 'right']
        self.current_direction_index = random.randint(0,
                                                      len(self.directions) - 1)
        self.colors = [(0, 0, 255), (128, 0, 128)]  # Blue and Purple
        self.current_color_index = 0
        self.next_color_change_time = pygame.time.get_ticks() + 3000


        # ... [existing __init__ and other methods] ...

    def update(self):

        current_time = pygame.time.get_ticks()
        # ... [Other update code] ...



        current_color = self.image.get_at((0, 0))
        direction = self.directions[self.current_direction_index]
        is_moving = False

        for sprite in self.other_sprites:
            if self.rect.colliderect(sprite.rect):
                self.handle_collision(sprite)

            # Proximity check and LOS not blocked
            if is_moving and current_color == (0, 0, 255):
                proximity_check = self.check_proximity_and_direction(sprite,
                                                                     direction)
                los_blocked = self.is_los_blocked(sprite)

                if proximity_check and not los_blocked:
                    sprite.change_color((0, 255, 0))  #


        current_time = pygame.time.get_ticks()
        if current_time >= self.next_color_change_time:
            self.change_color_randomly()
            self.change_direction_randomly()
            self.next_color_change_time = current_time + 3000

        current_color = self.image.get_at((0, 0))
        dx, dy = 0, 0
        direction = self.directions[self.current_direction_index]
        is_moving = False

        if current_color == (
        0, 0, 255):  # Check if the rectangle is blue
            if direction == 'up':
                dy = -self.speed
                is_moving = True
            elif direction == 'down':
                dy = self.speed
                is_moving = True
            elif direction == 'left':
                dx = -self.speed
                is_moving = True
            elif direction == 'right':
                dx = self.speed
                is_moving = True

            self.move(dx, dy, self.barriers, self.screen_width,
                      self.screen_height)

        # Check for collisions with other sprites
        for sprite in self.other_sprites:
            if self.rect.colliderect(sprite.rect):
                self.handle_collision(sprite)

            # Additional proximity-based color change logic
            red_rect = self.other_sprites[
                0]  # Assuming red_rect is the first sprite
            if sprite == red_rect and is_moving and current_color == (
            0, 0, 255):
                proximity_check = self.check_proximity_and_direction(
                    red_rect, direction)
                print(
                    f"Proximity Check: {proximity_check}, Direction: {direction}, Current Color: {current_color}")
                if proximity_check:
                    red_rect.change_color(
                        (0, 255, 0))  # Change to green



    def is_los_blocked(self, target_sprite):
        if self.pink_rect is None or not self.pink_rect.can_block_los:
            return False

        los_vector = pygame.math.Vector2(
            target_sprite.rect.centerx - self.rect.centerx,
            target_sprite.rect.centery - self.rect.centery)

        for step in range(1, 100):
            check_point = self.rect.center + los_vector * (step / 100.0)

            if self.pink_rect.rect.collidepoint(check_point.x, check_point.y):
                print("LOS is blocked at point:", check_point)
                return True

        return False

    # Logic to determine if the line of sight to target_sprite is blocked by the pink rectangle
    # This can be basic or complex depending on your game's requirements
    # For example, check if pink_rect is aligned between self and target_sprite
    # ...


    def check_proximity_and_direction(self, other_sprite, direction):
        # Fixed proximity threshold
        fixed_proximity_threshold = 240

        if self.is_los_blocked(other_sprite):
            return False

        # Calculate the horizontal and vertical distances between the center points of the sprites
        horizontal_distance = self.rect.centerx - other_sprite.rect.centerx
        vertical_distance = self.rect.centery - other_sprite.rect.centery

        # Check proximity thresholds based on direction
        if direction == 'left':
            if horizontal_distance > 0:
                return (
                    abs(horizontal_distance) <= fixed_proximity_threshold
                    and abs(vertical_distance) <= (self.rect.height // 2)
                )
        elif direction == 'right':
            if horizontal_distance < 0:
                return (
                    abs(horizontal_distance) <= fixed_proximity_threshold
                    and abs(vertical_distance) <= (self.rect.height // 2)
                )
        elif direction == 'up':
            if vertical_distance > 0:
                return (
                    abs(vertical_distance) <= fixed_proximity_threshold
                    and abs(horizontal_distance) <= (self.rect.width // 2)
                )
        elif direction == 'down':
            if vertical_distance < 0:
                return (
                    abs(vertical_distance) <= fixed_proximity_threshold
                    and abs(horizontal_distance) <= (self.rect.width // 2)
                )

        return False

    def change_color_randomly(self):
        self.current_color_index = (self.current_color_index + 1) % len(self.colors)
        new_color = self.colors[self.current_color_index]
        self.image.fill(new_color)

    def change_direction_randomly(self):
        self.current_direction_index = random.randint(0, len(self.directions) - 1)

    def handle_collision(self, other_sprite):
        # Adjust position based on the collision
        if self.rect.colliderect(other_sprite.rect):
            if self.current_direction_index == 0:  # Up
                self.rect.top = other_sprite.rect.bottom
            elif self.current_direction_index == 1:  # Down
                self.rect.bottom = other_sprite.rect.top
            elif self.current_direction_index == 2:  # Left
                self.rect.left = other_sprite.rect.right
            elif self.current_direction_index == 3:  # Right
                self.rect.right = other_sprite.rect.left

        # Additional interaction logic
        current_color = self.image.get_at((0, 0))
        if other_sprite == self.other_sprites[
            0]:  # Assuming red_rect is the first sprite in other_sprites
            if current_color == (0, 0, 255, 255):  # If the rectangle is blue
                # Check if the red rectangle is within 40 pixels in x or y based on direction
                if self.current_direction_index in [0, 1]:  # Up or Down
                    if abs(other_sprite.rect.centerx - self.rect.centerx) < 40:
                        other_sprite.change_color(
                            (0, 255, 0))  # Change to green
                elif self.current_direction_index in [2, 3]:  # Left or Right
                    if abs(other_sprite.rect.centery - self.rect.centery) < 40:
                        other_sprite.change_color(
                            (0, 255, 0))  # Change to green

        # Additional logic for interaction (e.g., change color)
        # This part depends on your specific game logic and how you want the blue rectangle to interact with other sprites