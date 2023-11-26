import os
import pygame

class Image:
    def __init__(self, screen) -> None:
        self.x = 0
        self.y = 0
        self.img = None
        self.width = 0
        self.height = 0
        self.screen = screen

    def __set_size__(self):
        ''' 이미지의 가로와 세로를 저장하는 내부함수 '''
        self.width, self.height = self.img.get_size()

    def load_image(self, path: str):
        ''' 이미지를 가져오는 함수 '''
        self.img = pygame.image.load(os.path.join('resources/images', path))
        if path[-3:] == 'png':
            self.img = self.img.convert_alpha()
        self.__set_size__()

    def change_size(self, width: int, height: int):
        ''' 이미지의 사이즈를 바꾸는 함수 '''
        self.img = pygame.transform.scale(self.img, (width, height))
        self.__set_size__()

    def flip_image(self, flip_x: bool, flip_y: bool):
        ''' 이미지를 반전시키는 함수 '''
        self.img = pygame.transform.flip(self.img, flip_x, flip_y)
        self.__set_size__()

    # def rotate_image(self, angle: int):
    #     ''' 이미지를 회전시키는 함수 '''
    #     self.img = pygame.transform.rotate(self.img, angle)
    #     self.__set_size__()

    def get_rect(self) -> pygame.Rect:
        ''' 이미지의 Rect 객체를 반환하는 함수 '''
        rect = self.img.get_rect()
        rect.left = self.x
        rect.top = self.y
        return rect

    def show(self):
        ''' 도형을 보여주는 함수 '''
        self.screen.blit(self.img, (self.x, self.y))
