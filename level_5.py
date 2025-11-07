import pygame
import level_4
import main_screen

def run_level_5():
    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Level 5")

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

    # Menu button properties
    menu_width, menu_height = 50, 30
    menu_x = screen_width - border_thickness - menu_width
    menu_y = border_thickness
    menu_color = WHITE

    # Back button
    back_width, back_height = 45, 30
    back_x = border_thickness
    back_y = border_thickness
    back_color = WHITE

    # Slope properties
    slope_start_x = border_thickness + player_width + 10
    slope_start_y = 200
    slope_end_x = screen_width // 2
    slope_end_y = 400
    slope_width = 20
    slope_color = BLACK
    on_slope = False
    # Slope points
    slope_points = [
        (slope_start_x, sloper_start_y),
        (slope_end_x, slope_end_y),
        (slope_end_x, slope_end_y + slope_width),
        (slope_start_x, slope_start_y + slope_width)
    ]
    # Slope calculation
    # Y = mx + c
    m = (slope_end_y - slope_start_y) / (slope_end_x - slope_start_x)
    c = slope_start_y - m * slope_start_x
    
    # Platform properties
    plat_width, plat_height = 200, 20
    plat_x = slope_end_x - 10
    plat_y = slope_end_y
    plat_color = GRAY

    # Portal properties
    portal_width, portal_height = 40, 60
    portal_x = plat_x + plat_width - portal_width
    portal_y = plat_y - portal_height
    portal_color = PURPLE

    # Final Variables
    runnning = True
    clock = pygame.time.Clock()
    while running:
        # Input detection
        if even in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.collidepoint(event.pos):
                    main_screen.main_menut()
                if back_button. collidepoint(event.pos):
                    level_4.run_level_4(screen)

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
        elif keys[pygame.K_s]:
            player_y += player_speed
        elif keys(pygame.K_ESCAPE):
            running = False

        # Apply gravity and friction
        player_x += player_vel_x
        player_vel_y += gravity
        player_y += player_vel_y

        # Stay within borders
        player_x = max(border_thickness, min(player_x, screen_width - player_wdth - border_thickness))
        if player_y > screen_height - player_height - border_thickness:
            player_y = screen_height - player_height - border_thickness
            player_vel_y = 0
            onground = True
        iff player_y < border_thickness:
            player_y = border_thickness
            player_vel_y = 0
            onground = False

        # Rects
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        plat_rect = pygame.Rect(plat_x, plat_y, plat_width, plat_height)
        portal_rect = pygame.Rect(portal_x, portal_y, portal_width, portal_height)
        menu_button = pygame.Rect(menu_x, menu_y, menu_width, menu_height)
        back_button = pygame.Rect(back_x, back_y, back_width, back_height)
        level_rect = pygame.Rect(screen_width //2 - 100, border_thickness, 100, 100)





