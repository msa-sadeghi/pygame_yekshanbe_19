import pygame
import os
from button import Button
import pickle
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
        pygame.draw.line(screen, "white", (i * TILE_SIZE - scroll, 0), (i * TILE_SIZE -scroll, HEIGHT))

    for i in range(ROWS + 1):
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

tile_map = []
for i in range(ROWS):
    r  = [-1] * COLS
    tile_map.append(r)
def show_tiles():
    for i in range(len(tile_map)):
        for j in range(len(tile_map[i])):
            if tile_map[i][j] != -1:
                screen.blit(buttons_list[tile_map[i][j]].image, (j * TILE_SIZE - scroll, i * TILE_SIZE))

scroll = 0
scroll_left, scroll_right = (False, False)
level_number = 1
font = pygame.font.SysFont("arial", 28)
level_text =  font.render(f"level {level_number}", True, "black")

up_image = pygame.image.load("./up.png")
down_image = pygame.transform.rotate(up_image, 180)

up_button = Button(up_image, "button", 150, HEIGHT + 20)
down_button = Button(down_image, "button", 250, HEIGHT + 20)

save_image = pygame.image.load("./save_btn.png")
load_image = pygame.image.load("./load_btn.png")

save_button = Button(save_image, "button", 350, HEIGHT + 30)
load_button = Button(load_image, "button", 450, HEIGHT + 30)

def save_level(level_number):
    with open(f"level{level_number}", "wb") as f:
        pickle.dump(tile_map, f)

def load_level(level_number):
    global tile_map
    if os.path.exists(f"level{level_number}"):
        with open(f"level{level_number}", "rb") as f:
            tile_map = pickle.load(f)
    else:
        print(f"level {level_number} not exists")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
    screen.fill("lightpink")
    draw_lines()
    show_tiles()
    pygame.draw.rect(screen, "lightgreen", (WIDTH, 0, RIGHT_SIDE, HEIGHT + BOTTOM_SIDE))
    pygame.draw.rect(screen, "lightgreen", (0, HEIGHT, WIDTH, BOTTOM_SIDE))
    level_text =  font.render(f"level {level_number}", True, "black")
    if up_button.draw(screen) and up_button.locked == False:

        level_number += 1
        up_button.locked = True
    if down_button.draw(screen) and down_button.locked == False:
        if level_number > 1:
            level_number -= 1
        down_button.locked = True
    if save_button.draw(screen):
        save_level(level_number)
    if load_button.draw(screen):
        load_level(level_number)
    screen.blit(level_text, (40, HEIGHT + 40 ))
    if scroll_left and scroll > 0:
        scroll -= 5
    if scroll_right:
        scroll += 5
    for i,btn in enumerate(buttons_list):
        if btn.draw(screen) == True:
            current_btn_number = i
            clicked_or_not = True
    if clicked_or_not:
        pygame.draw.rect(screen, "blue", buttons_list[current_btn_number].rect, 3)

    mouse_pos = pygame.mouse.get_pos()
    c = (mouse_pos[0] + scroll) // TILE_SIZE
    r = mouse_pos[1] // TILE_SIZE
    if mouse_pos[0] < WIDTH and mouse_pos[1] < HEIGHT:
        if pygame.mouse.get_pressed()[0]:
            tile_map[r][c] = current_btn_number  

        if pygame.mouse.get_pressed()[2]:
            tile_map[r][c] = -1  
    
    pygame.display.update()
    clock.tick(FPS)