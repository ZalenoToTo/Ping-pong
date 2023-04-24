from pygame import *
clock = time.Clock()
FPS = 60 
window = display.set_mode((800,300))
display.set_caption('Ping-pong')


class Gsprite(sprite.Sprite):
    def __init__(self,x,y,speed,img,width,heith):
        super().__init__()
        self.width = width
        self.heith = heith
        self.image=transform.scale(image.load(img),(self.width,self.heith))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class HeroSprite(Gsprite):
    def __init__(self,x,y,speed,img,width,heith):
        super().__init__(x,y,speed,img,width,heith)
       
    def update1(self):
        keys_pressed = key.get_pressed()
        if  keys_pressed[K_a] and self.rect.y>0:
            self.rect.y -= self.speed
        if  keys_pressed[K_d] and self.rect.y<725:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if  keys_pressed[K_UP] and self.rect.y>0:
            self.rect.y -= self.speed
        if  keys_pressed[K_DOWN] and self.rect.y<725:
            self.rect.y += self.speed
player = HeroSprite(20,50,4,'Игрок.png',20,80)
player2 = HeroSprite(750,50,4,'Игрок.png',20,80)
game = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    player.draw()
    player.update1()
    player2.draw()
    player2.update2()
    clock.tick(FPS)
    display.update()