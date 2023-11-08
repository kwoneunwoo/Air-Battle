import random
import pygame

import config
from image import Image


class GameScreen:
    def __init__(self, screen, clock) -> None:
        self.screen = screen
        self.clock = clock

        self.running = True
        self.cloud = None
        self.health = config.health
        self.used_bullet = 0
        self.crashed_missile = 0

    def load_resource(self):
        self.font = pygame.font.Font('fonts/neodgm.ttf', 30)


        self.background_1 = Image()
        self.background_1.load_image('images/sky.jpg')
        self.background_1.change_size(config.screen_width, config.screen_height)

        self.background_2 = Image()
        self.background_2.img = self.background_1.img.copy()
        self.background_2.flip_image(False, True)


        self.cloud_1 = Image()
        self.cloud_1.load_image('images/cloud-1.png')
        self.cloud_1.change_size(400, 191)

        self.cloud_2 = Image()
        self.cloud_2.load_image('images/cloud-2.png')
        self.cloud_2.change_size(400, 400)

        self.cloud_3 = Image()
        self.cloud_3.load_image('images/cloud-3.png')
        self.cloud_3.change_size(400, 400)


        self.filled_heart = Image()
        self.filled_heart.load_image('images/filled-heart.png')
        self.filled_heart.change_size(40, 40)
        self.filled_heart.health = config.health
        self.filled_heart.xy_list = []
        for i in range(1, self.filled_heart.health+1):
            self.filled_heart.xy_list.append((config.screen_width-self.filled_heart.width*i-10*i, 10))

        self.empty_heart = Image()
        self.empty_heart.load_image('images/empty-heart.png')
        self.empty_heart.change_size(40, 40)


        self.user = Image()
        self.user.load_image('images/fighter-jet.png')
        self.user.change_size(120, 120)

        self.missile = Image()
        self.missile.load_image('images/missile.png')
        self.missile.change_size(60, 226)

        self.explode = Image()
        self.explode.load_image('images/explode.png')
        self.explode.change_size(100, 100)

        self.bullet = Image()
        self.bullet.load_image('images/bullet.png')

        # TODO: 배경음 테스트
        pygame.mixer.music.load('sounds/stranger-things.mp3')
        pygame.mixer.music.play(-1)

        self.gunshot_sound = pygame.mixer.Sound('sounds/gun-shot.mp3')
        self.ending_sound = pygame.mixer.Sound('sounds/ending.mp3')

    def init_variable(self):
        self.background_2.y = -self.background_2.height

        self.user.to_x = 0
        self.user.to_y = 0
        self.user.x = config.screen_width/2 - self.user.width/2
        self.user.y = config.screen_height - self.user.height

        self.missile.x = config.screen_width/2 - self.missile.width/2
        self.missile.y = -self.missile.height

        self.explode.is_show = False
        self.explode.count = 0

        self.bullet.xy_list = []


    def write_text(self):
        text_1 = self.font.render(f'Used bullet: {self.used_bullet}', True, (0,0,0))
        self.screen.blit(text_1, (3,0))
        text_2 = self.font.render(f'Crashed missile: {self.crashed_missile}', True, (0,0,0))
        self.screen.blit(text_2, (3,text_1.get_height()))
    
    def lost_health(self):
        self.health -= 1
        self.ending_sound.play()

    def show_health(self):
        remaining_health = self.filled_heart.health-self.health
        if remaining_health == self.filled_heart.health:
            self.running = False

        for i in range(self.filled_heart.health):
            if remaining_health != 0:
                remaining_health -= 1
                self.empty_heart.x = self.filled_heart.xy_list[i][0]
                self.empty_heart.y = self.filled_heart.xy_list[i][1]
                self.empty_heart.show()
            else:
                self.filled_heart.x = self.filled_heart.xy_list[i][0]
                self.filled_heart.y = self.filled_heart.xy_list[i][1]
                self.filled_heart.show()

    def show_cloud(self, fps: int):
        if self.cloud == None or self.cloud.y >= config.screen_height:
            self.cloud = random.choice([self.cloud_1, self.cloud_2, self.cloud_3])
            self.cloud.y = -self.cloud.height
        self.cloud.y += 0.08 * fps
        self.cloud.show()


    def run(self):
        while self.running:
            fps = self.clock.tick(config.frame_rate)
            # 이벤트 발생시 가져오기
            for event in pygame.event.get():
                # 끄기 버튼 누를시 끄기
                if event.type == pygame.QUIT:
                    quit()

                # 키 누를때 움직이기
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.user.to_x += 0.7
                    elif event.key == pygame.K_LEFT:
                        self.user.to_x -= 0.7
                    elif event.key == pygame.K_UP:
                        self.user.to_y -= 0.7
                    elif event.key == pygame.K_DOWN:
                        self.user.to_y += 0.7
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_LCTRL:
                        self.bullet.y = self.user.y + self.bullet.height
                        self.bullet.x = self.user.x + self.user.width/2 - self.bullet.width/2
                        self.bullet.xy_list.append([self.bullet.x, self.bullet.y])
                        self.used_bullet += 1
                        self.gunshot_sound.play()

                # 키 올릴때 초기화
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key==pygame.K_LEFT:
                        self.user.to_x = 0
                    elif event.key == pygame.K_UP or event.key==pygame.K_DOWN:
                        self.user.to_y = 0


            # 배경 이동
            self.background_1.y += 0.05 * fps
            self.background_2.y += 0.05 * fps

            if self.background_1.y >= config.screen_height:
                self.background_1.y = -self.background_1.height + self.background_2.y
            if self.background_2.y >= config.screen_height:
                self.background_2.y = -self.background_2.height + self.background_1.y

            # 미사일 좌우 랜덤 하강
            self.missile.y += 0.5  * fps
            if self.missile.y >= self.screen_height:
                self.lost_health()
                self.missile.y = -self.missile.height
                self.missile.x = random.randint(0, self.screen_width - self.missile.width)

            # 총알 상승
            delete_list = []
            for i in range(len(self.bullet.xy_list)):
                if self.bullet.xy_list[i][1] <= 0:
                    delete_list.append(i)
                else:
                    self.bullet.xy_list[i][1] -= 0.7 * fps

            # 화면을 넘어간 총알은 삭제
            for d in delete_list[::-1]:
                del self.bullet.xy_list[d]

            # 유저 좌표 변경
            self.user.x += self.user.to_x * fps
            self.user.y += self.user.to_y * fps

            # x좌표 이상 벗어나지 않게
            if self.user.x >= config.screen_width - self.user.width: # 우측
                self.user.x = config.screen_width - self.user.width
            elif self.user.x <= 0: # 좌측
                self.user.x = 0
            # y좌표 이상 벗어나지 않게
            if self.user.y >= config.screen_height - self.user.height: # 하단
                self.user.y = config.screen_height - self.user.height
            elif self.user.y <= 0: # 상단
                self.user.y = 0
            

            # 유저 충돌 감지
            if self.user.get_rect().colliderect(self.missile.get_rect()):
                self.lost_health()
                # 폭발 이미지 위치 조정
                self.explode.is_show = True
                self.explode.x = self.user.x + self.user.width/2 - self.explode.width/2
                self.explode.y = self.user.y - self.explode.height/2
                # 미사일 다시 내려오기
                self.missile.y = -self.missile.height
                self.missile.x = random.randint(0, self.screen_width - self.missile.width)

            # 미사일 저격 감지
            delete_list = []
            for i in range(len(self.bullet.xy_list)):
                self.bullet.x = self.bullet.xy_list[i][0]
                self.bullet.y = self.bullet.xy_list[i][1]
                if self.missile.get_rect().colliderect(self.bullet.get_rect()):
                    delete_list.append(i)
                    # 폭발 이미지 위치 조정
                    self.explode.is_show = True
                    self.explode.x = self.missile.x + self.missile.width/2 - self.explode.width/2
                    self.explode.y = self.missile.y + self.missile.height - self.explode.height/2
                    # 미사일 다시 내려오기
                    self.missile.x = random.randint(0, self.screen_width - self.missile.width)
                    self.missile.y = -self.missile.height

            # 저격 성공한 총알은 삭제
            for d in delete_list[::-1]:
                self.crashed_missile += 1
                del self.bullet.xy_list[d]


            # 이미지 위치 지정
            self.background_1.show()
            self.background_2.show()
            self.show_cloud(fps)
            # 좌표 리스트로 총알 그리기
            for i in range(len(self.bullet.xy_list)):
                self.bullet.x = self.bullet.xy_list[i][0]
                self.bullet.y = self.bullet.xy_list[i][1]
                self.bullet.show()
            self.missile.show()
            self.user.show()
            self.write_text()
            self.show_health()
            # 0.1초동안 폭발 이미지 표시
            if self.explode.is_show:
                self.explode.count += 1
                self.explode.show()
                if self.explode.count >= config.frame_rate/10:
                    self.explode.count = 0
                    self.explode.is_show = False

            # 지정한 위치 업데이트
            pygame.display.update()