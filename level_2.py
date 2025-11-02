import pygame


pygame.init()

#Screen dimensions
screen_width, screen_height = 640, 480
screen = pygame.display.set_mod((screen_width, screen_height))
pygame.display.set_caption("Help MEEEEEEEEE")


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
platform_width = screen_width // 3
platform_height = 20
platform_x = screen_width - platform_width - border_thickness
platform_y = platform_x - 100
platform_color = GRAY

# Player properties
player_width, player_height = 50, 50
player_x = 100
player_y = screen_height - player_height - border_thickness
player_speed = 5
player_vel_y = 0
ongroud = False

# Force variables
gravity = 0.5
jump_power = -20

clock = pygame.time.Clock()
running = True 

while running:
    #Code here 
    
    #Comment the next line out when code and game works, and can be exited
    running = False
    #// 
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
