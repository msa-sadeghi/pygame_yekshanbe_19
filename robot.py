import pygame
from player import Player
pygame.init()

width = 1000
height = 600

screen = pygame.display.set_mode((width, height))
fps = 60
clock = pygame.time.Clock()

# robot = pygame.image.load("./png/Idle/Idle1.png")
# robot = pygame.transform.scale_by(robot, 0.3)
# robot_rect = robot.get_rect(topleft=(100, 300))

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    # screen.blit(robot, robot_rect)
    clock.tick(fps)