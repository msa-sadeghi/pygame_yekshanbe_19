import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
square = pygame.Rect(200 , 300, 100, 100)
circle = pygame.Rect(300 , 500, 100, 100)
moving_left, moving_right, moving_up, moving_down = (False, False, False, False)
moving_circle_left, moving_circle_right, moving_circle_up,moving_circle_down = (False, False, False, False)
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_UP:
                moving_up = True
            if event.key == pygame.K_DOWN:
                moving_down = True
            if event.key == pygame.K_a:
                moving_circle_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False 
            if event.key == pygame.K_UP:
                moving_up = False 
            if event.key == pygame.K_DOWN:
                moving_down = False    
            if event.key == pygame.K_a:
                moving_circle_left = False  
                
    if moving_left == True:
        square.x -= 5            
    if moving_right == True:
        square.x += 5
    if moving_up:
        square.y -= 5            
    if moving_down:
        square.y += 5  
    if moving_circle_left == True:
        circle.x -= 5          
    screen.fill("black")
    pygame.draw.rect(screen, "red", square)
    pygame.draw.ellipse(screen, "green", circle)
    pygame.display.update()
    clock.tick(FPS)