import pygame

from objects.image import Image

class ImageButton(Image):
    def mouse_over(self) -> bool:
        pos = pygame.mouse.get_pos()
        return self.get_rect().collidepoint(pos)
