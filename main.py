import os
import pygame

import config
import screens


# 경로 설정
os.chdir(os.path.dirname(__file__))

# 초기화
pygame.init()

# FPS 세팅
clock = pygame.time.Clock()

# 화면 크기 세팅
screen = pygame.display.set_mode((config.screen_width, config.screen_height))

# 화면 제목 세팅
programIcon = pygame.image.load('resources/images/gun.png')
pygame.display.set_icon(programIcon)
pygame.display.set_caption('Air Battle')


# 노래 재생
pygame.mixer.music.load('resources/sounds/stranger-things.mp3')
pygame.mixer.music.play(-1)


# 스크린 선언
start_screen = screens.StartScreen(screen, clock)
setting_screen = screens.SettingScreen(screen, clock)
game_screen = screens.GameScreen(screen, clock)
ending_screen = screens.EndingScreen(screen, clock)

# 리소스 로드
for _screen in [start_screen, setting_screen, game_screen, ending_screen]:
    print(f'Loading ... "{_screen.__class__.__name__}"')
    _screen.load_resource()


# 실행
while ending_screen.restart:
    start_screen.run()
    if start_screen.msg == 'setting':
        setting_screen.run()
        continue
    game_screen.init_variable()
    game_screen.run()
    ending_screen.run()
