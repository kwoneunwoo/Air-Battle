import pygame

import config
from config import Color
from objects import ImageButton


class StartScreen:
    def __init__(self, screen, clock) -> None:
        self.screen = screen
        self.clock = clock
        self.msg = ''

    def load_resource(self):
        ''' 스크린에 필요한 자원을 가져오는 함수입니다 '''
        self.font = pygame.font.Font('resources/fonts/neodgm.ttf', 50)

        self.setting_btn = ImageButton(self.screen)
        self.setting_btn.load_image('setting.png')
        self.setting_btn.change_size(50, 50)
        self.setting_btn.x = config.screen_width - self.setting_btn.width/3 *4
        self.setting_btn.y = self.setting_btn.height/3


    def run(self):
        ''' 스크린을 구동하는 함수입니다 '''
        self.msg = ''
        running = True
        while running:
            self.clock.tick(config.frame_rate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.setting_btn.mouse_over():
                        self.msg = 'setting'
                        running = False

            # 버튼과 마우스가 겹치는지 여부에 따라 커서를 변경합니다
            if self.setting_btn.mouse_over():
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            # 배경색을 채웁니다
            self.screen.fill(Color.black)

            # 텍스트를 보여줍니다
            text = self.font.render('TO START THE GAME', True, Color.purple)
            text_x = config.screen_width/2-text.get_width()/2
            text_y = config.screen_height/2-text.get_height()-20
            self.screen.blit(text, (text_x+3, text_y+3))
            text = self.font.render('TO START THE GAME', True, Color.white)
            self.screen.blit(text, (text_x, text_y))

            text = self.font.render('PRESS SPACE KEY', True, Color.purple)
            text_x = config.screen_width/2-text.get_width()/2
            text_y = config.screen_height/2+text.get_height()-20
            self.screen.blit(text, (text_x+3, text_y+3))
            text = self.font.render('PRESS SPACE KEY', True, Color.white)
            self.screen.blit(text, (text_x, text_y))

            # 버튼을 보여줍니다
            self.setting_btn.show()

            # 화면을 업데이트 합니다
            pygame.display.update()
