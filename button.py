import pygame

class Button:
    def __init__(self, image, type, x,y):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect(topleft=(x,y))
        self.locked = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        clicked = False
        mouse_position = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_position):
            self.image.set_alpha(100)
            if pygame.mouse.get_pressed()[0] == True:
                clicked = True
            else:
                self.locked = False
        else:
            self.image.set_alpha(255)

        return clicked