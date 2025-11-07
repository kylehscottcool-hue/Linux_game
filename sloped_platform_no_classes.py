
import pygame

def run_slope_example(screen):
    pygame.init()

    # --- Constants ---
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    PLAYER_COLOR = (255, 0, 0)
    PLATFORM_COLOR = (0, 255, 0)
    BACKGROUND_COLOR = (20, 20, 40)

    # --- Player Properties ---
    player_width, player_height = 30, 50
    player_x = 100
    player_y = 200
    player_change_x = 0
    player_change_y = 0
    on_slope = False
    gravity = 0.35

    # --- Slope Properties ---
    # The slope is defined by the line between (start_x, start_y) and (end_x, end_y)
    slope_start_x = 200
    slope_start_y = 400
    slope_end_x = 600
    slope_end_y = 200

    # For drawing, we define a polygon to give the slope thickness
    slope_poly_points = [
        (slope_start_x, slope_start_y), 
        (slope_end_x, slope_end_y), 
        (slope_end_x, slope_end_y + 50), 
        (slope_start_x, slope_start_y + 50)
    ]

    # --- Slope Calculation ---
    # Calculate slope (m) and y-intercept (c) for the line equation y = mx + c
    m = (slope_end_y - slope_start_y) / (slope_end_x - slope_start_x)
    c = slope_start_y - m * slope_start_x

    # --- Game Loop ---
    clock = pygame.time.Clock()
    running = True
    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_change_x = -3
                elif event.key == pygame.K_RIGHT:
                    player_change_x = 3
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player_change_x < 0:
                    player_change_x = 0
                elif event.key == pygame.K_RIGHT and player_change_x > 0:
                    player_change_x = 0

        # --- Player Logic ---
        # Apply gravity if not on the slope
        if not on_slope:
            player_change_y += gravity

        # Move left/right
        player_x += player_change_x

        # Move up/down
        player_y += player_change_y

        # Reset slope flag for the next frame
        on_slope = False

        # Create player rect for calculations
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

        # --- Slope Collision Logic ---
        # Check if the player's center is horizontally within the slope's bounds
        if slope_start_x < player_rect.centerx < slope_end_x:
            # Calculate the y position on the slope for the player's current x
            slope_y = m * player_rect.centerx + c

            # If the player's bottom is at or just above the slope, snap them to it
            if abs(player_rect.bottom - slope_y) < 10: # Use a small tolerance
                player_y = slope_y - player_height
                player_change_y = 0  # Stop falling
                on_slope = True

        # --- Screen Boundaries ---
        if player_y > SCREEN_HEIGHT:
            player_x = 100
            player_y = 200
            player_change_y = 0

        # --- Drawing ---
        screen.fill(BACKGROUND_COLOR)

        # Draw the slope polygon
        pygame.draw.polygon(screen, PLATFORM_COLOR, slope_poly_points)

        # Draw the player
        pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, player_width, player_height))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# To run this example, you could add this to your main_screen.py or similar
if __name__ == "__main__":
    screen = pygame.display.set_mode((800, 600))
    run_slope_example(screen)
