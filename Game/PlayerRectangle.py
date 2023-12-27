from Game.RectangleSprite import RectangleSprite


class PlayerRectangle(RectangleSprite):
    def __init__(self, color, width, height, speed=5):
        super().__init__(color, width, height, speed)
        # Additional player-specific initialization can go here

    def update(self, game_controller, screen_width, screen_height):
        # Update the player's position based on the game controller's input
        dx, dy = 0, 0


        if game_controller.isLeftPressed:
            dx -= self.speed
        if game_controller.isRightPressed:
            dx += self.speed
        if game_controller.isUpPressed:
            dy -= self.speed
        if game_controller.isDownPressed:
            dy += self.speed

        # Basic movement update
        self.rect.x += dx
        self.rect.y += dy

        # Ensure the player stays within the screen boundaries
        self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, screen_height - self.rect.height))
