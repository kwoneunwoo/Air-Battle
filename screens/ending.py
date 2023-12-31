import pygame

import config


class EndingScreen:
    def __init__(self, screen, clock) -> None:
        self.screen = screen
        self.clock = clock
        self.restart = True

        self.best_score = 0
        self.playtime = None
        self.accuracy = 0

    def load_resource(self):
        ''' 화면에 필요한 자원을 가져오는 함수입니다 '''
        self.font = pygame.font.Font('resources/fonts/neodgm.ttf', 100)
        self.small_text = pygame.font.Font('resources/fonts/neodgm.ttf', 30)

    def run(self):
        ''' 화면을 구동하는 함수입니다 '''
        running = True
        bg_opportunity = 45
        while running:
            self.clock.tick(config.frame_rate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.restart = False
                        running = False
                    # R 버튼을 눌렀을때 재시작합니다
                    elif event.key == pygame.K_r:
                        running = False


            # 여백을 변수로 설정합니다
            text_margin = 5
            bg_margin = 30


            # 텍스트를 정의합니다
            gameover_text = self.font.render('GAME OVER', True, config.Color.red)
            best_text = self.small_text.render(f'Best Score: {str(self.best_score).rjust(5," ")+" "*2}', True, config.Color.white)
            playtime_text = self.small_text.render(f'Playtime: {self.playtime}', True, config.Color.white)
            accuracy_text = self.small_text.render(f'Accuracy: {self.accuracy:.3f}', True, config.Color.white)
            reset_text = self.small_text.render('Press r to restart', True, config.Color.white)

            # 텍스트의 x값을 중앙으로 설정합니다
            gameover_text_x = config.screen_width/2-gameover_text.get_width()/2
            best_text_x = config.screen_width/2-best_text.get_width()/2
            playtime_text_x = config.screen_width/2-playtime_text.get_width()/2
            accuracy_text_x = config.screen_width/2-accuracy_text.get_width()/2
            reset_text_x = config.screen_width/2-reset_text.get_width()/2

            # 텍스트의 y값을 설정합니다
            gameover_text_y = 0
            best_text_y = gameover_text_y+gameover_text.get_height()+text_margin
            playtime_text_y = best_text_y+best_text.get_height()+text_margin
            accuracy_text_y = playtime_text_y+playtime_text.get_height()+text_margin
            reset_text_y = accuracy_text_y+accuracy_text.get_height()+text_margin*3


            # 텍스트의 높이와 y값을 계산합니다
            info_height = reset_text_y+reset_text.get_height()
            info_y = config.screen_height/2 - info_height/2


            # 검정색 반투명 화면의 크기를 설정합니다
            background = pygame.Surface((config.screen_width, info_height+bg_margin))
            background.fill(config.Color.black)
            background.set_alpha(10)


            # 화면에 요소들을 보여줍니다
            if bg_opportunity >= 0:
                self.screen.blit(background, (0, info_y-bg_margin/2))
                bg_opportunity -= 1
            self.screen.blit(gameover_text, (gameover_text_x, info_y+gameover_text_y))
            self.screen.blit(best_text, (best_text_x, info_y+best_text_y))
            self.screen.blit(playtime_text, (playtime_text_x, info_y+playtime_text_y))
            self.screen.blit(accuracy_text, (accuracy_text_x, info_y+accuracy_text_y))
            self.screen.blit(reset_text, (reset_text_x, info_y+reset_text_y))


            # 화면을 업데이트 합니다
            pygame.display.update()
