from pygame import *
FPS = 60
clock = time.Clock()

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
BALL_SP = 3

window = display.set_mode((WIN_W, WIN_H))
font.init()
my_font = font.SysFont('arial', 70)
win_1_txt = my_font.render('Left Player lost!', True, (255, 215, 0))
win_2_txt = my_font.render('Right Player lost!', True, (255, 215, 0))

display.set_caption("пинг-понг")

# задать картинку фона такого же размера, как размер окна
background = transform.scale(
    image.load("пол.jpg"),
    # здесь - размеры картинки
    (WIN_W, WIN_H)
)
cat1 = Player('кот2.png', 0, 250, PLAT_SP, (120, 200))
cat2 = Player('кот1.png', WIN_W - 120, 250, PLAT_SP, (120, 200))
ball = Ball('клубок.png', 382 ,282, BALL_SP)
# игровой цикл
game = True
finish = False

while game:
    if not finish:
    # отобразить картинку фона
        window.blit(background,(0, 0))
        cat1.reset()
        cat2.reset()
        cat1.update(K_w, K_s)
        cat2.update(K_UP, K_DOWN)
        ball.reset()
        ball.update()
        
        if sprite.collide_rect(cat1, ball):
            ball.speed_x *= -1
        if sprite.collide_rect(cat2, ball):
            ball.speed_x *= -1
        if ball.rect.x < cat1.rect.x:
            window.blit(win_1_txt, (WIN_W // 2 - 180, WIN_H // 2 - 50))
            display.update()
            finish = True
        if ball.rect.x > cat2.rect.x:
            window.blit(win_2_txt, (WIN_W // 2 - 180, WIN_H // 2 - 50))
            display.update()
            finish = True


    # слушать события и обрабатывать
    for e in event.get():
        # выйти, если нажат "крестик"
        if e.type == QUIT:
            game = False
    # обновить экран, чтобы отобрзить все изменения
    clock.tick(FPS)
    display.update()
