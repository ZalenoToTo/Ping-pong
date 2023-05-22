from pygame import *
clock = time.Clock()
FPS = 60 
font.init()
font_for_win = font.Font(None,65)
font_for_count = font.Font(None,65)
window = display.set_mode((1024,512))
display.set_caption('Ping-pong')

createRect = 0
cleaneRect = 0
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
        if  keys_pressed[K_w] and self.rect.y>0 and p1w < 7:
            self.rect.y -= self.speed
        if  keys_pressed[K_s] and self.rect.y<412 and p1w < 7:
            self.rect.y += self.speed
        if  keys_pressed[K_s] and self.rect.y>0 and p1w >= 7:
            self.rect.y -= self.speed
        if  keys_pressed[K_w] and self.rect.y<412 and p1w >= 7:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if  keys_pressed[K_UP] and self.rect.y>0 and p2w < 7:
            self.rect.y -= self.speed
        if  keys_pressed[K_DOWN] and self.rect.y<412 and p2w < 7:
            self.rect.y += self.speed
        if  keys_pressed[K_DOWN] and self.rect.y>0 and p2w < 7:
            self.rect.y -= self.speed
        if  keys_pressed[K_UP] and self.rect.y<412 and p2w < 7:
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
background = transform.scale(image.load('fon-pattern.png'),(1024,512))
player = HeroSprite(16,64,4,'Player.png',40,100)
player2 = HeroSprite(970,64,4,'Player.png',40,100)
ball = Ball(512,256,8,'Ball.png',90,90,10)
game = True
finish = True
imgSurf = None
p1w = 4
p2w = 0

bool1 = True
count1 = font_for_count.render(
    "1st Player's wins"+str(p1w), True, (0,0,0)
)
count2 = font_for_count.render(
    "2nd Player's wins"+str(p2w), True, (0,0,0)
)
while game:
    for i in event.get():
        if i.type == QUIT:
                game = False
    if finish :
        if ball.rect.x > 1024 :
            p1w+=1
            count1 = font_for_count.render(
                "1st Player's wins: "+str(p1w), True, (0,0,0)
            )
            ball.rect.x,ball.rect.y = 512,256
        if  ball.rect.x < 0  :
            p2w+=1
            count2 = font_for_count.render(
                "2nd Player's wins: "+str(p2w), True, (0,0,0)
            )
            ball.rect.x,ball.rect.y = 512,256
        if p1w > 6 or p2w >6:
            if  new_ball.rect.x > 1024:
                p1w+=1
                count1 = font_for_count.render(
                    "1st Player's wins: "+str(p1w), True, (0,0,0)
                )
                new_ball.rect.x,new_ball.rect.y = 512,256
            if   new_ball.rect.x < 0:
                p2w+=1
                count2 = font_for_count.render(
                    "2nd Player's wins: "+str(p2w), True, (0,0,0)
                )
                new_ball.rect.x,new_ball.rect.y = 512,256
        if (6>p1w > 4 or 4 < p2w < 6) and bool1:
            new_ball=Ball(512,256,6,'Ball.png',50,50,12)
            bool1 = False
            
        window.blit(background,(0,0))
        ball.draw()
        ball.update()
        player.draw()
        player.update1()
        player2.draw()
        player2.update2()
        if p1w > 6 or p2w >6:
            new_ball.draw()
            new_ball.update()
        try:
            window.blit(imgSurf,(0,0))
        except:
            pass
        
            
        window.blit(count1,(30,30))
        window.blit(count2,(30,90))
        
        if p1w > 3 or p2w > 3:
            createRect+=1
            print(createRect)
            if createRect == 1_620 and imgSurf == None:
                imgSurf = Surface((1024,512))
                imgSurf.fill((200,0,200))
            if createRect == 1_800:
                imgSurf= None
                createRect = 0
                print(imgSurf)
       
        clock.tick(FPS)
        
        if p1w >90 :
            defeat = font_for_win.render(
                    "1st player win!",True,(155,92,103)
                )
            window.blit(defeat,(470,250))
            finish = False
        if  p2w >90:
            defeat = font_for_win.render(
                    "2nd player win!",True,(155,92,103)
                )
            window.blit(defeat,(470,250))
            finish = False
        display.update()
    
