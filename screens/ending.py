import pygame

import config


class EndingScreen:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.restart = True

    def load_resource(self):
        self.font = pygame.font.Font('resources/fonts/neodgm.ttf', 100)

    def run(self):
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
                    elif event.key == pygame.K_r:
                        running = False

            text = self.font.render('GAME OVER', True, config.Color.red)
            self.screen.blit(text, (config.screen_width/2 - text.get_width()/2, config.screen_height/2 - text.get_height()/2))

            pygame.display.update()
