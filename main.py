import os
import pygame

import screens



# 경로 설정
os.chdir(os.path.dirname(__file__))

# 초기화
pygame.init()

# FPS 세팅
clock = pygame.time.Clock()

# 화면 크기 세팅
screen_width = 480
screen_height = 700#640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 제목 세팅
programIcon = pygame.image.load('resources/images/gun.png')
pygame.display.set_icon(programIcon)
pygame.display.set_caption('Air Battle')


# 노래 재생
# pygame.mixer.music.load('resources/sounds/stranger-things.mp3')
# pygame.mixer.music.play(-1)


# 스크린 선언
start_screen = screens.StartScreen(screen, clock)
game_screen = screens.GameScreen(screen, clock)
ending_screen = screens.EndingScreen(screen, clock)

# 리소스 로드
print('준비창 로드중...')
start_screen.load_resource()
print('게임창 로드중...')
game_screen.load_resource()
print('엔딩창 로드중...')
ending_screen.load_resource()


# 실행
while ending_screen.restart:
    start_screen.run()
    game_screen.init_variable()
    game_screen.run()
    ending_screen.run()
