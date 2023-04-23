from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,picture,w,h,x,y):
        super().__init__()
        self.image=transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y,size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    def update(self):
        if player.rect.x <= win_width-80 and player.x_speed > 0 or player.rect.x >= 0 and player.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0: 
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left) 
        elif self.x_speed < 0: 
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if player.rect.y <= win_height-80 and player.y_speed > 0 or player.rect.y >= 0 and player.y_speed < 0:
            self.rect.y += self.y_speed
            platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: 
            for p in platforms_touched:
                self.y_speed = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0: 
            for p in platforms_touched:
                self.y_speed = 0  
                self.rect.top = max(self.rect.top, p.rect.bottom) 
class Enemy(GameSprite):
    direction = 'left'
    def __init__(self, player_image, player_x, player_y, size_x, size_y , player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self): 
        if self.rect.x <= 350:
            self.direction = 'right'
        if self.rect.x >= win_width - 150 :
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed        
win_width=700
win_height = 500
back = (50, 255, 100)
window = display.set_mode((win_width, win_height))
window.fill(back)
display.set_caption('GTA VI')
health = GameSprite('health.png',190,130,20,-22 )
w_1 = GameSprite('tree.png',55,55,200,250)
w_2 = GameSprite('tree.png',60,60,135,205)
w_3 = GameSprite('tree.png',55,55,230,280)
w_4 = GameSprite('tree.png',55,55,290,320)
w_5 = GameSprite('tree.png',55,55,200,190)
w_6 = GameSprite('tree.png',60,60,100,230)
w_7 = GameSprite('tree.png',55,55,50,300)
w_8 = GameSprite('tree.png',55,55,150,260)
w_9 = GameSprite('tree.png',55,55,70,200)
w_10 = GameSprite('tree.png',55,55,230,300)
w_11 = GameSprite('tree.png',55,55,110,290)
w_12 = GameSprite('tree.png',55,55,150,350)
pigs = sprite.Group()
player = Player('human.png',60, 60, 50, 400, 0, 0)
final = GameSprite('house.png',83, 83, 600 , 370)
farm = GameSprite('farm.png',83, 83, 550 , 30)
pig1 = Enemy('pig.png',60, 60, 500 , 100, 5)
pig2 = Enemy('pig.png',55, 55, 570 , 130, 5)
pigs.add(pig1)
pigs.add(pig2)
barriers = sprite.Group()
barriers.add(w_1)
barriers.add(w_2)
run = True
finish = False
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
               player.x_speed = -5
            elif e.key == K_RIGHT:
                player.x_speed = 5
            elif e.key == K_UP:
                player.y_speed = -5
            elif e.key == K_DOWN:
                player.y_speed = 5
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                player.x_speed = 0
            elif e.key == K_RIGHT:
                player.x_speed = 0
            elif e.key == K_UP:
                player.y_speed = 0
            elif e.key == K_DOWN:
                player.y_speed = 0
    if finish != True:
        window.fill(back)
        w_1.reset()
        w_2.reset()
        w_3.reset()
        w_4.reset()
        w_5.reset()
        w_6.reset()
        w_7.reset()
        w_8.reset() 
        w_9.reset() 
        w_10.reset()
        w_11.reset()
        w_12.reset()
        final.reset()
        player.reset()
        farm.reset()
        pig1.reset()
        pig2.reset()
        health.reset()

        player.reset()
        player.update()
        pig1.update()
        pig2.update()
        if sprite.spritecollide(player, pigs, False):
            finish = True
            img = image.load('over.jpg')
            d = img.get_width() // img.get_height()
            window.fill((255,255,255))
            window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))

        if sprite.collide_rect(player, final):
            finish = True
            img = image.load('win.jpg')
            window.fill((255,255,255))
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
        display.update()


    
