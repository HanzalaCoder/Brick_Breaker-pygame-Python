import pygame
import sys
import random


class Paddle:
    def __init__(self):
        super().__init__()
        self.paddle_image_ = pygame.image.load("New folder1/Paddle.png").convert_alpha()
        self.paddle_image_ = pygame.transform.rotozoom(self.paddle_image_,90,1)
        self.paddle_rec = self.paddle_image_.get_rect(midbottom=(400,600))
        self.speeed_paddle = 0

    def move_paddle(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.speeed_paddle = -10
            self.paddle_rec.x += self.speeed_paddle
        if key[pygame.K_d]:
            self.speeed_paddle = 10
            self.paddle_rec.x += self.speeed_paddle
        if self.paddle_rec.x <= 0:
            self.paddle_rec.x = 0
        if self.paddle_rec.x >= 660:
            self.paddle_rec.x = 660

    def draw_paddle(self):
        screen.blit(self.paddle_image_,self.paddle_rec)

    def give_paddle(self):
        return self.paddle_rec

    def update(self):
        self.move_paddle()
        self.draw_paddle()


class Ball:

    def __init__(self):
        self.ball_image = pygame.image.load("New folder1/ball.png").convert_alpha()
        new_width = self.ball_image.get_width()
        new_height = self.ball_image.get_height()
        self.ball_image = pygame.transform.scale(self.ball_image,(new_width // 2,new_height // 2))
        self.font = pygame.font.Font("New folder1/Pixeltype.ttf", 50)
        self.ball_rect = self.ball_image.get_rect(center=(400,300))
        self.ball_speed = 0
        self.ball_x = random.choice((2, -2))
        self.ball_y = random.choice((2, -2))

    def ball_movement(self,pad):
        self.ball_rect.x += self.ball_x
        self.ball_rect.y += self.ball_y
        if self.ball_rect.top <= 0:
            self.ball_y *= -1
        if self.ball_rect.left <= 0:
            self.ball_x *= -1
        if self.ball_rect.right >= screen_width:
            self.ball_x *= -1
        if self.ball_rect.colliderect(pad):
            self.ball_y *= -1

    def ball_lives(self):
        self.ball_rect.y += self.ball_y
        lives_ = 0

        if self.ball_rect.bottom >= screen_height:
            self.ball_rect.center = (400,300)
            lives_ += 1
            self.ball_y *= -1
        return lives_

    def ball_brick_hit(self,brick_list_):
        score_ = 0
        self.ball_rect.y += self.ball_y
        for rect in brick_list_:
            if self.ball_rect.colliderect(rect["rect"]):
                rect["Health"] -= 25
                if rect["Health"] == 0:
                    brick_list_.remove(rect)
                    self.ball_y *= -1
                    score_ += 1
                else:
                    self.ball_y *= -1
                    score_ += 0
        return brick_list_,score_

    def ball_fruit_hit(self,fruit_list):
        self.ball_rect.y += self.ball_y
        for rect in fruit_list:
            if self.ball_rect.colliderect(rect):
                fruit_list.remove(rect)
                self.ball_y *= -1
        return fruit_list

    def draw_ball(self):
        screen.blit(self.ball_image,self.ball_rect)

    def update(self,pad):
        self.draw_ball()
        self.ball_movement(pad)

    def give_ball(self):
        return self.ball_rect


class Bricks:
    def __init__(self):
        self.image = pygame.image.load("New folder1/brick (2).png").convert_alpha()
        self.fruit_list = []
        self.health = 100

    def list_bricks(self):
        i = 0
        # block1
        for _ in range(7):
            self.fruit_list.append({"rect":self.image.get_rect(topleft=(0,i)),"Health":self.health})
            i += 25
        j = 25
        for _ in range(4):
            self.fruit_list.append({"rect": self.image.get_rect(topleft=(j, 150)), "Health": self.health})
            j += 45
        k = 150
        for _ in range(7):
            self.fruit_list.append({"rect": self.image.get_rect(topleft=(j, k)), "Health": self.health})
            k -= 25

        # block2
        m = 0
        for _ in range(7):
            self.fruit_list.append({"rect": self.image.get_rect(topleft=(300, m)), "Health": self.health})
            m += 25
        n = 300
        for _ in range(4):
            self.fruit_list.append({"rect": self.image.get_rect(topleft=(n, 150)), "Health": self.health})
            n += 45
        o = 150
        for _ in range(7):
            self.fruit_list.append({"rect": self.image.get_rect(topleft=(n,o)), "Health": self.health})
            o -= 25

        # block3
        x = 0
        for _ in range(7):
            self.fruit_list.append({"rect": self.image.get_rect(topleft=(550, x)), "Health": self.health})
            x += 25
        y = 550
        for _ in range(4):
            self.fruit_list.append({"rect": self.image.get_rect(topleft=(y, 150)), "Health": self.health})
            y += 45
        z = 150
        for _ in range(7):
            self.fruit_list.append({"rect": self.image.get_rect(topleft=(y, z)), "Health": self.health})
            z -= 25
        T = 0
        for _ in range(16):
            self.fruit_list.append({"rect": self.image.get_rect(topleft=(0 + T, 180)), "Health": self.health + 100})
            T += 50
        h = 0
        for _ in range(16):
            self.fruit_list.append({"rect": self.image.get_rect(topleft=(0 + h, 220)), "Health": self.health + 100})
            h += 50

        return self.fruit_list

    def give_image(self):
        return self.image


class Info:
    def __init__(self):
        self.font = pygame.font.Font("New folder1/Pixeltype.ttf",50)
        self.score = 0
        self.lives = 5

    def draw_score(self, score0):
        self.score += score0
        score_info = self.font.render(f"Score {self.score}",False,"black")
        font_rect = score_info.get_rect(midleft=(10,400))
        pygame.draw.rect(screen,"green",font_rect)
        pygame.draw.rect(screen,"green",font_rect,15)
        screen.blit(score_info,font_rect)

    def draw_lives(self,live):
        self.lives -= live
        lives_info = self.font.render(f"Lives {self.lives}", False, "black")
        font_rect1 = lives_info.get_rect(midleft=(10, 450))
        pygame.draw.rect(screen, "green", font_rect1)
        pygame.draw.rect(screen, "green", font_rect1, 15)
        screen.blit(lives_info, font_rect1)
        return self.lives

    def game_info(self):
        game_info = self.font.render(f"Press Space to Start The Game", False, "black")
        game_rec = game_info.get_rect(midleft=(200, 500))
        pygame.draw.rect(screen, "white", game_rec)
        pygame.draw.rect(screen, "white", game_rec, 15)
        screen.blit(game_info, game_rec)


class Fruits:
    def __init__(self):
        self.fruit = pygame.image.load("New folder1/apple.png").convert_alpha()
        self.fruit_list = []

    def draw_fruits(self):
        i = 0
        for _ in range(3):
            self.fruit_list.append(self.fruit.get_rect(topleft=(50+i,40)))
            i += 35
        j = 0
        for _ in range(3):
            self.fruit_list.append(self.fruit.get_rect(topleft=(350 + j, 40)))
            j += 35
        k = 0
        for _ in range(3):
            self.fruit_list.append(self.fruit.get_rect(topleft=(600 + k, 40)))
            k += 35
        return self.fruit_list

    def give_fruit(self):
        return self.fruit


pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("BRICK BREAKER")
clock = pygame.time.Clock()
background = pygame.image.load("New folder1/gameBG.png").convert_alpha()

paddle = Paddle()
ball = Ball()

bricks = Bricks()
brick_list = bricks.list_bricks()
fruits_list = Fruits().draw_fruits()
info = Info()
text = False

# background
background_image = pygame.image.load("New folder1/menu_bg.png").convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                text = True
    if text and brick_list:
        screen.blit(background,(0,0))
        image = Bricks().give_image()
        for num in brick_list:
            screen.blit(image,num["rect"])
        fruits = Fruits().give_fruit()
        for row in fruits_list:
            screen.blit(fruits,row)

        paddle.update()# to move paddle
        a_paddle = paddle.give_paddle()

        ball.update(a_paddle)
        brick_list,score = ball.ball_brick_hit(brick_list) # to remove fruit upon hitting and update score
        fruits_list = ball.ball_fruit_hit(fruits_list)

        lives = ball.ball_lives()
        # update_score
        lives = info.draw_lives(lives)
        info.draw_score(score)
        if lives < 1:
            text = False

    else:
        screen.blit(background_image,(0,0))
        info = Info()
        info.game_info()
        paddle = Paddle()
        ball = Ball()
        bricks = Bricks()
        fruits_list = Fruits().draw_fruits()
        brick_list = bricks.list_bricks()

    pygame.display.update()
    clock.tick(60)
