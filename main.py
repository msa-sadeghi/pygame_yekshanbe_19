import pygame
from player import Player
pygame.init()

width = 1000
height = 600

screen = pygame.display.set_mode((width, height))
fps = 60
clock = pygame.time.Clock()

my_player = Player(200, 350)

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if my_player.shooting == True:
        my_player.change_animation("Shoot")
    elif my_player.idle == True:
        my_player.change_animation("Idle")
    else:
        my_player.change_animation("Run")
    screen.fill('lightpink')
    my_player.move()
    my_player.draw(screen)
    pygame.display.update()
   
    clock.tick(fps)