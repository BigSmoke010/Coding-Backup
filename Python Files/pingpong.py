import pygame
from random import choice

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

Player = pygame.image.load(f'/home/walid/Coding/Python Files/images/PingPong/Untitled.png').convert_alpha()
ball = pygame.image.load('images/PingPong/ball.png').convert_alpha()
font = pygame.font.Font('Fonts/Minecrafter.Reg.ttf', 50)
font1 = pygame.font.Font('Fonts/ARCADECLASSIC.TTF', 80)
ballrect = ball.get_rect(topleft = [400, 300])
bottom = Player.get_rect()
enemyrect = Player.get_rect()
preffered_side = 'left'
beep = pygame.mixer.Sound('Sounds/Ping Pong/Blip_select 25.wav')
beep1 = pygame.mixer.Sound('Sounds/Ping Pong/Random 42.wav')

if preffered_side == 'left':
    bottom = Player.get_rect(topleft = [50, 350])
    botmiddle = Player.get_rect(topleft = [50, 325])
    topmiddle = Player.get_rect(topleft = [50, 300])
    top = Player.get_rect(topleft = [50, 275])
    enemybottom = Player.get_rect(topleft = [750, 350])
    enemybotmiddle = Player.get_rect(topleft = [750, 325])
    enemytopmiddle = Player.get_rect(topleft = [750, 300])
    enemytop = Player.get_rect(topleft = [750, 275])

elif preffered_side == 'right':
    bottom = Player.get_rect(topleft = [750, 350])
    botmiddle = Player.get_rect(topleft = [750, 325])
    topmiddle = Player.get_rect(topleft = [750, 300])
    top = Player.get_rect(topleft = [750, 275])
    enemybottom = Player.get_rect(topleft = [50, 350])
    enemybotmiddle = Player.get_rect(topleft = [50, 325])
    enemytopmiddle = Player.get_rect(topleft = [50, 300])
    enemytop = Player.get_rect(topleft = [50, 275])
running = True
locked = True
y = False
game = 2
scoreplayer = 0
scorebot = 0
playergravity = 0
enemygravity = 0
ballgravitx = choice([3, -3]) 
ballgravity = choice([3, -3])
ballspeed = 3

while running:
    screen.fill("#948282")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False           
        if game == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    playergravity = -5
                if event.key == pygame.K_DOWN:
                    playergravity = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playergravity = 0 
            if locked:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        locked = False
        elif game == 2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game = 1
    if game == 1 :
        if locked:
            ballrect.x = 400
            ballrect.y = 300
        ballrect.x += ballgravitx
        if y:
            ballrect.y += ballgravity
            
        bottom.y += playergravity
        botmiddle.y += playergravity
        topmiddle.y += playergravity
        top.y += playergravity
        enemybottom.y += enemygravity
        enemybotmiddle.y += enemygravity
        enemytopmiddle.y += enemygravity
        enemytop.y += enemygravity
        
        if ballrect.y < enemybotmiddle.y:
            enemygravity = -5
        if ballrect.y > enemybotmiddle.y:
            enemygravity = 5
        if ballrect.y == enemybotmiddle.y:
            enemygravity = 0
        if ballrect.y <= 0:
            ballgravity = ballspeed
            beep1.play()
        if ballrect.y >= 570:
            ballgravity = -abs(ballspeed)
            beep1.play()

        bottomcollide = bottom.colliderect(ballrect)
        botmidcollide = botmiddle.colliderect(ballrect)
        topmidcollide = topmiddle.colliderect(ballrect)
        topcollide = top.colliderect(ballrect)
        
        enemybottomcollide = enemybottom.colliderect(ballrect)
        enemybotmidcollide = enemybotmiddle.colliderect(ballrect)
        enemytopmidcollide = enemytopmiddle.colliderect(ballrect)
        enemytopcollide = enemytop.colliderect(ballrect)
    
        if bottomcollide and preffered_side == 'left':
            ballspeed += 0.1
            ballgravitx = ballspeed
            ballgravity  = 5
            y = True
            beep.play()
        if botmidcollide and preffered_side == 'left':
            ballspeed += 0.1
            ballgravitx = ballspeed
            ballgravity  = 1
            y = True
            beep.play()
        if topmidcollide and preffered_side == 'left':
            ballspeed += 0.1
            ballgravitx = ballspeed
            ballgravity = -1
            y = True
            beep.play()
        if topcollide and preffered_side == 'left':
            ballspeed += 0.1
            ballgravitx = ballspeed
            ballgravity = -5
            y = True
            beep.play()
        if bottomcollide and preffered_side == 'right':
            ballspeed += 0.1
            ballgravitx = -abs(ballspeed)
            ballgravity  = 5
            y = True
            beep.play()
        if botmidcollide and preffered_side == 'right':
            ballspeed += 0.1
            ballgravitx = -abs(ballspeed)
            ballgravity  = 1
            y = True
            beep.play()
        if topmidcollide and preffered_side == 'right':
            ballspeed += 0.1
            ballgravitx = -abs(ballspeed)
            ballgravity = -1
            y = True
            beep.play()
        if topcollide and preffered_side == 'right':
            ballspeed += 0.1
            ballgravitx = -abs(ballspeed)
            ballgravity = -5
            y = True
            beep.play()
        
        if enemybottomcollide and preffered_side == 'left':
            ballspeed += 0.1
            ballgravitx = -abs(ballspeed)
            ballgravity  = 5
            y = True
            beep.play()
        if enemybotmidcollide and preffered_side == 'left':
            ballspeed += 0.1
            ballgravitx = -abs(ballspeed)
            ballgravity  = 1
            y = True
            beep.play()
        if enemytopmidcollide and preffered_side == 'left':
            ballspeed += 0.1
            ballgravitx = -abs(ballspeed)
            ballgravity = -1
            y = True
            beep.play()
        if enemytopcollide and preffered_side == 'left':
            ballspeed += 0.1
            ballgravitx = -abs(ballspeed)
            ballgravity = -5
            y = True
            beep.play()
        if enemybottomcollide and preffered_side == 'right':
            ballspeed += 0.1
            ballgravitx = ballspeed
            ballgravity  = 5
            y = True
            beep.play()
        if enemybotmidcollide and preffered_side == 'right':
            ballspeed += 0.1
            ballgravitx = ballspeed
            ballgravity  = 1
            y = True
            beep.play()
        if enemytopmidcollide and preffered_side == 'right':
            ballspeed += 0.1
            ballgravitx = ballspeed
            ballgravity = -1
            y = True
            beep.play()
        if enemytopcollide and preffered_side == 'right':
            ballspeed += 0.1
            ballgravitx = ballspeed
            ballgravity = -5
            y = True
            beep.play()
        
        if top.y <= 0:
            top.y = 0
            playergravity = 0
        if bottom.y >= 585:
            bottom.y = 585
            playergravity = 0
        
        if enemytop.y <= 0:
            enemyrect.y = 0
            enemygravity = 5
        if enemybottom.y >= 585:
            enemyrect.y = 585
            enemygravity = -5
        if ballrect.x >= 749:
            scoreplayer += 1
            locked = True
            y = False
            x = font.render(str(scoreplayer), False, "#FFFFFF", None)
            screen.blit(x, (300, 100))
            ballrect.x = 400
            ballrect.y = 300
            ballgravitx = choice([5, -5]) 
            ballgravity = choice([5, -5])
            ballspeed = 2
        if ballrect.x <= 0:
            scorebot += 1
            locked = True
            y = False
            ballspeed = 2
            z = font.render(str(scorebot), False, "#FFFFFF", None)
            screen.blit(z, (500, 100))
            ballrect.x = 400
            ballrect.y = 300
            ballgravitx = choice([5, -5]) 
            ballgravity = choice([5, -5])
        x = font.render(str(scoreplayer), False, "#FFFFFF", None)
        z = font.render(str(scorebot), False, "#FFFFFF", None)

        screen.blit(x, (300, 100))
        screen.blit(z, (500, 100))
        
        screen.blit(ball, ballrect)
        screen.blit(Player, bottom)
        screen.blit(Player, botmiddle)
        screen.blit(Player, topmiddle)
        screen.blit(Player, top)
        screen.blit(Player, enemybottom)
        screen.blit(Player, enemybotmiddle)
        screen.blit(Player, enemytopmiddle)
        screen.blit(Player, enemytop)

    elif game == 2:
        title = font1.render('PING PONG', False, "orange")
        screen.blit(title, (220, 100))
        title = font1.render('press S to start', False, "yellow")
        screen.blit(title, (110, 400))
    clock.tick(60)
    pygame.display.update()

