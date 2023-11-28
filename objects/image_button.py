import pygame

from objects.image import Image

class ImageButton(Image):
    def __init__(self, screen, use_alpha: bool = False) -> None:
        super().__init__(screen)
        self.use_alpha = use_alpha

    def mouse_over(self) -> bool:
        ''' 마우스와 도형의 접촉 여부를 반환하는 함수 '''
        pos = pygame.mouse.get_pos()
        return self.get_rect().collidepoint(pos)
    
    def show(self):
        if self.use_alpha:
            if self.mouse_over():
                self.img.set_alpha(255)
            else:
                self.img.set_alpha(180)
        super().show()
