from pygame import *

win_width = 1100
win_height = 750

window = display.set_mode((win_width,win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.y <= 400:
            self.direction = "right"
        if self.rect.y >= win_width - 500:
            self.direction = "left"

        if self.direction == "left":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed



class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width,self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


w1 = Wall(140, 0, 30, 0, 5, 1080, 10)
w2 = Wall(140, 0, 30, 1080, 5, 10, 750)
#w3 = Wall()

display.set_caption("Лабиринт")
background = transform.scale(image.load("background.jpg"),(win_width,win_height))

hero = Player('hero.png',5,650,5)
hero2 = Player2('hero.png',80,650,5)
cyborg = Enemy('cyborg.png',500,50,2)
cyborg2 = Enemy('cyborg.png',400,50,2)
cyborg3 = Enemy('cyborg.png',300,50,2)
treasure = GameSprite('treasure.png',950,650,0)


clock = time.Clock()
FPS = 60


speed = 10

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

font.init()
font = font.SysFont('Arial', 70)
win = font.render(
    'YOU WIN!',True,(255,215,0)
)

lose = font.render(
    'YOU LOSE!',True,(180,0,0)
)

money = mixer.Sound("money.ogg")
kick = mixer.Sound("kick.ogg")


game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:

        window.blit(background,(0, 0))
        hero.update()
        hero2.update()
        cyborg.update()
        cyborg2.update()
        cyborg3.update()

        treasure.reset()

        hero.reset()
        hero2.reset()
        cyborg.reset()
        cyborg2.reset()
        cyborg3.reset()
        w1.draw_wall()
        w2.draw_wall()
        
        if sprite.collide_rect(hero,cyborg) or sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, w2) or sprite.collide_rect(hero,cyborg2) or sprite.collide_rect(hero,cyborg3):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()
        
        if sprite.collide_rect(hero, treasure):
            finish = True
            window.blit(win, (200, 200))
            money.play()
    else:
        keys = key.get_pressed()
        if keys[K_KP_ENTER] :
            hero.rect.x = 5
            hero.rect.y = 650
            finish=False
            



    clock.tick(FPS)
    display.update()

