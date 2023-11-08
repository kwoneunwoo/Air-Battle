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


            self.screen.fill((0,0,0))

            text = self.font.render('TO START THE GAME', True, (200,0,200))
            self.screen.blit(text, (config.screen_width/2-text.get_width()/2+3, config.screen_height/2-text.get_height()-20+3))
            text = self.font.render('TO START THE GAME', True, (255,255,255))
            self.screen.blit(text, (config.screen_width/2-text.get_width()/2, config.screen_height/2-text.get_height()-20))
            text = self.font.render('PRESS SPACE KEY', True, (200,0,200))
            self.screen.blit(text, (config.screen_width/2-text.get_width()/2+3, config.screen_height/2+text.get_height()-20+3))
            text = self.font.render('PRESS SPACE KEY', True, (255,255,255))
            self.screen.blit(text, (config.screen_width/2-text.get_width()/2, config.screen_height/2+text.get_height()-20))

            pygame.display.update()