import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("runnin")

clock = pygame.time.Clock()

background = pygame.image.load(
    "./images/runin/cartoon orange autumn leaves.jpg"
).convert_alpha()
enemy = pygame.image.load(
    "./images/runin/mushroom.png").convert_alpha(
    )
enemy = pygame.transform.scale(enemy, (50, 50))
enemy1 = pygame.image.load(
    "./images/runin/mushroom.png").convert_alpha(
    )
enemy1 = pygame.transform.scale(enemy, (50, 50))
enemy2 = pygame.image.load(
    "./images/runin/mushroom.png").convert_alpha(
    )
enemy2 = pygame.transform.scale(enemy, (50, 50))
bomb = pygame.image.load(
    "./images/runin/Bomb.png").convert_alpha()
bomb = pygame.transform.scale(bomb, (30, 50))
flyingenemy = pygame.image.load(
    "./images/runin/eagle.png").convert_alpha()
flyingenemy = pygame.transform.scale(flyingenemy, (50, 50))
ground = pygame.image.load(
    "./images/runin/ground.png").convert_alpha()
heroz = pygame.image.load(
    "./images/runin/superhero.png"
).convert_alpha()
walkin1 = pygame.image.load(
    "./images/runin/walkin1.png").convert_alpha(
    )
walkin1 = pygame.transform.scale(walkin1, (50, 50))
walkin2 = pygame.image.load(
    "./images/runin/walkin2.png").convert_alpha(
    )
walkin2 = pygame.transform.scale(walkin2, (50, 50))
walkindex = 1
walks = [walkin1, walkin2]
hero = walks[walkindex]

x = randint(0, 750)

userevent = pygame.USEREVENT + 1
pygame.time.set_timer(userevent, 100)

flyinrect = flyingenemy.get_rect(topleft=[700, 340])
bombrect = bomb.get_rect(topleft=[x, 10])
enemyrect = enemy.get_rect(topleft=[700, 400])
enemy1rect = enemy1.get_rect(topleft=[bombrect.x, 400])
enemy2rect = enemy1.get_rect(topleft=[bombrect.x, 400])
enemies = [flyinrect, bombrect, enemyrect]
tup = [
    (flyingenemy, flyinrect, "x"),
    (enemy, enemyrect, "x"),
    (bomb, bombrect, "y"),
    (bomb, bombrect, "y"),
]
litup = []
font = pygame.font.Font(
    "./Fonts/ARCADECLASSIC.TTF", 40)
font1 = pygame.font.Font("./Fonts/ARCADE.TTF",
                         40)

score = 0

groundrect = ground.get_rect(topleft=[0, 200])

herorect = hero.get_rect(topleft=[100, 400])
textscore = font.render("Enemies Dodged :" + str(score), False, "blue")
scorerect = textscore.get_rect(center=[400, 100])

game = 3
state = "ground"

speed = 5
gravity = 0
gravitix = 0
startime = 0

runing = True
deployed = False
doubles = False
spawned = False
deployed = False

enemi = any


def deploy(chosen):
    litup.append(tup[chosen])
    screen.blit(litup[0][0], litup[0][1])


def animated():
    global walkindex, hero

    if herorect.y < 400:
        hero = heroz
    elif herorect.bottom == 450:
        walkindex += 0.1
        if walkindex >= len(walks):
            walkindex = 0
        hero = walks[int(walkindex)]


enemmm = randint(0, 3)
deploy(enemmm)

while runing:
    enemmm = randint(0, 3)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if game == 1:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and state == "ground":
                    gravity = -20
                    state = "sky"

                if event.key == pygame.K_RIGHT:
                    gravitix += 10

                if event.key == pygame.K_LEFT:
                    gravitix -= 10
            if event.type == userevent:
                if not deployed:
                    x = randint(0, 750)
                    bombrect.x = x
                    z = bombrect.x
                    if not spawned:
                        enemy1rect.x = z
                        enemy2rect.x = z
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    herorect.top += 1

                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    gravitix = 0

        elif game == 2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game = True
                    enemy1rect.x = 400
                    enemy2rect.x = 400
                    try:
                        if litup[0][2] == "x":
                            litup[0][1].x = 700
                        elif litup[0][2] == "y":
                            litup[0][1].y = 10

                    except Exception:
                        pass

                    herorect.x = 100
                    speed = 5
                    score -= score
                    startime = pygame.time.get_ticks()

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game = 1

    if game == 1:

        screen.blit(background, (0, 0))
        screen.blit(ground, groundrect)
        animated()
        screen.blit(hero, herorect)

        deploy(enemmm)

        collide = herorect.colliderect(litup[0][1])
        if collide:
            game = 2

        if litup[0][2] == "x":
            deploy(enemmm)
            litup[0][1].x -= speed
            if litup[0][1].x <= 0:
                litup[0][1].x = 700
                litup.clear()
                score += 1
                speed += 0.1

        elif litup[0][2] == "y":
            deployed = True
            deploy(enemmm)
            litup[0][1].y += speed
            if litup[0][1].y >= 450:
                litup[0][1].y = 10
                litup.clear()
                score += 1
                speed += 0.1
                doubles = True
                deployed = False
        if doubles:
            screen.blit(enemy1, enemy1rect)
            screen.blit(enemy2, enemy2rect)
            enemy1rect.x -= speed
            enemy2rect.x += speed
            collisionn1 = herorect.colliderect(enemy1rect)
            collisionn2 = herorect.colliderect(enemy2rect)
            spawned = True
            if collisionn1 or collisionn2:
                game = 2
            if enemy1rect.x <= 0:
                doubles = False
                spawned = False
                enemy1rect.x = bombrect.x
                enemy2rect.x = bombrect.x

        gravity += 1
        herorect.y += gravity
        herorect.x += gravitix

        if herorect.bottom >= 450:
            herorect.bottom = 450
            state = "ground"

        if herorect.x >= 800:
            herorect.x = 800
        elif herorect.x <= 0:
            herorect.x = 0

        textscore = font.render("Enemies  dodged  " + str(score), False,
                                "#9DCC18")
        screen.blit(textscore, scorerect)

        x = pygame.time.get_ticks()

    elif game == 2:
        x = pygame.time.get_ticks() - startime
        screen.fill("black")
        text = font.render("GAME OVER", False, "#FF2929")
        textr = font1.render("(press R to restart)", False, "#2941FF")
        texxts = font1.render(
            "you lasted " + str(int(x / 1000)) + " seconds !", False,
            "#C8D81C")
        screen.blit(text, (280, 200))
        screen.blit(textr, (200, 300))
        screen.blit(texxts, (170, 150))

    elif game == 3:
        screen.fill("#4A1EFF")
        herobg = pygame.image.load(
            "./images/runin/City-Cartoon-Wallpaper.jpg"
        )
        herobg = pygame.transform.scale(herobg, (800, 600))
        screen.blit(herobg, (0, 0))

        heroimg = pygame.image.load(
            "./images/runin/Untitled.png")
        screen.blit(heroimg, (-20, 0))

        gametitle = font.render("runner", False, "#89FF1E")
        screen.blit(gametitle, (320, 100))

        startinstr = font1.render("Click Here or press S to Start", False,
                                  "#5A840C")
        startrec = startinstr.get_rect(topleft=[150, 400])
        screen.blit(startinstr, startrec)
        x = startrec.collidepoint(pygame.mouse.get_pos())
        y = pygame.mouse.get_pressed()
        if x:
            pygame.draw.rect(screen, "red", startrec)
            screen.blit(startinstr, startrec)
        if x and y[0]:
            game = 1

    pygame.display.update()
    clock.tick(60)
