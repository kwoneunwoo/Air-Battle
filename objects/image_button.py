import pygame

from objects.image import Image

class ImageButton(Image):
    def mouse_over(self) -> bool:
        ''' 마우스와 도형의 접촉 여부를 반환하는 함수 '''
        pos = pygame.mouse.get_pos()
        return self.get_rect().collidepoint(pos)
