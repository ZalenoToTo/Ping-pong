from pygame import *
clock = time.Clock()
FPS = 60 
font.init()
font = font.Font(None,45)
window = display.set_mode((1024,512))
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
        if  keys_pressed[K_w] and self.rect.y>0:
            self.rect.y -= self.speed
        if  keys_pressed[K_s] and self.rect.y<412:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if  keys_pressed[K_UP] and self.rect.y>0:
            self.rect.y -= self.speed
        if  keys_pressed[K_DOWN] and self.rect.y<412:
            self.rect.y += self.speed

    def bot(self,ball):
        ballypossition=ball.rect.y
        rasstoyanie = ball
class Ball(Gsprite):
    def __init__(self,x,y,speed,img,width,heith,speedy):
        super().__init__(x,y,speed,img,width,heith)
        self.speedy = speedy

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speed
        if self.rect.y < 0 or self.rect.y >412:
            self.speedy*=-1
        if Rect.colliderect(self.rect,player.rect) or Rect.colliderect(self.rect,player2.rect):
            
            self.speed*=-1
        print(self.rect.y)
player = HeroSprite(16,64,4,'Player.png',40,100)
player2 = HeroSprite(970,64,4,'Player.png',40,100)
ball = Ball(512,256,8,'Ball.png',60,60,10)
game = True
finish = True
while game:
    for i in event.get():
        if i.type == QUIT:
                game = False
    if finish :
        
        ball.draw()
        ball.update()
        player.draw()
        player.update1()
        player2.draw()
        player2.update2()
        clock.tick(FPS)
        if ball.rect.x > 1024 :
            defeat = font.render(
                    "1st player win!",True,(155,92,103)
                )
            window.blit(defeat,(470,250))
            finish = False
        if  ball.rect.x < 0:
            defeat = font.render(
                    "2nd player win!",True,(155,92,103)
                )
            window.blit(defeat,(470,250))
            finish = False
        display.update()
