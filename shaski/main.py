from typing import Any
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint


FPS = 60
win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
clock = time.Clock()
background = scale(load("checkers_thumb.png"), (win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_hight, player_speed):
        super().__init__()
        self.image = scale(load(player_image), (player_width, player_hight))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Cursor(GameSprite):
    def update(self):
        pos = mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
g_press1 = False
g_press2 = False
class g_Check1(GameSprite):
    def update(self):
        self.rect.x = cordx-70
        self.rect.y = cordy+50
        if mouse.get_pressed()[0]:
            if mouse.get_pos()[0] >= self.rect.x and mouse.get_pos()[1] >=self.rect.y and mouse.get_pos()[0] <= self.rect.x+70 and mouse.get_pos()[1] <=self.rect.y+50:
                global g_press1
                g_press1 = True
class g_Check2(GameSprite):
    def update(self):
        self.rect.x = cordx+70
        self.rect.y = cordy+50       
        if mouse.get_pressed()[0]:
            if mouse.get_pos()[0] >= self.rect.x and mouse.get_pos()[1] >=self.rect.y and mouse.get_pos()[0] <= self.rect.x+70 and mouse.get_pos()[1] <=self.rect.y+50:
                global g_press2
                g_press2 = True
cordx = -100
cordy = -100
class w_Check(GameSprite):
    def update(self):
        if mouse.get_pressed()[0]:
            if mouse.get_pos()[0] >= self.rect.x and mouse.get_pos()[1] >=self.rect.y and mouse.get_pos()[0] <= self.rect.x+70 and mouse.get_pos()[1] <=self.rect.y+50:
                global cordx, cordy
                cordx = self.rect.x
                cordy = self.rect.y
            if cordx != -100:
                if g_press1:
                    self.rect.x = g1.rect.x
                    self.rect.y = g1.rect.y
                    cordx = -100
                if g_press2:
                    self.rect.x = g2.rect.x
                    self.rect.y = g2.rect.y
                    cordx = -100
                

                    
                
            
class b_Check(GameSprite):
    def update(self):
        pass

green = sprite.Group()
cursor = Cursor("white_check.png", 300, 300, 50, 50, 0)
white = sprite.Group()

for i in range(2):
    x=cordx+70
    y=cordy+50
    g1 = g_Check1("green_check.png", x, y, 70, 50, 1)
    g2 = g_Check2("green_check.png", x, y, 70, 50, 1)
    green.add(g1)
    green.add(g2)





xx=70
yy=50
for i in range(4):
    x = xx
    y = yy
    xx+=140
    speed = 0
    mon = w_Check("white_check.png", x, y, 70, 50, speed)
    white.add(mon)
xx=140
yy=100
for i in range(4):
    x = xx
    y = yy
    xx+=140
    speed = 0
    mon = w_Check("white_check.png", x, y, 70, 50, speed)
    white.add(mon)
xx=70
yy=150
for i in range(4):
    x = xx
    y = yy
    xx+=140
    speed = 0
    mon = w_Check("white_check.png", x, y, 70, 50, speed)
    white.add(mon)
black = sprite.Group()
xx=140
yy=400
for i in range(4):
    x = xx
    y = yy
    xx+=140
    speed = 0
    mon = b_Check("black_check.png", x, y, 70, 50, speed)
    black.add(mon)
xx=70
yy=350
for i in range(4):
    x = xx
    y = yy
    xx+=140
    speed = 0
    mon = b_Check("black_check.png", x, y, 70, 50, speed)
    black.add(mon)
xx=140
yy=300
for i in range(4):
    x = xx
    y = yy
    xx+=140
    speed = 0
    mon = b_Check("black_check.png", x, y, 70, 50, speed)
    black.add(mon)

game = True
finish = False
p = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        #print(mouse.get_pos())
        #print(cordx,cordy)
        #print(g_press1, g_press2)
        g_press1 = False
        g_press2 = False
        window.blit(background,(0,0))
        white.draw(window)
        black.draw(window)
        green.draw(window)
        white.update()
        
        Lb = mouse.get_pressed()[0]
        
        green.update()


    white.update()
    cursor.update()
    display.update()
    clock.tick(FPS)