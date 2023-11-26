import random
import pygame

import config
from objects import Image


class GameScreen:
    def __init__(self, screen, clock) -> None:
        self.screen = screen
        self.clock = clock

    def load_resource(self):
        ''' 스크린에 필요한 자원을 가져오는 함수입니다 '''
        self.font = pygame.font.Font('resources/fonts/neodgm.ttf', 30)

        # 배경 이미지를 가져옵니다
        self.background_1 = Image(self.screen)
        self.background_1.load_image('sky.jpg')
        self.background_1.change_size(config.screen_width, config.screen_height)

        self.background_2 = Image(self.screen)
        self.background_2.img = self.background_1.img.copy()
        self.background_2.flip_image(False, True)

        # 구름 이미지들을 가져옵니다
        self.cloud_1 = Image(self.screen)
        self.cloud_1.load_image('cloud-1.png')
        self.cloud_1.change_size(400, 191)

        self.cloud_2 = Image(self.screen)
        self.cloud_2.load_image('cloud-2.png')
        self.cloud_2.change_size(400, 400)

        self.cloud_3 = Image(self.screen)
        self.cloud_3.load_image('cloud-3.png')
        self.cloud_3.change_size(400, 400)

        # 생명력 이미지를 가져와 x, y 좌표 리스트를 지정합니다
        self.filled_heart = Image(self.screen)
        self.filled_heart.load_image('filled-heart.png')
        self.filled_heart.change_size(40, 40)
        self.filled_heart.xy_list = []

        self.empty_heart = Image(self.screen)
        self.empty_heart.load_image('empty-heart.png')
        self.empty_heart.change_size(40, 40)

        # 유저 이미지를 가져옵니다
        self.user = Image(self.screen)
        self.user.load_image('fighter-jet.png')
        self.user.change_size(120, 120)

        # 미사일 이미지를 가져옵니다
        self.missile = Image(self.screen)
        self.missile.load_image('missile.png')
        self.missile.change_size(60, 226)

        # 폭발 이미지를 가져옵니다
        self.explode = Image(self.screen)
        self.explode.load_image('explode.png')
        self.explode.change_size(100, 100)

        # 총알 이미지를 가져옵니다
        self.bullet = Image(self.screen)
        self.bullet.load_image('bullet.png')

        # 효과음을 가져옵니다
        self.gunshot_sound = pygame.mixer.Sound('resources/sounds/gun-shot.mp3')
        self.ending_sound = pygame.mixer.Sound('resources/sounds/ending.mp3')

    def init_variable(self):
        ''' 게임과 관련된 변수를 초기화하는 함수입니다 '''
        self.running = True
        self.cloud = None
        self.health = config.health
        self.used_bullet = 0
        self.crashed_missile = 0
    
        for i in range(1, 4):
            self.filled_heart.xy_list.append((config.screen_width-self.filled_heart.width*i-10*i, 10))
            
        self.background_1.y = 0
        self.background_2.y = -self.background_2.height

        self.user.to_right = False
        self.user.to_left = False
        self.user.to_up = False
        self.user.to_down = False
        self.user.x = config.screen_width/2 - self.user.width/2
        self.user.y = config.screen_height - self.user.height

        self.missile.x = config.screen_width/2 - self.missile.width/2
        self.missile.y = -self.missile.height

        self.explode.is_show = False
        self.explode.count = 0

        self.bullet.xy_list = []


    def write_text(self):
        ''' 화면에 나타낼 정보(텍스트)를 보여주는 함수입니다 '''
        text_1 = self.font.render(f'Used bullet: {self.used_bullet}', True, (0,0,0))
        self.screen.blit(text_1, (3,0))
        text_2 = self.font.render(f'Crashed missile: {self.crashed_missile}', True, (0,0,0))
        self.screen.blit(text_2, (3,text_1.get_height()))
    
    def lost_health(self):
        ''' 생명력을 잃게 하는 함수입니다 '''
        self.health -= 1
        self.ending_sound.play()

    def show_health(self):
        ''' 화면에 남은 생명력을 보여주는 함수입니다 '''
        # 남은 생명력이 0이라면 게임을 종료합니다
        if self.health <= 0:
            self.running = False

        # 남은 생명력을 표시하며 4개 이상이라면 숫자로 표현합니다
        if self.health < 4:
            remaining_health = 3-self.health
            for i in range(3):
                if remaining_health != 0:
                    remaining_health -= 1
                    self.empty_heart.x = self.filled_heart.xy_list[i][0]
                    self.empty_heart.y = self.filled_heart.xy_list[i][1]
                    self.empty_heart.show()
                else:
                    self.filled_heart.x = self.filled_heart.xy_list[i][0]
                    self.filled_heart.y = self.filled_heart.xy_list[i][1]
                    self.filled_heart.show()
        else:
            self.filled_heart.x = self.filled_heart.xy_list[1][0]
            self.filled_heart.y = self.filled_heart.xy_list[1][1]
            self.filled_heart.show()

            text = self.font.render(f'X{self.health}', True, config.Color.black)
            text_x = self.filled_heart.xy_list[0][0]
            text_y = self.filled_heart.xy_list[0][1]+self.filled_heart.height/2-text.get_height()/2
            self.screen.blit(text, (text_x, text_y))


    def move_background(self, fps: int):
        ''' 배경 이미지를 이동시키는 함수입니다 '''
        self.background_1.y += 0.05 * fps
        self.background_2.y += 0.05 * fps

        if self.background_1.y >= config.screen_height:
            self.background_1.y = -self.background_1.height + self.background_2.y
        if self.background_2.y >= config.screen_height:
            self.background_2.y = -self.background_2.height + self.background_1.y

    def move_cloud(self, fps: int):
        ''' 구름 이미지를 랜덤으로 지정하고 이동시키는 함수입니다 '''
        if self.cloud == None or self.cloud.y >= config.screen_height:
            self.cloud = random.choice([self.cloud_1, self.cloud_2, self.cloud_3])
            self.cloud.y = -self.cloud.height
        self.cloud.y += 0.08 * fps

    def reset_missile_position(self):
        ''' 미사일 이미지의 위치를 재설정하는 함수입니다 '''
        self.missile.y = -self.missile.height
        self.missile.x = random.randint(0, config.screen_width - self.missile.width)

    def move_missile(self, fps: int):
        ''' 미사일 이미지를 이동시키는 함수입니다 '''
        self.missile.y += 0.5  * fps
        if self.missile.y >= config.screen_height:
            self.lost_health()
            self.reset_missile_position()

    def move_bullet(self, fps: int):
        ''' 리스트에 저장된 총알의 좌표를 이동시키는 함수입니다 '''
        delete_list = []
        for i in range(len(self.bullet.xy_list)):
            if self.bullet.xy_list[i][1] <= 0:
                delete_list.append(i)
            else:
                self.bullet.xy_list[i][1] -= 0.7 * fps

        for d in delete_list[::-1]:
            del self.bullet.xy_list[d]
    
    def move_user(self, fps: int):
        ''' 유저 이미지의 위치를 이동시키는 함수입니다 '''
        to_x = 0
        to_y = 0

        if self.user.to_right == True:
            to_x = 0.7
        elif self.user.to_left == True:
            to_x = -0.7

        if self.user.to_up == True:
            to_y = -0.7
        elif self.user.to_down == True or config.air_resistance:
            to_y = 0.7

        self.user.x += to_x * fps
        self.user.y += to_y * fps

        # 유저 이미지가 화면을 벗어나지 않도록 조정합니다
        if self.user.x >= config.screen_width - self.user.width:
            self.user.x = config.screen_width - self.user.width
        elif self.user.x <= 0:
            self.user.x = 0

        if self.user.y >= config.screen_height - self.user.height:
            self.user.y = config.screen_height - self.user.height
        elif self.user.y <= 0:
            self.user.y = 0


    def check_user_crash(self):
        ''' 유저가 미사일과 충돌했는지 확인하는 함수입니다 '''
        if self.user.get_rect().colliderect(self.missile.get_rect()):
            self.lost_health()

            self.explode.is_show = True
            self.explode.x = self.user.x + self.user.width/2 - self.explode.width/2
            self.explode.y = self.user.y - self.explode.height/2
            
            if self.health > 0:
                self.reset_missile_position()

    def check_missile_crash(self):
        ''' 총알 이미지와 미사일의 충돌을 확인합니다 '''
        delete_list = []
        for i in range(len(self.bullet.xy_list)):
            self.bullet.x = self.bullet.xy_list[i][0]
            self.bullet.y = self.bullet.xy_list[i][1]
            if self.missile.get_rect().colliderect(self.bullet.get_rect()):
                delete_list.append(i)

                self.explode.is_show = True
                self.explode.x = self.missile.x + self.missile.width/2 - self.explode.width/2
                self.explode.y = self.missile.y + self.missile.height - self.explode.height/2

                self.reset_missile_position()

        for d in delete_list[::-1]:
            self.crashed_missile += 1
            del self.bullet.xy_list[d]


    def run(self):
        ''' 스크린을 구동하는 함수입니다 '''
        while self.running:
            fps = self.clock.tick(config.frame_rate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                elif event.type == pygame.KEYDOWN:
                    # 유저를 이동하는 코드입니다
                    if event.key == pygame.K_RIGHT:
                        self.user.to_right = True
                    elif event.key == pygame.K_LEFT:
                        self.user.to_left = True
                    elif event.key == pygame.K_UP:
                        self.user.to_up = True
                    elif event.key == pygame.K_DOWN:
                        self.user.to_down = True
                    # 총알을 발사하는 코드입니다
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_LCTRL:
                        self.bullet.y = self.user.y + self.bullet.height
                        self.bullet.x = self.user.x + self.user.width/2 - self.bullet.width/2
                        self.bullet.xy_list.append([self.bullet.x, self.bullet.y])
                        self.used_bullet += 1
                        self.gunshot_sound.play()
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.user.to_right = False
                    elif event.key == pygame.K_LEFT:
                        self.user.to_left = False
                    elif event.key == pygame.K_UP:
                        self.user.to_up = False
                    elif event.key==pygame.K_DOWN:
                        self.user.to_down = False

            # 이미지들을 움직입니다
            self.move_background(fps)
            self.move_cloud(fps)
            self.move_missile(fps)
            self.move_bullet(fps)
            self.move_user(fps)

            # 이미지간 충돌 여부를 확인합니다
            self.check_user_crash()
            self.check_missile_crash()

            # 이미지들과 화면 정보들을 보여줍니다
            self.background_1.show()
            self.background_2.show()
            self.cloud.show()
            for i in range(len(self.bullet.xy_list)):
                self.bullet.x = self.bullet.xy_list[i][0]
                self.bullet.y = self.bullet.xy_list[i][1]
                self.bullet.show()
            self.missile.show()
            self.user.show()
            self.write_text()
            self.show_health()
            # 약 0.1초 동안 폭발 이미지를 표시합니다
            if self.explode.is_show:
                self.explode.count += 1
                self.explode.show()
                if self.explode.count >= config.frame_rate/10:
                    self.explode.count = 0
                    self.explode.is_show = False

            # 화면을 업데이트 합니다
            pygame.display.update()
