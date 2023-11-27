import pygame

from config import Color


class IntButton:
    def __init__(self, screen, num: int, min_num: int, max_num: int) -> None:
        self.screen = screen
        
        self.num = num
        self.max_num = max_num
        self.min_num = min_num

        self.x = 0
        self.y = 0

        self.margin = 13
        self.width = 70
        self.height = 50

        self.collide_point_num = 0

        self.font = pygame.font.SysFont('comicsansms', 25)
        self.big_font = pygame.font.SysFont('comicsansms', 35)


    def mouse_over(self) -> bool:
        ''' 마우스와 도형의 접촉 여부를 반환하는 함수 '''
        pos = pygame.mouse.get_pos()
        is_collide = False
        self.collide_point_num = None
        for i in range(5):
            rect = pygame.Rect(self.x+self.width*i+self.margin*i, self.y, self.width, self.height)
            if i != 2 and rect.collidepoint(pos):
                self.collide_point_num = i
                is_collide = True
        return is_collide

    def clicked(self) -> int:
        ''' 버튼 클릭시 호출하는 함수입니다 '''
        text_list = [-10, -1, 0, 1, 10]
        num = self.num+text_list[self.collide_point_num]
        if self.min_num <= num <= self.max_num:
            self.num = num
        else:
            if self.collide_point_num == 0:
                self.num = self.min_num
            elif self.collide_point_num == len(text_list)-1:
                self.num = self.max_num
        return self.num

    def show(self):
        ''' 도형을 보여주는 함수 '''
        self.mouse_over()
        text_list = ['-10', '-1', str(self.num), '+1', '+10']
        for i in range(5):
            x = self.x + self.width*i + self.margin*i

            rect = pygame.Rect(x, self.y, self.width, self.height)
            if i == self.collide_point_num:
                pygame.draw.rect(self.screen, Color.bright_gray, rect)
            elif i != 2:
                pygame.draw.rect(self.screen, Color.gray, rect)

            if i == 2:
                text = self.big_font.render(text_list[i], True, Color.white)
            else:
                text = self.font.render(text_list[i], True, Color.black)
            text_x = x+self.width/2-text.get_width()/2
            text_y = self.y+self.height/2-text.get_height()/2
            self.screen.blit(text, (text_x, text_y))
