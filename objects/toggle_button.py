import pygame

from config import Color


class ToggleButton:
    def __init__(self, screen, is_on: bool, x: int, y: int) -> None:
        self.screen = screen
        self.is_on = is_on

        self.x = x
        self.y = y
        self.width = 130
        self.height = 50

        self.font = pygame.font.SysFont('comicsansms', 25)
        self.text = None

        self.color = None
        self.focused_color = None
        # 최초 색 지정을 위한 함수 호출
        self.is_on = not self.is_on
        self.clicked()

    def mouse_over(self) -> bool:
        ''' 마우스와 도형의 접촉 여부를 반환하는 함수 '''
        pos = pygame.mouse.get_pos()
        return pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(pos)

    def clicked(self) -> bool:
        ''' 버튼 클릭시 호출하는 함수입니다 '''
        self.is_on = not self.is_on
        if self.is_on:
            self.text = 'On'
            self.color = Color.green
            self.focused_color = Color.bright_green
        else:
            self.text = 'Off'
            self.color = Color.red
            self.focused_color = Color.bright_red
        return self.is_on
    
    def show(self):
        ''' 도형을 보여주는 함수 '''
        # 도형을 보여줍니다
        if self.mouse_over():
            pygame.draw.rect(self.screen, self.focused_color, (self.x,self.y,self.width,self.height))
        else:
            pygame.draw.rect(self.screen, self.color, (self.x,self.y,self.width,self.height))

        # 텍스트를 보여줍니다
        text = self.font.render(self.text, True, Color.black)
        text_x = (self.x+self.width/2)-text.get_width()/2
        text_y = (self.y+self.height/2)-text.get_height()/2
        self.screen.blit(text, (text_x, text_y))
