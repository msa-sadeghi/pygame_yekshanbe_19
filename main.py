import pygame
from player import Player
pygame.init()

width = 1000
height = 600

screen = pygame.display.set_mode((width, height))
fps = 60
clock = pygame.time.Clock()

my_player = Player(200, 350)
bullet_group = pygame.sprite.Group()
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if my_player.melee:
        my_player.change_animation("Melee")
    elif my_player.shooting and my_player.idle == False:
        my_player.change_animation("RunShoot")
    elif my_player.shooting and my_player.in_air:
        my_player.change_animation("JumpShoot")
    elif my_player.in_air:
        my_player.change_animation("Jump")
    elif my_player.sliding:
        my_player.change_animation("Slide")
    elif my_player.shooting == True:
        my_player.change_animation("Shoot")
    elif my_player.idle == True:
        my_player.change_animation("Idle")
    else:
        my_player.change_animation("Run")
    screen.fill('lightpink')
    my_player.move()
    my_player.draw(screen)
    my_player.shoot_bullet(bullet_group)
    bullet_group.update()
    bullet_group.draw(screen)
    pygame.display.update()
   
    clock.tick(fps)