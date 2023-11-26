import pygame

import config


class EndingScreen:
    def __init__(self, screen, clock) -> None:
        self.screen = screen
        self.clock = clock
        self.restart = True

    def load_resource(self):
        ''' 화면에 필요한 자원을 가져오는 함수입니다 '''
        self.font = pygame.font.Font('resources/fonts/neodgm.ttf', 100)

    def run(self):
        ''' 화면을 구동하는 함수입니다 '''
        running = True
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

            # 텍스트를 보여줍니다
            text = self.font.render('GAME OVER', True, config.Color.red)
            self.screen.blit(text, (config.screen_width/2 - text.get_width()/2, config.screen_height/2 - text.get_height()/2))

            # 화면을 업데이트 합니다
            pygame.display.update()
