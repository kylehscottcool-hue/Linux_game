import pygame

def run_level_2(screen):
    screen_width, screen_height = screen.get_size()


#Border thickness
    border_thickness= 5


#Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    PURPLE = (160, 32, 240)


# Platform properties (Non_moving)
    platform_width = 200
    platform_height = 20
    platform_x = screen_width - platform_width - border_thickness + 100
    platform_y = screen_height - border_thickness - 100
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
    jump_y = platform_y + platform_height + 25
    jump_x = platform_x + 45
    jump_active = False
    jump_color = YELLOW
    draw_jump = True

# New platform powerup properties
    nplat_width, nplat_height = 20, 20
    nplat_y = platform_y - platform_height - player_height
    nplat_x = platform_x + 50
    nplat_active = False
    nplat_color = GREEN
    draw_nplat_powerup = True

# Portal properties
    portal_width, portal_height = 40, 60
    portal_x = 50
    portal_y = screen_height - border_thickness - 450
    portal_color = PURPLE

# Force variables
    gravity = 0.5
    jump_power = -5

    clock = pygame.time.Clock()
    running = True 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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

        
        # Gravity application
        player_vel_y += gravity
        player_y += player_vel_y

        # Rects
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        platform_rect = pygame.Rect(platform_x, platform_y, platform_width, platform_height)
        jump_rect = pygame.Rect(jump_x, jump_y, jump_width, jump_height)
        nplat_rect = pygame.Rect(nplat_x, nplat_y, nplat_width, nplat_height)
        portal_rect = pygame.Rect(portal_x, portal_y, portal_width, portal_height)

        # Stay within border_thickness
        player_x = max(border_thickness, min(player_x, screen_width - player_width - border_thickness))
        if player_y > screen_height - player_height - border_thickness:
            player_y = screen_height - player_height - border_thickness
            player_vel_y = 0
            onground = True
        elif player_y < border_thickness:
            player_y = border_thickness
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

        # Check for nplat powerup collision
        if player_rect.colliderect(nplat_rect):
            draw_nplat_powerup = False
            nplat_active = True
            platform_width = screen_width //2
            platform_x = screen_width //2
        # Platform collision logic
        if player_rect.colliderect(platform_rect):
            # Platform from above
            if player_vel_y >= 0 and player_y + player_height <= platform_y + platform_height and player_y + player_height > platform_y:
                player_y = platform_y -  player_height
                player_vel_y = 0
                onground = True
            # Platform from YELLOW
            elif player_vel_y < 0 and player_y < platform_y + platform_height and player_y + player_height > platform_y + platform_height:
                player_y = platform_y + platform_height
                player_vel_y = 0
                onground = False

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
        # Draw jump powerup
        if draw_jump:
            pygame.draw.rect(screen, jump_color, (jump_x, jump_y, jump_width, jump_height))
        # Draw nplat powerup
        if draw_nplat_powerup:
            pygame.draw.rect(screen, nplat_color, (nplat_x, nplat_y, nplat_width, nplat_height))


        pygame.display.flip()
        clock.tick(60)


