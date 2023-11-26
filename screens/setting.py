import pygame

import config
from config import Color
from objects import ImageButton, SquareButton

class SettingScreen:
    def __init__(self, screen, clock) -> None:
        self.screen = screen
        self.clock = clock

    def load_resource(self):
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

            # 마우스와 버튼이 겹치는지에 따라 커서를 바꿉니다
            mouse_over = False
            for btn in self.btn_list:
                if btn.mouse_over():
                    mouse_over = True
                    break
            if mouse_over:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


            self.screen.fill(Color.black)


            text = self.font.render('Setting', True, Color.white)
            self.screen.blit(text, (config.screen_width/2-text.get_width()/2, text.get_height()/3))

            self.exit_btn.show()
            self.on_btn.show()


            pygame.display.update()
