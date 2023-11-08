import pygame

import config

class StartScreen:
    def __init__(self, screen, clock) -> None:
        self.screen = screen
        self.clock = clock

    def load_resource(self):
        self.font = pygame.font.Font('fonts/neodgm.ttf', 50)

    def run(self):
        running = True
        while running:
            self.clock.tick(config.frame_rate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
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


            pygame.display.update()
