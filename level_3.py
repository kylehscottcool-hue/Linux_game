
# imports
import pygame
import main_screen
import level_2

def run_level_3(screen):
    
    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Level 3")

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


# Player properties
    player_width, player_height = 50, 50
    player_x = 100
    player_y = screen_height - player_height - border_thickness
    player_speed = 5
    player_vel_y = 0
    onground = False
    player_color = RED

# First jump platform
    plat1_width, plat1_height = 200, 20
    plat1_x = screen_width - plat1_width - border_thickness
    plat1_y = screen_height - border_thickness - 100
    plat1_color = GRAY

# Second jump platform
    plat2_width, plat2_height = 200, 20
    plat2_x = border_thickness
    plat2_y = border_thickness + 200 
    plat2_color = GRAY

# Blocking platform
    block_width, block_height = 20, 100
    block_x = screen_width - border_thickness - block_width - 50
    block_y = screen_height - block_height - border_thickness
    block_color = GRAY
    draw_block = True

# Key properties
    key_width, key_height = 20, 40
    key_x = plat2_x + 50
    key_y = plat2_y - key_height - 5
    key_color = YELLOW
    draw_key = True

# Portal properties
    portal_width, portal_height = 40, 60
    portal_x = screen_width - border_thickness - portal_width
    portal_y = screen_height - border_thickness - portal_height
    portal_color = PURPLE

# Force variables
    gravity = 0.5
    jump_power = -15

# Menu Button
    menu_width, menu_height = 50, 30
    menu_x = screen_width - border_thickness - menu_width
    menu_y = border_thickness
    menu_color = WHITE

# Back button
    back_width, back_height = 45, 30
    back_x = border_thickness
    back_y = border_thickness
    back_color = WHITE

# Final variables
    clock = pygame.time.Clock()
    running = True

# Input detection
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.collidepoint(event.pos):
                    main_screen.main_menu()
                if back_button.collidepoint(event.pos):
                    level_2.run_level_2(screen)

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
            running = False:
        if keys[pygame.K_m]:
            main_screen.main_menu()
        if keys[pygame.K_b]
            level_2.run_level_2(screen)
            
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
        plat1_rect = pygame.Rect(plat1_x, plat1_y, plat1_width, plat1_height)
        plat2_rect = pygame.Rect(plat2_x, plat2_y, plat2_width, plat2_height)
        block_rect = pygame.Rect(block_x, block_y, block_width, block_height)
        key_rect = pygame.Rect(key_x, key_y, key_width, key_height)
        portal_rect = pygame.Rect(portal_x, portal_y, portal_width, portal_height)
        menu_button = pygame.Rect(menu_x, menu_y, menu_width, menu_height)
        back_button = pygame.Rect(back_x, back_y, back_width, back_height)
        level_rect = pygame.Rect(screen_width // 2 - 100, border_thickness, 100, 100)

# plat1 collision
        if player_rect.colliderect(plat1_rect):
            # plat1 from above
            if player_vel_y >= 0 and player_y + player_height <= plat1_y + plat1_height and player_y + player_height > plat1_y:
                player_y = plat1_y - player_height
                player_vel_y = 0
                onground = True
            # Platform from bellow
            elif player_vel_y < 0 and player_y < plat1_y + plat1_height and player_y + player_height > plat1_y + plat1_height:
                player_y = plat1_y + plat1_height
                player_vel_y = 0
                onground = False

# plat2 collision
        if player_rect.colliderect(plat2_rect):
            # plat2 below player
            if player_vel_y >= 0 and player_y + player_height <= plat2_y + plat2_height and player_y + player_height > plat2_y:
                player_y = plat2_y - player_height
                player_vel_y = 0
                onground = True
            # plat2 above player
            if player_vel_y < 0 and player_y < plat2_y + plat2_height and player_y + player_height > plat2_y + plat2_height:
                player_y = plat2_y + plat2_height
                player_vel_y = 0
                onground = False

# block collision
        if player_rect.colliderect(block_rect):
            if draw_block:
                if player_speed >= 0 and player_x + player_width <= portal_x and player_x < portal_x:
                     player_x = block_x - player_width

# key collision
        if player_rect.colliderect(key_rect):
            if draw_key:
                draw_key = False
                draw_block = False

# portal collision
        if player_rect.colliderect(portal_rect):
            return True

# Text
        menu_button_text = font.render("MENU", True, BLACK)
        back_button_text = font.render("BACK", True, BLACK)
        level_text = level_font.render("LEVEL 3", True, BLACK)

# Drawing
        screen.fill(BLUE)
# Draw border
        pygame.draw.rect(screen, GRAY, (0, 0, screen_width, screen_height), border_thickness)
# Draw plat1
        pygame.draw.rect(screen, plat1_color, (plat1_x, plat1_y, plat1_width, plat1_height))
# Draw plat2
        pygame.draw.rect(screen, plat2_color, (plat2_x, plat2_y, plat2_width, plat2_height))
# Draw block
        if draw_block:
            pygame.draw.rect(screen, block_color, (block_x, block_y, block_width, block_height))
# Draw key
        if draw_key:
            pygame.draw.rect(screen, key_color, (key_x, key_y, key_width, key_height))
# Draw portal
        pygame.draw.rect(screen, portal_color, (portal_x, portal_y, portal_width, portal_height))
# Draw player
        pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
# Draw menu button
        pygame.draw.rect(screen, menu_color, menu_button)
        screen.blit(menu_button_text, (menu_button.x + 5, menu_button.y + 7))
# Draw bck button
        pygame.draw.rect(screen, back_color, back_button)
        screen.blit(back_button_text, (back_button.x + 5, back_button.y + 7))
# Draw level Text
        screen.blit(level_text, (level_rect.x + 40, level_rect.y + 10))

# Loading
        pygame.display.flip()
        clock.tick(60)
