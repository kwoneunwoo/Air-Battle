import pygame

from config import Color


class SquareButton():
    def __init__(self,
                 screen,
                 x: int, y: int,
                 text: str,
                 color: tuple, focused_color: tuple = None) -> None:
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 150
        self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.font = pygame.font.SysFont('comicsansms', 25)
        self.text = self.font.render(text, True, Color.black)
        self.text_x = (self.x+self.width/2)-self.text.get_width()/2
        self.text_y = (self.y+self.height/2)-self.text.get_height()/2

        self.color = color
        self.focused_color = color if focused_color == None else focused_color

    def mouse_over(self) -> bool:
        ''' 마우스와 도형의 접촉 여부를 반환하는 함수 '''
        pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(pos)
    
    def show(self):
        ''' 도형을 보여주는 함수 '''
        if self.mouse_over():
            pygame.draw.rect(self.screen, self.focused_color, self.rect)
        else:
            pygame.draw.rect(self.screen, self.color, self.rect)

        self.screen.blit(self.text, (self.text_x, self.text_y))
