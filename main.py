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

    # 세팅 화면에 진입합니다
    if start_screen.msg == 'setting':
        setting_screen.run()
        # 세팅이 종료된 후 반복문을 재실행합니다
        continue

    # 게임 화면의 변수를 초기화합니다
    game_screen.init_variable()
    # 마우스 커서가 안보이게 설정합니다
    pygame.mouse.set_visible(False)
    game_screen.run()
    # 마우스 커서가 보이게 설정합니다
    pygame.mouse.set_visible(True)

    # 필요한 정보를 넘겨주고 엔딩 화면을 실행합니다
    ending_screen.best_score = game_screen.best_score
    ending_screen.playtime = game_screen.playtime
    if game_screen.used_bullet == 0:
        ending_screen.accuracy = 0
    else:
        ending_screen.accuracy = game_screen.crashed_missile/game_screen.used_bullet
    ending_screen.run()
