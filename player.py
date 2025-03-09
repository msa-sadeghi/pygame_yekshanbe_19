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

    def draw(self, screen):
        screen.blit(self.image, self.rect)



