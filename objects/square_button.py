import pygame

class SquareButton():
    def __init__(self, screen, color: tuple, focused_color: tuple = None) -> None:
        self.screen = screen
        self.x = None
        self.y = None
        self.width = 150
        self.height = 50
        self.rect = None
        self.color = color
        self.focused_color = color if focused_color == None else focused_color
    
    def set_coordinate(self, x: int, y: int):
        ''' Rect 객체를 생성하는 함수  '''
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def mouse_over(self) -> bool:
        ''' 마우스와 도형의 접촉 여부를 반환하는 함수 '''
        pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(pos)
    
    def show(self):
        ''' 도형을 보여주는 함수 '''
        if self.mouse_over():
            pygame.draw.rect(self.screen, self.focused_color, self.rect)#(self.x,self.y,self.width,self.height))
        else:
            pygame.draw.rect(self.screen, self.color, (self.x,self.y,self.width,self.height))
