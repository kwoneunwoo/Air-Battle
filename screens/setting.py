import pygame

import config
from config import Color
from objects import ImageButton, SquareButton, ToggleButton


class SettingScreen:
    def __init__(self, screen, clock) -> None:
        self.screen = screen
        self.clock = clock

    def load_resource(self):
        ''' 스크린에 필요한 자원을 가져오는 함수입니다 '''
        self.neodgm_font = pygame.font.Font('resources/fonts/neodgm.ttf', 65)
        self.setting_font = pygame.font.Font('resources/fonts/blackhansans.ttf', 55)

        self.exit_btn = ImageButton(self.screen)
        self.exit_btn.load_image('logout.png')
        self.exit_btn.change_size(50, 50)
        self.exit_btn.x = config.screen_width-self.exit_btn.width/3*4

        # self.on_btn = SquareButton(self.screen, x=80, y=80, text='test',
        #                            color=Color.green, focused_color=Color.bright_green)

        self.bgm_btn = ToggleButton(self.screen, False, 80, 80)
        self.air_btn = ToggleButton(self.screen, False, 80, 80)

        self.btn_list = [self.exit_btn, self.bgm_btn, self.air_btn]


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
                    if event.button == 1:
                        if self.exit_btn.mouse_over():
                            running = False
                        elif self.bgm_btn.mouse_over():
                            self.bgm_btn.clicked()
                        elif self.air_btn.mouse_over():
                            self.air_btn.clicked()


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


            # 세팅 텍스트와 버튼
            text = self.neodgm_font.render('Setting', True, Color.white)
            self.screen.blit(text, (config.screen_width/2-text.get_width()/2, text.get_height()/3))
            screen_y = text.get_height()/3*4

            self.exit_btn.y = text.get_height()/3+text.get_height()/2-self.exit_btn.height/2
            self.exit_btn.show()

            # 배경음악 세팅
            text = self.setting_font.render('배경 음악', True, Color.white)
            screen_y += 20
            self.screen.blit(text, (30, screen_y))

            self.bgm_btn.x = config.screen_width-self.bgm_btn.width-30
            self.bgm_btn.y = screen_y
            self.bgm_btn.show()
            screen_y += text.get_height()

            # 공기저항 세팅
            text = self.setting_font.render('공기저항', True, Color.white)
            screen_y += 20
            self.screen.blit(text, (30, screen_y))

            self.air_btn.x = config.screen_width-self.air_btn.width-30
            self.air_btn.y = screen_y
            self.air_btn.show()
            screen_y += text.get_height()



            # 화면을 업데이트 합니다
            pygame.display.update()
