import pygame

class Image:
    def __init__(self, screen) -> None:
        self.x = 0
        self.y = 0
        self.screen = screen

    def __set_size__(self):
        self.width, self.height = self.img.get_size()

    def load_image(self, path):
        self.img = pygame.image.load(path)
        if path[-3:] == 'png':
            self.img = self.img.convert_alpha()
        self.__set_size__()

    def change_size(self, width: int, height: int):
        self.img = pygame.transform.scale(self.img, (width, height))
        self.__set_size__()

    def flip_image(self, flip_x: bool, flip_y: bool):
        self.img = pygame.transform.flip(self.img, flip_x, flip_y)
        self.__set_size__()

    # def rotate_image(self, angle: int):
    #     self.img = pygame.transform.rotate(self.img, angle)
    #     self.__set_size__()

    def get_rect(self):
        rect = self.img.get_rect()
        rect.left = self.x
        rect.top = self.y
        return rect

    def show(self):
        self.screen.blit(self.img, (self.x, self.y))
