# coding=utf-8
import pygame
import random
pygame.init()
window = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Knight DEMO')
# Шрифт
font = pygame.font.Font("ttf/pixel.ttf", 15)
# Бег
RunRight = [pygame.image.load('animation/_RUN_000-removebg-preview.png'),pygame.image.load('animation/_RUN_001-removebg-preview.png'),
pygame.image.load('animation/_RUN_002-removebg-preview.png'),pygame.image.load('animation/_RUN_003-removebg-preview.png'),
pygame.image.load('animation/_RUN_004-removebg-preview.png'),pygame.image.load('animation/_RUN_005-removebg-preview.png'),
pygame.image.load('animation/_RUN_006-removebg-preview.png')]
# Атака
AttackAnimation = [pygame.image.load('animation/ATTACK_000-removebg-preview.png'),pygame.image.load('animation/ATTACK_001-removebg-preview.png'),
pygame.image.load('animation/ATTACK_002-removebg-preview.png'),pygame.image.load('animation/ATTACK_003-removebg-preview.png'),
pygame.image.load('animation/ATTACK_004-removebg-preview.png'),pygame.image.load('animation/ATTACK_005-removebg-preview.png'),
pygame.image.load('animation/ATTACK_006-removebg-preview.png')]
# Бездействие
PlayerStand = [pygame.image.load('animation/_IDLE_000-removebg-preview.png'),pygame.image.load('animation/_IDLE_001-removebg-preview.png'),
pygame.image.load('animation/_IDLE_002-removebg-preview.png'),pygame.image.load('animation/_IDLE_003-removebg-preview.png'),
pygame.image.load('animation/_IDLE_004-removebg-preview.png'),pygame.image.load('animation/_IDLE_005-removebg-preview.png'),
pygame.image.load('animation/_IDLE_006-removebg-preview.png')]
# Прыжок
JumpAnimation = [pygame.image.load('animation/_JUMP_000-removebg-preview.png'),pygame.image.load('animation/_JUMP_001-removebg-preview.png'),
pygame.image.load('animation/_JUMP_002-removebg-preview.png'),pygame.image.load('animation/_JUMP_003-removebg-preview.png'),
pygame.image.load('animation/_JUMP_004-removebg-preview.png'),pygame.image.load('animation/_JUMP_005-removebg-preview.png'),
pygame.image.load('animation/_JUMP_006-removebg-preview.png')]
# Фон
bg= pygame.image.load('BG/bg.jpg')
# Бомбы ?!
bomb = pygame.image.load('mob/bomb.png')
"""Размеры нашего игрока"""
player_widht = 40
player_height = 40

def WinDraw():
    global anime
    window.blit(bg,(0,0))
    if anime + 1 >= 30:
        anime = 0
    if run_right:
        window.blit(RunRight[anime//5],(x,y))
        anime+=1
    if left:
        window.blit(RunRight[anime//5],(x,y))
        anime+=1
    if left == False and run_right == False and jump == False and Attack == False:
        window.blit(PlayerStand[anime//5],(x,y))
        anime+=1
    if jump:
        window.blit(JumpAnimation[anime//5],(x,y))
        anime+=1
    if Attack:
        window.blit(AttackAnimation[anime//5],(x,y))
        anime+=1
    window.blit(font.render('GAME : '
    ' Fantasy Knight', -1, (255,0,0)), (50, 10))
    all_sprites.update()
    all_sprites.draw(window)
    pygame.display.update()


x = 90
y = 480
widht = 85
height = 60
jump_h = 5
run_speed = 10
run_right = False
left = False
walk_right = False
Attack = False
jump = False
anime = 0
"""Логика врагов"""
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1280 - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > 720 + 10 or self.rect.left < -25 or self.rect.right > 1280 + 20:
            self.rect.x = random.randrange(1280 - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
q = True
clock = pygame.time.Clock()
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
"""Основной цикл"""
while q == True:
    clock.tick(30)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            q = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x > 1:
        x-=run_speed
        left = True
        run_right = True
    elif keys[pygame.K_d] and x < 1250:
        x+=run_speed
        run_right = True
        left = False
    else:
        run_right = False
        left = False
        anime = 0
    if not(jump):
        if keys[pygame.K_w]:
            jump = True
    else:
        if jump_h >= -5:
            if jump_h <0:
                y+=(jump_h**2)/2
            else:
                y-=(jump_h**2)/2
            jump_h -=1
        else:
            jump = False
            jump_h = 5
    if not(Attack):
        if keys[pygame.K_s]:
            Attack = True
    else:
        Attack = False
    WinDraw()
pygame.quit()

 # Смерть
# PlayerDie = [pygame.image.load('_DIE_000-removebg-preview.png'),pygame.image.load('_DIE_001-removebg-preview.png'),
# pygame.image.load('_DIE_002-removebg-preview.png'),pygame.image.load('_DIE_003-removebg-preview.png'),
# pygame.image.load('_DIE_004-removebg-preview.png'),pygame.image.load('_DIE_005-removebg-preview.png'),
# pygame.image.load('_DIE_006-removebg-preview.png')]
# Добавлю вместе с мобами
# Условия смерти:
# когда координаты игрока + его ширина + высота совпдают с координатами врага+ширина врага + высота врага
# тогда проигрываем анимацию смерти
