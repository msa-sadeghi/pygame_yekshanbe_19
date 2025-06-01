import pygame
import os
from button import Button
pygame.init()

WIDTH = 1000
HEIGHT = 600

RIGHT_SIDE = 400
BOTTOM_SIDE = 100
COLS = 150
TILE_SIZE = 50
ROWS = 12
screen = pygame.display.set_mode((WIDTH + RIGHT_SIDE,  HEIGHT + BOTTOM_SIDE))


object_images = []
for img in os.listdir("./game_world/Objects"):
    object_images.append(
        pygame.transform.scale(
            pygame.image.load(f"./game_world/Objects/{img}"),
            (TILE_SIZE, TILE_SIZE)
            )
    )
tile_images = []
for img in os.listdir("./game_world/Tiles"):
    tile_images.append(
        pygame.transform.scale(
            pygame.image.load(f"./game_world/Tiles/{img}"),
            (TILE_SIZE, TILE_SIZE)
            )
    )




def draw_lines():
    for i in range(COLS + 1):
        pygame.draw.line(screen, "white", (i * TILE_SIZE, 0), (i * TILE_SIZE, HEIGHT))

    for i in range(COLS + 1):
        pygame.draw.line(screen, "white", (0, i * TILE_SIZE), (WIDTH, i * TILE_SIZE)) 

buttons_list = []
r = 0
c = 0

for img in object_images:
    btn = Button(img, "object", WIDTH + 20 + c * 70, 20 + r * 70)
    buttons_list.append(btn)
    c += 1
    if c == 5:
        r += 1
        c = 0

for img in tile_images:
    btn = Button(img, "tile", WIDTH + 20 + c * 70, 20 + r * 70)
    buttons_list.append(btn)
    c += 1
    if c == 5:
        r += 1
        c = 0
FPS = 60

current_btn_number = 0
clicked_or_not =  False
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("lightpink")
    draw_lines()
    pygame.draw.rect(screen, "lightgreen", (WIDTH, 0, RIGHT_SIDE, HEIGHT + BOTTOM_SIDE))
    pygame.draw.rect(screen, "lightgreen", (0, HEIGHT, WIDTH, BOTTOM_SIDE))

    for i,btn in enumerate(buttons_list):
        if btn.draw(screen) == True:
            current_btn_number = i
            clicked_or_not = True
    if clicked_or_not:
        pygame.draw.rect(screen, "blue", buttons_list[current_btn_number].rect, 3)
    pygame.display.update()
    clock.tick(FPS)