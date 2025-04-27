from pygame.sprite import Sprite
import pygame
class Bullet(Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.all_images = []
        for i in range(5):
            img = pygame.image.load(f"./Objects/Bullet/Bullet_00{i}.png")
            img = pygame.transform.scale_by(img, 0.4)
            self.all_images.append(img)

        self.frame_index = 0
        self.image = self.all_images[self.frame_index]
        self.rect = self.image.get_rect(topleft = (x,y))
        self.direction = direction
        self.last_animation_time = pygame.time.get_ticks()
        

    def update(self):

        self.image = self.all_images[self.frame_index]
        self.image = pygame.transform.flip(self.image, self.direction == -1, False)
        if pygame.time.get_ticks() - self.last_animation_time >= 100:
            self.last_animation_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.all_images):
                self.frame_index = 0
        self.rect.x += 5 * self.direction