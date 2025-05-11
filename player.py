from pygame.sprite import Sprite
import pygame
import os
from bullet import Bullet
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
        self.direction  = 1
        self.last_shoot_time = pygame.time.get_ticks()
        self.ammo = 5
        self.ammo_charge = True
        self.sliding = False
        self.gravity = 0
        self.in_air = False
        self.melee = False

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
            self.direction = -1
            self.idle = False
            self.flip = True
            dx -= 5
        if keys[pygame.K_RIGHT]:
            self.direction = 1
            self.idle = False
            self.flip = False
            dx += 5
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.idle = True

        if keys[pygame.K_SPACE]:
            self.shooting = True
        if not keys[pygame.K_SPACE]:
            self.shooting = False
        if keys[pygame.K_DOWN] and not self.idle:
            self.sliding = True
            self.rect.x += 3 * self.direction
        else:
            self.sliding = False

        if keys[pygame.K_UP] and not self.in_air:
            self.gravity = -15
            self.in_air = True
        if keys[pygame.K_m]:
            self.melee  = True
        else:
            self.melee = False

        dy += self.gravity
        self.gravity += 1
        if self.rect.bottom + dy > 500:
            dy = 500 - self.rect.bottom
            self.gravity = 0
            self.in_air = False


        self.rect.x += dx
        self.rect.y += dy


    def change_animation(self, action):
        if self.action != action:
            self.action = action
            self.costume_number = 0
            self.timer = pygame.time.get_ticks()


    def shoot_bullet(self, bullet_group):
        if self.shooting and  pygame.time.get_ticks() - self.last_shoot_time > 150 and self.ammo > 0:
            self.ammo -= 1
            self.last_shoot_time = pygame.time.get_ticks()
            b = Bullet(
                self.rect.centerx + self.direction * self.rect.size[0],
                self.rect.centery,
                self.direction
            )
            bullet_group.add(b)
        if self.ammo <= 0 and pygame.time.get_ticks() - self.last_shoot_time >= 10000:
            self.ammo = 5
            
        
