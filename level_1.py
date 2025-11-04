import pygame
import level_2
import main_screen

def run_level_1(screen):

    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Level 1")

# Colors
    WHITE = ('#ADF5FF')
    BLACK = ('#13293D')
    GRAY = ('#8F9491')
    GREEN = ('#104911')
    BLUE = ('#1B98E0')
    RED = ('#D55672')
    YELLOW = ('#FFD449')
    PURPLE = ('#13293D')

# Border
    border_thickness = 5
    border_color = GRAY

# Font
    font = pygame.font.Font(None, 20)
    level_font = pygame.font.Font(None, 50)

# Menu Button
    menu_width, menu_height = 50, 30
    menu_x = screen_width - border_thickness - menu_width
    menu_y = border_thickness
    menu_color = WHITE

# Platform properties (unmovable rectangle)
    platform_width = screen_width // 2
    platform_height = 20
    platform_x = screen_width - platform_width - border_thickness
    platform_y = screen_height - platform_height - 100 - border_thickness
    platform_color = GRAY

# Player properties
    player_width, player_height = 50, 50
    player_x = 100
    player_y = screen_height - player_height - border_thickness
    player_speed = 5
    player_vel_y = 0
    onground = False
    player_color = RED

# Jump powerup properties
    jump_width, jump_height = 20, 20
    jump_x = platform_x + 100
    jump_y = platform_y + player_height
    jump_color = YELLOW
    draw_jump = True
    jump_active = False


# Force variables
    gravity = 0.5
    jump_power = -5

# Portal properties
    portal_width = 40
    portal_height = 60
    portal_x = platform_x + platform_width - portal_width
    portal_y = platform_y - portal_height
    portal_color = PURPLE

    clock = pygame.time.Clock()
    running = True

    while running:

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.collidepoint(event.pos):
                    main_screen.main_menu()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            player_x += player_speed
        if keys[pygame.K_a]:
            player_x -= player_speed
        if keys[pygame.K_w] and onground:
            player_vel_y = jump_power
            onground = False
        if keys[pygame.K_s]:
            player_y += player_speed
        if keys[pygame.K_ESCAPE]:
            running = False
        
        # Apply gravity
        player_vel_y += gravity
        player_y += player_vel_y



        # Stay within borders
        player_x = max(border_thickness, min(player_x, screen_width - player_width - border_thickness))
        if player_y > screen_height - player_height - border_thickness:
            player_y = screen_height - player_height - border_thickness
            player_vel_y = 0
            onground = True
        if player_y < border_thickness:
            player_y = border_thickness
            player_vel_y = 0
            onground = False

        # Rects
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        platform_rect = pygame.Rect(platform_x, platform_y, platform_width, platform_height)
        portal_rect = pygame.Rect(portal_x, portal_y, portal_width, portal_height)
        jump_rect = pygame.Rect(jump_x, jump_y, jump_width, jump_height)
        menu_button = pygame.Rect(menu_x, menu_y, menu_width, menu_height)
        level_rect = pygame.Rect(screen_width // 2 - 100, border_thickness, 100, 100)

        # Platform collision logic
        if player_rect.colliderect(platform_rect):
            # Land on platform from above
            if player_vel_y >= 0 and player_y + player_height <= platform_y + platform_height and player_y + player_height > platform_y:
                player_y = platform_y - player_height
                player_vel_y = 0
                onground = True
            # Hit head on platform from below
            elif player_vel_y < 0 and player_y < platform_y + platform_height and player_y + player_height > platform_y + platform_height:
                player_y = platform_y + platform_height
                player_vel_y = 0
                onground = False

        # Check for portal collision
        if player_rect.colliderect(portal_rect):
            return True

        # Check for jump powerup collision
        if player_rect.colliderect(jump_rect) and draw_jump:
            draw_jump = False
            jump_active = True
            jump_power = -18

        # Text
        menu_button_text = font.render("MENU", True, BLACK)
        level_text = level_font.render("LEVEL 1", True, BLACK)
            
        # Drawing
        screen.fill(BLUE)
        # Draw border
        pygame.draw.rect(screen, GRAY, (0, 0, screen_width, screen_height), border_thickness)
        # Draw platform
        pygame.draw.rect(screen, platform_color, (platform_x, platform_y, platform_width, platform_height))
        # Draw portal
        pygame.draw.rect(screen, portal_color, (portal_x, portal_y, portal_width, portal_height))
        # Draw player
        pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
        # Draw menu button
        pygame.draw.rect(screen, menu_color, menu_button)
        screen.blit(menu_button_text, (menu_button.x + 5, menu_button.y + 7))
        # Draw level Text
        screen.blit(level_text, (level_rect.x + 40, level_rect.y + 10))
        # Draw jump powerup
        if draw_jump:
            pygame.draw.rect(screen, jump_color, (jump_x, jump_y, jump_width, jump_height))
        pygame.display.flip()
        clock.tick(60)
