import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

space = pygame.image.load("images/1.webp").convert_alpha()
space = pygame.transform.scale(space, (800, 600))

player = pygame.image.load("images/space.png").convert_alpha()
playerect = player.get_rect(topleft=[400, 500])

bullet = pygame.image.load("images/circle.png").convert_alpha()
bulletrect = bullet.get_rect(topleft=[playerect.x, 500])

bullet2 = pygame.image.load("images/circle.png").convert_alpha()
bullet2 = pygame.transform.rotate(bullet2, 30)
bulletrect2 = bullet2.get_rect(topleft=[playerect.x, 500])

bullet3 = pygame.image.load("images/circle.png").convert_alpha()
bullet3 = pygame.transform.rotate(bullet3, -30)
bulletrect3 = bullet3.get_rect(topleft=[playerect.x, 500])

warning_sign = pygame.image.load("images/warning.png").convert_alpha()
warning_sign = pygame.transform.scale(warning_sign, (50, 50))

bonus = pygame.image.load("images/Untitled.png").convert_alpha()
bonusrect = bonus.get_rect(topleft=[randint(0, 800), 0])

running = True
deployed = False

userevent = pygame.USEREVENT + 1
pygame.time.set_timer(userevent, 5000)

font = pygame.font.Font("Fonts/Minecrafter.Reg.ttf", 50)

bonusss = False
bonusfunc = False

gravitix = 0

enemy = []
enemyrect = []
enemyx = []
gravity = []

num_of_enemies = 6

bullet_shoot = pygame.mixer.Sound("Sounds/Laser_shoot 4.wav")
dead = pygame.mixer.Sound("Sounds/Explosion 7.wav")
warn = pygame.mixer.Sound("Sounds/Random 12.wav")

for i in range(num_of_enemies):
    enemy.append(pygame.image.load("images/alien1.png").convert_alpha())
    x = randint(0, 750)
    y = randint(0, 400)
    enemyrect.append(enemy[0].get_rect(topleft=(x, y)))
    enemyx.append(5)
    gravity.append(50)

shoted = False
shoted1 = False

bonusx = 2
bonusy = 2

game = 1
score = 0
number_of_shots = 0


def spawnbonus(x):
    global deployed
    if x == 1:
        deployed = True
        screen.blit(bonus, bonusrect)


def multiplebullets(x):
    global shoted1

    if bonusss:
        bulletrect.x = x + 18
        if not shoted1:
            bulletrect2.x = x
            bulletrect3.x = x + 36
        screen.blit(bullet, bulletrect)
        screen.blit(bullet2, bulletrect2)
        screen.blit(bullet3, bulletrect3)
        shoted1 = True


def shoot(x):
    global shoted

    bulletrect.x = x + 18
    screen.blit(bullet, bulletrect)
    shoted = True


while running:
    screen.fill("#000000")
    screen.blit(space, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    gravitix += 10
                if event.key == pygame.K_LEFT:
                    gravitix -= 10
                if event.key == pygame.K_UP and not shoted and not bonusss:
                    meow = playerect.x
                    shoot(meow)
                    bullet_shoot.play()
                if event.key == pygame.K_UP and bonusss and not shoted1:
                    meiw = playerect.x
                    multiplebullets(meiw)
                    bonusfunc = True
                    number_of_shots += 1
                    shoted1 = True
            if event.type == userevent:
                if not deployed:
                    decide = randint(0, 1)
                    spawnbonus(decide)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    gravitix = 0

        elif game == 2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    score -= score
                    bonusss = False
                    bonusfunc = False
                    number_of_shots = 0
                    game = 1

    if game == 1:
        playerect.x += gravitix
        screen.blit(player, playerect)
        if playerect.x >= 750:
            gravitix = 0
        if playerect.x <= 0:
            gravitix = 0

        if deployed:
            spawnbonus(decide)
            bonusrect.x += bonusx
            bonusrect.y += bonusy

            bonusmode = playerect.colliderect(bonusrect)
            if bonusmode and not shoted:
                if bonusfunc:
                    pass
                else:
                    bonusss = True
            if bonusrect.x >= 750:
                bonusx = -5
            if bonusrect.x <= 0:
                bonusx = 5
            if bonusrect.y >= 600:
                bonusrect.y = 0
                deployed = False

        if number_of_shots == 6:
            bonusfunc = False
            bonusss = False
            shoted1 = False
            bulletrect.y = 500
            bulletrect3.y = 500
            bulletrect3.x = 400
            bulletrect2.y = 500
            bulletrect2.x = 400

            number_of_shots -= number_of_shots

        for i in range(num_of_enemies):
            screen.blit(enemy[i], enemyrect[i])
            enemyrect[i].x += enemyx[i]
            if enemyrect[i].x >= 750:
                enemyx[i] = -5
                enemyrect[i].y += gravity[i]
            if enemyrect[i].x <= 0:
                enemyx[i] = 5
                enemyrect[i].y += gravity[i]
            buletcolide = bulletrect.colliderect(enemyrect[i])
            bullet2colide = bulletrect2.colliderect(enemyrect[i])
            bullet3colide = bulletrect3.colliderect(enemyrect[i])
            if enemyrect[i].y >= 400:
                screen.blit(warning_sign, (0, 420))
                screen.blit(warning_sign, (750, 420))
                warn.play()

            if enemyrect[i].y >= 450:
                warn.stop()
                enemyrect[i].y = 0
                game = 2
            if buletcolide or bullet2colide or bullet3colide:
                redalen = pygame.image.load("images/alien2.png")
                screen.blit(redalen, enemyrect[i])
                enemyrect[i].x = randint(0, 750)
                enemyrect[i].y = randint(0, enemyrect[i].y)
                dead.play()
                score += 1
                screen.blit(fontscore, (350, 40))

        fontscore = font.render(str(score), False, "white")
        screen.blit(fontscore, (350, 40))

        if shoted and not bonusfunc:
            shoot(meow)
            bulletrect.y -= 10

        if bonusfunc and shoted1:
            multiplebullets(meiw)
            bulletrect.y -= 10
            bulletrect2.y -= 10
            bulletrect2.x -= 5
            bulletrect3.y -= 10
            bulletrect3.x += 5

        if bulletrect.y <= 0 and not bonusss:
            bulletrect.y = 500
            shoted = False

        if (bulletrect.y <= 0 and bonusss and bulletrect2.x <= 0
                and bulletrect3.x >= 800):
            bulletrect.y = 500
            bulletrect3.y = 500
            bulletrect3.x = 400
            bulletrect2.y = 500
            bulletrect2.x = 400
            shoted1 = False

        if bulletrect.y <= 0 and bonusss and bulletrect2.y <= 0 and bulletrect3.y <= 0:
            bulletrect.y = 500
            bulletrect3.y = 500
            bulletrect3.x = 400
            bulletrect2.y = 500
            bulletrect2.x = 400
            shoted1 = False

    elif game == 2:
        gameovertxt = font.render("GAME OVER", False, "#921818")
        screen.blit(gameovertxt, (210, 300))
        scoretxt = font.render("Final Score:", False, "#F6FF25")
        screen.blit(scoretxt, (200, 150))
        scorertxt = font.render(str(score), False, "#25FF37")
        screen.blit(scorertxt, (350, 200))
        scorertxt = font.render("press r to restart", False, "#921818")
        screen.blit(scorertxt, (100, 400))

    elif game == 0:
        print("title screen")

    pygame.display.update()
    clock.tick(60)
