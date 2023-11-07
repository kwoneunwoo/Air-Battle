import os
import pygame
import random



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
programIcon = pygame.image.load('images/gun.png')
pygame.display.set_icon(programIcon)
pygame.display.set_caption('Air Battle')



# 반복 가능한 객체 생성
class Image:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def __set_size__(self):
        self.width, self.height = self.img.get_size()

    def load_image(self, path):
        self.img = pygame.image.load(path)
        if path[-3:] == 'png':
            self.img = self.img.convert_alpha()
        self.__set_size__()

    def change_size(self, width: int, height: int):
        self.img = pygame.transform.scale(self.img, (width, height))
        self.__set_size__()

    def flip_image(self, flip_x: bool, flip_y: bool):
        self.img = pygame.transform.flip(self.img, flip_x, flip_y)
        self.__set_size__()

    # def rotate_image(self, angle: int):
    #     self.img = pygame.transform.rotate(self.img, angle)
    #     self.__set_size__()

    def get_rect(self):
        self.rect = self.img.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y
        return self.rect

    def show(self):
        screen.blit(self.img, (self.x, self.y))



# 백그라운드 이미지 로드 (1)
background_1 = Image()
background_1.load_image('images/sky.jpg')
background_1.change_size(screen_width, screen_height)

# 백그라운드 이미지 로드 (2)
background_2 = Image()
background_2.img = background_1.img.copy()
background_2.flip_image(False, True)
# 두번째 배경 좌표: 화면 밖 위쪽
background_2.y = -background_2.height

# 구름 이미지 로드
# cloud = Image()
# cloud.load_image('images/cloud-1.png')
# cloud.change_size(400, 191)
# cloud.img.set_alpha(128)

# 채워진 생명 이미지 로드
filled_heart = Image()
filled_heart.load_image('images/filled-heart.png')
filled_heart.change_size(50, 50)
filled_heart.xy_list = [
    (screen_width-filled_heart.width, 0),
    (screen_width-filled_heart.width*2, 0),
    (screen_width-filled_heart.width*3, 0)
    ]

# 비워진 생명 이미지 로드
empty_heart = Image()
empty_heart.load_image('images/empty-heart.png')
empty_heart.change_size(50, 50)

# 비행기 이미지 로드
user = Image()
user.load_image('images/fighter-jet.png')
user.change_size(120, 120)
# 비행기 이동 필요 좌표
user.to_x = 0
user.to_y = 0
# 비행기 좌표: 중앙 하단
user.x = screen_width/2 - user.width/2
user.y = screen_height - user.height

# 미사일 이미지 로드
missile = Image()
missile.load_image('images/missile.png')
missile.change_size(60, 226)
# 미사일 좌표: 중앙 최상단
missile.x = screen_width/2 - missile.width/2
missile.y = -missile.height


# 총알 이미지 로드
bullet = Image()
bullet.load_image('images/bullet.png')
# 총알 리스트 생성
bullet.xy_list = []


# 배경음악 로드
pygame.mixer.music.load('sounds/stranger-things.mp3')
pygame.mixer.music.play(-1)
 
# 효과음 로드
gunshot_sound = pygame.mixer.Sound('sounds/gun-shot.mp3')
ending_sound = pygame.mixer.Sound('sounds/ending.mp3')


class StartScreen:
    def __init__(self) -> None:
        self.font = pygame.font.Font('fonts/neodgm.ttf', 50)

    def run(self):
        running = True
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False

            screen.fill((0,0,0))

            # text = self.font.render('TO START THE GAME', True, (200, 0, 200))
            # text.x = screen_width/2 - text.get_width()/2+3
            # text.y = screen_height/2 - text.get_height()-20+3
            # screen.blit(text, (text.x, text.y))
            # text.set_colorkey((255, 255, 255))
            # screen.blit(text, (text.x, text.y))

            text = self.font.render('TO START THE GAME', True, (200,0,200))
            screen.blit(text, (screen_width/2-text.get_width()/2+3, screen_height/2-text.get_height()-20+3))
            text = self.font.render('TO START THE GAME', True, (255,255,255))
            screen.blit(text, (screen_width/2-text.get_width()/2, screen_height/2-text.get_height()-20))
            text = self.font.render('PRESS SPACE KEY', True, (200,0,200))
            screen.blit(text, (screen_width/2-text.get_width()/2+3, screen_height/2+text.get_height()-20+3))
            text = self.font.render('PRESS SPACE KEY', True, (255,255,255))
            screen.blit(text, (screen_width/2-text.get_width()/2, screen_height/2+text.get_height()-20))

            pygame.display.update()


class GameScreen:
    def __init__(self) -> None:
        self.font = pygame.font.Font('fonts/neodgm.ttf', 30)
        self.used_bullet = 0
        self.crashed_missile = 0
        self.health = 3
    
    def write_text(self):
        text_1 = self.font.render(f'Used bullet: {self.used_bullet}', True, (0,0,0))
        screen.blit(text_1, (3,0))
        text_2 = self.font.render(f'Crashed missile: {self.crashed_missile}', True, (0,0,0))
        screen.blit(text_2, (3,text_1.get_height()))

    def show_health(self):
        for i in range(len(filled_heart.xy_list)):
            filled_heart.x = filled_heart.xy_list[i][0]
            filled_heart.y = filled_heart.xy_list[i][1]
            filled_heart.show()

    def run(self):
        running = True
        while running:
            fps = clock.tick(60)
            # 이벤트 발생시 가져오기
            for event in pygame.event.get():
                # 끄기 버튼 누를시 끄기
                if event.type == pygame.QUIT:
                    quit()

                # 키 누를때 움직이기
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        user.to_x += 0.7
                    elif event.key == pygame.K_LEFT:
                        user.to_x -= 0.7
                    elif event.key == pygame.K_UP:
                        user.to_y -= 0.7
                    elif event.key == pygame.K_DOWN:
                        user.to_y += 0.7
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_LCTRL:
                        bullet.y = user.y + bullet.height
                        bullet.x = user.x + user.width/2 - bullet.width/2
                        bullet.xy_list.append([bullet.x, bullet.y])
                        self.used_bullet += 1
                        gunshot_sound.play()

                # 키 올릴때 초기화
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key==pygame.K_LEFT:
                        user.to_x = 0
                    elif event.key == pygame.K_UP or event.key==pygame.K_DOWN:
                        user.to_y = 0


            # 배경 이동
            background_1.y += 0.05 * fps
            background_2.y += 0.05 * fps

            if background_1.y >= screen_height:
                background_1.y = -background_1.height + background_2.y
            if background_2.y >= screen_height:
                background_2.y = -background_2.height + background_1.y

            # 구름 이동
            # cloud.y += 0.08 * fps
            
            # 미사일 좌우 랜덤 하강
            missile.y += 0.5  * fps
            if missile.y >= screen_height:
                missile.y = -missile.height
                missile.x = random.randint(0, screen_width - missile.width)

            # 총알 상승
            delete_list = []
            for i in range(len(bullet.xy_list)):
                if bullet.xy_list[i][1] <= 0:
                    delete_list.append(i)
                else:
                    bullet.xy_list[i][1] -= 0.7 * fps

            # 화면을 넘어간 총알은 삭제
            for d in delete_list[::-1]:
                del bullet.xy_list[d]

            # 유저 좌표 변경
            user.x += user.to_x * fps
            user.y += user.to_y * fps

            # x좌표 이상 벗어나지 않게
            if user.x >= screen_width - user.width: # 우측
                user.x = screen_width - user.width
            elif user.x <= 0: # 좌측
                user.x = 0
            # y좌표 이상 벗어나지 않게
            if user.y >= screen_height - user.height: # 하단
                user.y = screen_height - user.height
            elif user.y <= 0: # 상단
                user.y = 0
            

            # 유저 충돌 감지
            if user.get_rect().colliderect(missile.get_rect()):
                # pygame.mixer.music.fadeout(500)
                ending_sound.play()
                running = False

            # 미사일 저격 감지
            delete_list = []
            for i in range(len(bullet.xy_list)):
                bullet.x = bullet.xy_list[i][0]
                bullet.y = bullet.xy_list[i][1]
                if missile.get_rect().colliderect(bullet.get_rect()):
                    delete_list.append(i)
                    missile.y = -missile.height
                    missile.x = random.randint(0, screen_width - missile.width)

            # 저격 성공한 총알은 삭제
            for d in delete_list[::-1]:
                self.crashed_missile += 1
                del bullet.xy_list[d]


            # 이미지 위치 지정
            background_1.show()
            background_2.show()
            # cloud.show()
            for i in range(len(bullet.xy_list)):
                bullet.x = bullet.xy_list[i][0]
                bullet.y = bullet.xy_list[i][1]
                bullet.show()
            missile.show()
            user.show()
            self.write_text()
            self.show_health()


            # 지정한 위치 업데이트
            pygame.display.update()


class EndingScreen:
    def __init__(self) -> None:
        self.font = pygame.font.Font('fonts/neodgm.ttf', 100)

    def run(self):
        running = True
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            text = self.font.render('GAME OVER', True, (255, 0, 0))
            screen.blit(text, (screen_width/2 - text.get_width()/2, screen_height/2 - text.get_height()/2))

            pygame.display.update()


if __name__ == '__main__':
    start_screen = StartScreen()
    game_screen = GameScreen()
    ending_screen = EndingScreen()

    start_screen.run()
    game_screen.run()
    ending_screen.run()
