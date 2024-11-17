import pygame
pygame.init()
pygame.mixer.init()#zvuk
pygame.mixer.music.load("jungles.ogg")
pygame.mixer.music.play()
#sozdanie ekrana
window = pygame.display.set_mode((700, 500))
#sozdanie fps
fps = pygame.time.Clock()


fon = pygame.image.load("background.jpg")
fon = pygame.transform.scale(fon,(700, 500))


class gameObject(pygame.sprite.Sprite):
    def __init__(self, image, visota, shirina, x, y, speed):
        super().__init__() 
        self.img_sprite = pygame.image.load(image)
        self.img_sprite = pygame.transform.scale(self.img_sprite,(visota, shirina))       
        self.hitbox = self.img_sprite.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.move = ''
    def show(self):
        window.blit(self.img_sprite, self.hitbox)
#БИНД КНОПОК
class gamePlayer(gameObject):
    def upravlenie(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.hitbox.y > 0:
            self.hitbox.y -= self.speed
        if keys[pygame.K_s] and self.hitbox.y < 445:
            self.hitbox.y += self.speed
        if keys[pygame.K_a] and self.hitbox.x > 0:
            self.hitbox.x -= self.speed
        if keys[pygame.K_d] and self.hitbox.x < 645:
            self.hitbox.x += self.speed

class wall(pygame.sprite.Sprite):
    def __init__(self, wall_x, wall_y, wall_shirina, wall_visota, wall_r, wall_g, wall_b):
        super().__init__()     
        self.wall_shirina = wall_shirina
        self.wall_visota = wall_visota
        self.wall_r = wall_r
        self.wall_g = wall_g
        self.wall_b = wall_b

        self.wall_image = pygame.Surface((self.wall_shirina, self.wall_visota))
        self.wall_image.fill((self.wall_r, self.wall_g, self.wall_b))

        self.wall_hitbox = self.wall_image.get_rect()
        self.wall_hitbox.x = wall_x
        self.wall_hitbox.y = wall_y

    def show(self):
        window.blit(self.wall_image, self.wall_hitbox)


player = gamePlayer('hero.png', 55, 45, 20, 400, 3)



gold = gameObject('treasure.png', 60, 60, 610, 400, 0)

#ssteni
w1 = wall(10, 380, 200, 10, 252, 3, 3)
w2 = wall(10, 460, 500, 10, 252, 3, 3)
w3 = wall(510, 380, 10, 90, 252, 3, 3)
w4 = wall(310, 380, 200, 10, 252, 3, 3)
w5 = wall(210, 90, 10, 300, 252, 3, 3)
w6 = wall(10, 80, 210, 10, 252, 3, 3)
w7 = wall(10, 10, 10, 80, 252, 3, 3)
w8 = wall(10, 10, 670, 10, 252, 3, 3)
w9 = wall(680, 10, 10, 400, 252, 3, 3)
w10 = wall(310, 80, 10, 300, 252, 3, 3) 
w11 = wall(310, 80, 280, 10, 252, 3, 3) 
w12 = wall(590, 80, 10, 330, 252, 3, 3)


class Enemy(gameObject):
    def forward(self):
        if self.hitbox.x >= 620:
            self.move = 'left'
        if self.hitbox.x <= 30:
            self.move = "right"
        
        if self.move  == 'left':
            self.hitbox.x -=self.speed
        else:
            self.hitbox.x +=self.speed

enemy = Enemy('cyborg.png', 60, 60, 500, 22, 3.7)  


run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    window.blit(fon,(0, 0))
    player.show()
    player.upravlenie()
    enemy.show()
    gold.show()
    w1.show()
    w2.show()
    w3.show()
    w4.show()
    w5.show()
    w6.show()
    w7.show()
    w8.show()
    w9.show()
    w10.show()
    w11.show()
    w12.show()
    enemy.forward()
    if player.hitbox.colliderect(w1.wall_hitbox) or player.hitbox.colliderect(w2.wall_hitbox) or player.hitbox.colliderect(w2.wall_hitbox) or player.hitbox.colliderect(w3.wall_hitbox) or player.hitbox.colliderect(w4.wall_hitbox) or player.hitbox.colliderect(w5.wall_hitbox) or player.hitbox.colliderect(w6.wall_hitbox) or player.hitbox.colliderect(w7.wall_hitbox) or player.hitbox.colliderect(w8.wall_hitbox) or player.hitbox.colliderect(w9.wall_hitbox) or player.hitbox.colliderect(w10.wall_hitbox) or player.hitbox.colliderect(w11.wall_hitbox) or player.hitbox.colliderect(w12.wall_hitbox) or player.hitbox.colliderect(enemy.hitbox):
        player.hitbox.x =  20
        player.hitbox.y =  400
    pygame.display.update()
    fps.tick(60)
    

