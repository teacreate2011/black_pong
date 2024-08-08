from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size = (65, 65)):
        super().__init__()
        self.image = transform.scale(image.load(player_image),size)

        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size = (65, 65)):
        super().__init__(player_image, player_x, player_y, player_speed, size)
    def update(self, up, down, stop_value=200):
        keys_pressed = key.get_pressed()
        if keys_pressed[up] and self.rect.y >5:
            self.rect.y -= 10
        if keys_pressed[down] and self.rect.y < WIN_H - stop_value:
            self.rect.y += 10

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size = (65, 65)):
        super().__init__(player_image, player_x, player_y, player_speed, size)
        self.speed_x = player_speed
        self.speed_y = player_speed
    def update(self,):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.y <0 or self.rect.y > WIN_H - 65:
            self.speed_y *= -1
        if self.rect.x <0 or self.rect.x > WIN_W - 65:
            self.speed_x *= -1 
WIN_W = 700
WIN_H = 500
PLAT_SP = 2
BALL_SP = 1

window = display.set_mode((WIN_W, WIN_H))


display.set_caption("пинг-понг")

# задать картинку фона такого же размера, как размер окна
background = transform.scale(
    image.load("пол.jpg"),
    # здесь - размеры картинки
    (WIN_W, WIN_H)
)
cat1 = Player('кот2.png', 0, 250, PLAT_SP, (150, 200))
cat2 = Player('кот1.png', WIN_W - 150, 250, PLAT_SP, (150, 200))
ball = Ball('клубок.png', 382 ,282, BALL_SP)
# игровой цикл
game = True
while game:
    # отобразить картинку фона
    window.blit(background,(0, 0))
    cat1.reset()
    cat2.reset()
    cat1.update(K_w, K_s)
    cat2.update(K_UP, K_DOWN)
    ball.reset()
    ball.update()
    

    # слушать события и обрабатывать
    for e in event.get():
        # выйти, если нажат "крестик"
        if e.type == QUIT:
            game = False
    # обновить экран, чтобы отобрзить все изменения
    display.update()
