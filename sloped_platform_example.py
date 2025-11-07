
import pygame

pygame.init()

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_COLOR = (255, 0, 0)
PLATFORM_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (20, 20, 40)

# --- Player ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 50])
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 200
        self.change_x = 0
        self.change_y = 0
        self.on_slope = False

    def update(self):
        # Gravity
        if not self.on_slope:
            self.change_y += 0.35

        # Move left/right
        self.rect.x += self.change_x

        # Move up/down
        self.rect.y += self.change_y

        # Reset for next frame
        self.on_slope = False

# --- Slope ---
class Slope(pygame.sprite.Sprite):
    def __init__(self, points):
        super().__init__()
        self.points = points
        # Create a polygon for drawing
        self.image = pygame.Surface([max(p[0] for p in points), max(p[1] for p in points)], pygame.SRCALPHA)
        pygame.draw.polygon(self.image, PLATFORM_COLOR, [(p[0] - points[0][0], p[1] - points[0][1]) for p in points])
        self.rect = self.image.get_rect(topleft=points[0])

        # Slope line properties
        self.start_x = points[0][0]
        self.end_x = points[1][0]
        self.start_y = points[0][1]
        self.end_y = points[1][1]

        # Calculate slope (m) and y-intercept (c) for the top line of the slope
        self.m = (self.end_y - self.start_y) / (self.end_x - self.start_x)
        self.c = self.start_y - self.m * self.start_x

    def collide_with_player(self, player):
        # Check if the player is within the horizontal bounds of the slope
        if self.start_x < player.rect.centerx < self.end_x:
            # Calculate the y position on the slope for the player's x
            slope_y = self.m * player.rect.centerx + self.c

            # If the player is on or just above the slope, snap them to it
            if abs(player.rect.bottom - slope_y) < 10: # A small tolerance
                player.rect.bottom = slope_y
                player.change_y = 0 # Stop falling
                player.on_slope = True


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sloped Platform Example")

    player = Player()
    
    # Define the slope polygon (top-left, top-right, bottom-right, bottom-left)
    # The actual slope is between the first two points
    slope_points = [(200, 400), (600, 200), (600, 250), (200, 450)]
    slope = Slope(slope_points)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player, slope)

    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.change_x = -3
                elif event.key == pygame.K_RIGHT:
                    player.change_x = 3
                elif event.key == pygame.K_UP and not player.on_slope:
                    player.change_y = -8 # Simple jump
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.change_x = 0
                elif event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.change_x = 0

        # Update
        player.update()
        slope.collide_with_player(player)

        # --- Prevent falling off screen ---
        if player.rect.top > SCREEN_HEIGHT:
            player.rect.x = 100
            player.rect.y = 200
            player.change_y = 0

        # --- Drawing ---
        screen.fill(BACKGROUND_COLOR)
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
