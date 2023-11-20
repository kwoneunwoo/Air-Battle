import pygame

from objects.image import Image

class Button(Image):
    def change_cursor(self):
        if self.mouse_over():
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def mouse_over(self) -> bool:
        pos = pygame.mouse.get_pos()
        return self.get_rect().collidepoint(pos)
