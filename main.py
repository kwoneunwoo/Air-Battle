import os
import pygame

from screens import start, game, ending



# 경로 설정
os.chdir(os.path.dirname(__file__))

# 초기화
pygame.init()

# FPS 세팅
frame_rate = 60
clock = pygame.time.Clock()

# 화면 크기 세팅
screen_width = 480
screen_height = 700#640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 제목 세팅
programIcon = pygame.image.load('images/gun.png')
pygame.display.set_icon(programIcon)
pygame.display.set_caption('Air Battle')



# 스크린 선언
start_screen = start.StartScreen(screen, clock)
game_screen = game.GameScreen(screen, clock)
ending_screen = ending.EndingScreen(screen, clock)

# 리소스 로드
print('준비창 로드중...')
start_screen.load_resource()
print('게임창 로드중...')
game_screen.load_resource()
print('엔딩창 로드중...')
ending_screen.load_resource()

game_screen.init_variable()

# 실행
start_screen.run()
game_screen.run()
ending_screen.run()
while ending_screen.restart:
    start_screen.run()
    game_screen.init_variable()
    game_screen.run()
    ending_screen.run()
