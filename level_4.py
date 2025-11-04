
# imports
import pygame
import main_screen
import level_3

def run_level_4(screen):

    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Level 4")

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
    player_vel_x = 0
    player_vel_y = 0
    onground = False
    player_color = RED

# nplat properties
    nplat_width, nplat_height = 200, 20
    nplat_x = screen_width - nplat_width - border_thickness
    nplat_y = screen_height - border_thickness - 100
    nplat_color = GRAY
    draw_nplat = False

# nplat2 properties
    nplat2_width, nplat2_height = 200, 20
    nplat2_x = border_thickness
    nplat2_y = border_thickness + 200
    nplat2_color = GRAY
    draw_nplat2 = False

# portal properties
    portal_width, portal_height = 40, 60
    portal_x = nplat2_x + 5
    portal_y = nplat2_y - portal_height
    portal_color = PURPLE
    draw_portal = False

# block1 properties
    block1_width, block1_height = 20, 70
    block1_x = portal_x + portal_width + 10
    block1_y = nplat2_y - block1_height
    block1_color = GRAY
    draw_blocks = False

# block2 properties
    block2_width, block2_height = 75, 20
    block2_x = border_thickness
    block2_y = portal_y - 10 - block2_height
    block2_color = GRAY

# power1 properties
    power1_width, power1_height = 20, 20
    power1_x = border_thickness + player_width
    power1_y = screen_height - player_height
    power1_color = GREEN
    draw_power1 = False

# power2 properties
    power2_width, power2_height = 20, 20
    power2_x = nplat_x + 75
    power2_y = nplat_y - player_height
    power2_color = GREEN
    draw_power2 = False

# key properties
    key_width, key_height = 20, 40
    key_x = screen_width - border_thickness - player_width
    key_y = screen_height - player_height
    key_color = YELLOW
    draw_key = False

# jump properties
    jump_width, jump_height = 20, 20
    jump_x = key_x - 50
    jump_y = screen_height - player_height
    jump_color = YELLOW
    draw_jump = True

# Force variables
    gravity = 0.5
    jump_power = -5

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
    running = True
    clock = pygame.time.Clock()
    while running:
# Input detection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.collidepoint(event.pos):
                    main_screen.main_menu()
                if back_button.collidepoint(event.pos):
                    level_3.run_level_3(screen)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            player_vel_x = player_speed
        elif keys[pygame.K_a]:
            player_vel_x = -player_speed
        else:
            player_vel_x = 0

        if keys[pygame.K_w] and onground:
            player_vel_y = jump_power
            onground = False
        if keys[pygame.K_s]:
            player_y += player_speed
        if keys[pygame.K_ESCAPE]:
            running = False

# Apply velocity and friction
        player_x += player_vel_x
            
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
        nplat_rect = pygame.Rect(nplat_x, nplat_y, nplat_width, nplat_height)
        nplat2_rect = pygame.Rect(nplat2_x, nplat2_y, nplat2_width, nplat2_height)
        block1_rect = pygame.Rect(block1_x, block1_y, block1_width, block1_height)
        block2_rect = pygame.Rect(block2_x, block2_y, block2_width, block2_height)
        power1_rect = pygame.Rect(power1_x, power1_y, power1_width, power1_height)
        power2_rect = pygame.Rect(power2_x, power2_y, power2_width, power2_height)
        jump_rect = pygame.Rect(jump_x, jump_y, jump_width, jump_height)
        key_rect = pygame.Rect(key_x, key_y, key_width, key_height)
        portal_rect = pygame.Rect(portal_x, portal_y, portal_width, portal_height)
        menu_button = pygame.Rect(menu_x, menu_y, menu_width, menu_height)
        back_button = pygame.Rect(back_x, back_y, back_width, back_height)
        level_rect = pygame.Rect(screen_width // 2 - 100, border_thickness, 100, 100)

# nplat1_collision
        if player_rect.colliderect(nplat_rect):
            if draw_nplat:
                if player_vel_y >= 0 and player_y + player_height <= nplat_y + nplat_height and player_y + player_height > nplat_y:
                    player_y = nplat_y - player_height
                    player_vel_y = 0
                    onground = True
                # Platform from bellow
                elif player_vel_y < 0 and player_y < nplat_y + nplat_height and player_y + player_height > nplat_y + nplat_height:
                    player_y = nplat_y + nplat_height
                    player_vel_y = 0
                    onground = False

# nplat2 collision
        if player_rect.colliderect(nplat2_rect):
            if draw_nplat2:
                if player_vel_y >= 0 and player_y + player_height <= nplat2_y + nplat2_height and player_y + player_height > nplat2_y:
                    player_y = nplat2_y - player_height
                    player_vel_y = 0
                    onground = True
                # plat2 above player
                if player_vel_y < 0 and player_y < nplat2_y + nplat2_height and player_y + player_height > nplat2_y + nplat2_height:
                    player_y = nplat2_y + nplat2_height
                    player_vel_y = 0
                    onground = False

# block1 collision
        if player_rect.colliderect(block1_rect):
            if draw_blocks:
                if abs(player_rect.right - block1_rect.left) < 10 and player_vel_x > 0:
                    player_x = block1_rect.left - player_width
                if abs(player_rect.left - block1_rect.right) < 10 and player_vel_x < 0:
                    player_x = block1_rect.right
                if abs(player_rect.bottom - block1_rect.top) < 10 and player_vel_y > 0:
                    player_y = block1_rect.top - player_height
                    player_vel_y = 0
                    onground = True
                if abs(player_rect.top - block1_rect.bottom) < 10 and player_vel_y < 0:
                    player_y = block1_rect.bottom
                    player_vel_y = 0

# block2 collision
        if player_rect.colliderect(block2_rect):
            if draw_blocks:
                if abs(player_rect.right - block2_rect.left) < 10 and player_vel_x > 0:
                    player_x = block2_rect.left - player_width
                if abs(player_rect.left - block2_rect.right) < 10 and player_vel_x < 0:
                    player_x = block2_rect.right
                if abs(player_rect.bottom - block2_rect.top) < 10 and player_vel_y > 0:
                    player_y = block2_rect.top - player_height
                    player_vel_y = 0
                    onground = True
                if abs(player_rect.top - block2_rect.bottom) < 10 and player_vel_y < 0:
                    player_y = block2_rect.bottom
                    player_vel_y = 0

# jump powerup collision
        if player_rect.colliderect(jump_rect):
            if draw_jump:
                draw_jump = False
                draw_power1 = True
                jump_power = -15

# power1 collision
        if player_rect.colliderect(power1_rect):
            draw_nplat = True
            draw_power1 = False
            draw_power2 = True

# power2 collision
        if player_rect.colliderect(power2_rect):
            if draw_power2:
                draw_power2 = False
                draw_nplat2 = True
                draw_blocks = True
                draw_portal = True
                draw_key = True

# key collision
        if player_rect.colliderect(key_rect):
            if draw_key:
                draw_blocks = False
                draw_key = False
# portal collision
        if player_rect.colliderect(portal_rect):
            main_screen.main_menu()
            running = False

# Text
        menu_button_text = font.render("MENU", True, BLACK)
        back_button_text = font.render("BACK", True, BLACK)
        level_text = level_font.render("LEVEL 4", True, BLACK)

# Drawing
        screen.fill(BLUE)
# Draw border
        pygame.draw.rect(screen, GRAY, (0, 0, screen_width, screen_height), border_thickness)
# Draw nplat
        if draw_nplat:
            pygame.draw.rect(screen, nplat_color, (nplat_x, nplat_y, nplat_width, nplat_height))
# Draw nplat2
        if draw_nplat2:
            pygame.draw.rect(screen, nplat2_color, (nplat2_x, nplat2_y, nplat2_width, nplat2_height))
# Draw block1
        if draw_blocks:
            pygame.draw.rect(screen, block1_color, (block1_x, block1_y, block1_width, block1_height))
# Draw block2
        if draw_blocks:
            pygame.draw.rect(screen, block2_color, (block2_x, block2_y, block2_width, block2_height))
# Draw jump
        if draw_jump:
            pygame.draw.rect(screen, jump_color, (jump_x, jump_y, jump_width, jump_height))
# Draw power1
        if draw_power1:
            pygame.draw.rect(screen, power1_color, (power1_x, power1_y, power1_width, power1_height))
# Draw power2
        if draw_power2:
            pygame.draw.rect(screen, power2_color, (power2_x, power2_y, power2_width, power2_height))
# Draw key
        if draw_key:
            pygame.draw.rect(screen, key_color, (key_x, key_y, key_width, key_height))
# Draw portal
        if draw_portal:
            pygame.draw.rect(screen, portal_color, (portal_x, portal_y, portal_width, portal_height))
# Draw player
        pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
# Draw menu button
        pygame.draw.rect(screen, menu_color, menu_button)
        screen.blit(menu_button_text, (menu_button.x + 5, menu_button.y + 7))
# Draw back button
        pygame.draw.rect(screen, back_color, back_button)
        screen.blit(back_button_text, (back_button.x + 5, back_button.y +7))
# Draw level Text
        screen.blit(level_text, (level_rect.x + 40, level_rect.y + 10))

# Quiting
        pygame.display.flip()
        clock.tick(60)
    
