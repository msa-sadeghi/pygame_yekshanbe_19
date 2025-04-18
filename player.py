from pygame.sprite import Sprite
import pygame
import os
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.animation_types = (
            'Dead', 'Idle', 'Jump', 'JumpMelee', 'JumpShoot',
            'Melee', 'Run', 'RunShoot', 'Shoot', 'Slide'
        )

        self.all_images = {}
        for animation in self.animation_types:
            image_list = []
            num_of_images = len(os.listdir(f"./png/{animation}"))
            for i in range(1,num_of_images):
                img = pygame.image.load(f"./png/{animation}/{animation}{i}.png")
                img = pygame.transform.scale_by(img, 0.4)
                image_list.append(img)
            self.all_images[animation] = image_list
        self.image = self.all_images["Idle"][0]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.costume_number = 0
        self.action = "Idle"
        self.timer = pygame.time.get_ticks()
        self.idle = True
        self.flip = False
        self.shooting = False

    def draw(self, screen):
        screen.blit(
            pygame.transform.flip(self.image, self.flip, False), 
            self.rect)
        self.animation()

    def animation(self):
        self.image = self.all_images[self.action][self.costume_number]
        if pygame.time.get_ticks() - self.timer >= 100:# یک دهم ثانیه
            self.timer = pygame.time.get_ticks()
            self.costume_number += 1
            if self.costume_number >= len(self.all_images[self.action]):
                self.costume_number = 0

    def move(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.idle = False
            self.flip = True
            dx -= 5
        if keys[pygame.K_RIGHT]:
            self.idle = False
            self.flip = False
            dx += 5
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.idle = True

        if keys[pygame.K_SPACE]:
            self.shooting = True
        if not keys[pygame.K_SPACE]:
            self.shooting = False
        
        self.rect.x += dx
        self.rect.y += dy


    def change_animation(self, action):
        if self.action != action:
            self.action = action
            self.costume_number = 0
            self.timer = pygame.time.get_ticks()
            
        
