import pygame

import config
from config import Color
from objects import ImageButton, ToggleButton, IntButton


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

        # 배경음악 재생 여부 확인
        is_bgm_playing = False
        if pygame.mixer.music.get_busy():
            is_bgm_playing = True

        # 버튼 설정
        self.bgm_btn = ToggleButton(self.screen, is_bgm_playing, 80, 80)
        self.air_btn = ToggleButton(self.screen, config.air_resistance, 80, 80)
        self.fps_btn = IntButton(self.screen, config.frame_rate, 30, 120)
        self.health_btn = IntButton(self.screen, config.health, 1, 99)

        self.btn_list = [self.exit_btn, self.bgm_btn, self.air_btn,
                         self.fps_btn, self.health_btn]


    def run(self):
        ''' 스크린을 구동하는 함수입니다 '''
        running = True
        while running:
            self.clock.tick(config.frame_rate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 마우스 우클릭시 버튼 누름 확인 및 작동
                    if event.button == 1:
                        if self.exit_btn.mouse_over():
                            running = False
                        elif self.bgm_btn.mouse_over():
                            bgm_play = self.bgm_btn.clicked()
                            if bgm_play == False:
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.unpause()
                        elif self.air_btn.mouse_over():
                            config.air_resistance = self.air_btn.clicked()
                        elif self.fps_btn.mouse_over():
                            config.frame_rate = self.fps_btn.clicked()
                        elif self.health_btn.mouse_over():
                            config.health = self.health_btn.clicked()


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


            margin = 20

            # 배경색을 채웁니다
            self.screen.fill(Color.black)


            # 세팅 타이틀
            text = self.neodgm_font.render('Setting', True, Color.white)
            screen_y = text.get_height()/3
            # 중앙, 위와 1/3 격차
            self.screen.blit(text, (config.screen_width/2-text.get_width()/2, screen_y))

            # 버튼의 4/3, 텍스트 세로 중간
            self.exit_btn.x = config.screen_width-self.exit_btn.width/3*4
            self.exit_btn.y = screen_y+text.get_height()/2-self.exit_btn.height/2
            self.exit_btn.show()
            screen_y += text.get_height() + margin/2*3


            # 배경음악 세팅
            text = self.setting_font.render('배경 음악', True, Color.white)
            self.screen.blit(text, (30, screen_y))

            # 뒤와 30px 격차
            self.bgm_btn.x = config.screen_width-self.bgm_btn.width-30
            self.bgm_btn.y = screen_y
            self.bgm_btn.show()
            screen_y += text.get_height() + margin


            # 공기저항 세팅
            text = self.setting_font.render('공기저항', True, Color.white)
            self.screen.blit(text, (30, screen_y))

            # 뒤와 30px 격차
            self.air_btn.x = config.screen_width-self.air_btn.width-30
            self.air_btn.y = screen_y
            self.air_btn.show()
            screen_y += text.get_height() + margin


            # FPS 세팅
            text = self.setting_font.render('FPS', True, Color.white)
            self.screen.blit(text, (30, screen_y))

            # 화면 중앙, 1/2 여백
            self.fps_btn.x = config.screen_width/2-self.fps_btn.width*5/2-self.fps_btn.margin*4/2
            self.fps_btn.y = screen_y + text.get_height() + margin/2
            self.fps_btn.show()
            screen_y = self.fps_btn.y + self.fps_btn.height + margin/3*2


            # 생명력 세팅
            text = self.setting_font.render('생명력', True, Color.white)
            self.screen.blit(text, (30, screen_y))

            # 화면 중앙, 1/2 여백
            self.health_btn.x = config.screen_width/2-self.health_btn.width*5/2-self.health_btn.margin*4/2
            self.health_btn.y = screen_y + text.get_height() + margin/2
            self.health_btn.show()
            screen_y = self.health_btn.y + self.health_btn.height + margin/3*2


            # 화면을 업데이트 합니다
            pygame.display.update()
