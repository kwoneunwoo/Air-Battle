import pygame

import config
from config import Color
from objects import ImageButton, SquareButton

class SettingScreen:
    def __init__(self, screen, clock) -> None:
        self.screen = screen
        self.clock = clock

    def load_resource(self):
        ''' 스크린에 필요한 자원을 가져오는 함수입니다 '''
        self.font = pygame.font.Font('resources/fonts/neodgm.ttf', 50)

        self.exit_btn = ImageButton(self.screen)
        self.exit_btn.load_image('logout.png')
        self.exit_btn.change_size(50, 50)
        self.exit_btn.x = config.screen_width-self.exit_btn.width/3*4
        self.exit_btn.y = self.exit_btn.height/3

        self.on_btn = SquareButton(self.screen, Color.green, Color.bright_green)
        self.on_btn.set_coordinate(80, 80)

        self.btn_list = [self.exit_btn, self.on_btn]


    def run(self):
        ''' 스크린을 구동하는 함수입니다 '''
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
                    if event.button == 1 and self.exit_btn.mouse_over():
                        running = False

            # 버튼과 마우스가 겹치는지 여부에 따라 커서를 변경합니다
            mouse_over = False
            for btn in self.btn_list:
                if btn.mouse_over():
                    mouse_over = True
                    break

            if mouse_over:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


            # 배경색을 채웁니다
            self.screen.fill(Color.black)


            # 글자와 버튼을 보여줍니다
            text = self.font.render('Setting', True, Color.white)
            self.screen.blit(text, (config.screen_width/2-text.get_width()/2, text.get_height()/3))

            self.exit_btn.show()
            self.on_btn.show()

            # 화면을 업데이트 합니다
            pygame.display.update()
