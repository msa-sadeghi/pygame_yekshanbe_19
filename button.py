import pygame

class Button:
    def __init__(self, image, type, x,y):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect(topleft=(x,y))

    def draw(self, screen):
        pass