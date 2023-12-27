import pygame

from Game.RectangleSprite import RectangleSprite


class ObstacleRectangle(RectangleSprite):
    def __init__(self, width, height, color=(255, 20, 147), speed=5,
                 can_block_los=True):
        super().__init__(color, width, height, speed)
        self.can_block_los = can_block_los
        # Additional initialization for PinkRectangleSprite if needed

    # If you need specific update logic for PinkRectangleSprite, override the update method
    def update(self):
        # Add any update logic specific to the pink rectangle here if needed
        # For example, you can call self.move(dx, dy, barriers, screen_width, screen_height) to move the sprite
        pass

    # You can also override other methods from RectangleSprite or add new methods if needed
