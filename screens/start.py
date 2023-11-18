import pygame

import config
from objects.button import Button

class StartScreen:
    def __init__(self, screen, clock) -> None:
        self.screen = screen
        self.clock = clock
        self.msg = ''

    def load_resource(self):
        self.font = pygame.font.Font('resources/fonts/neodgm.ttf', 50)

        self.setting_btn = Button(self.screen)
        self.setting_btn.load_image('setting.png')
        self.setting_btn.change_size(50, 50)
        self.setting_btn.x = config.screen_width - self.setting_btn.width/3 *4
        self.setting_btn.y = self.setting_btn.height/3


    def run(self):
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


            self.screen.fill(config.Color.black)


            text = self.font.render('TO START THE GAME', True, config.Color.purple)
            text_x = config.screen_width/2-text.get_width()/2
            text_y = config.screen_height/2-text.get_height()-20
            self.screen.blit(text, (text_x+3, text_y+3))
            text = self.font.render('TO START THE GAME', True, config.Color.white)
            self.screen.blit(text, (text_x, text_y))

            text = self.font.render('PRESS SPACE KEY', True, config.Color.purple)
            text_x = config.screen_width/2-text.get_width()/2
            text_y = config.screen_height/2+text.get_height()-20
            self.screen.blit(text, (text_x+3, text_y+3))
            text = self.font.render('PRESS SPACE KEY', True, config.Color.white)
            self.screen.blit(text, (text_x, text_y))

            self.setting_btn.show()


            pygame.display.update()
