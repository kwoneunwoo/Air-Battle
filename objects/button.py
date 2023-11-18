import pygame

from objects.image import Image

class Button(Image):
    def mouse_over(self):
        pos = pygame.mouse.get_pos()
        return self.get_rect().collidepoint(pos)
