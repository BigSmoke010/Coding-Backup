import pygame

pygame.init()
cell_size = 50
cell_number = 8
screen = pygame.display.set_mode((
    cell_number * cell_size,
    cell_number * cell_size,
))
pygame.display.set_caption('chess')
whitepeon = pygame.image.load('images/Chess_plt45.svg').convert_alpha()
blackpeon = pygame.image.load('images/Chess_pdt45.svg').convert_alpha()
whitepeonlist = [
    pygame.Rect(0 * cell_size, 1 * cell_size, cell_size, cell_size),
    pygame.Rect(1 * cell_size, 1 * cell_size, cell_size, cell_size),
    pygame.Rect(2 * cell_size, 1 * cell_size, cell_size, cell_size),
    pygame.Rect(3 * cell_size, 1 * cell_size, cell_size, cell_size),
    pygame.Rect(4 * cell_size, 1 * cell_size, cell_size, cell_size),
    pygame.Rect(5 * cell_size, 1 * cell_size, cell_size, cell_size),
    pygame.Rect(6 * cell_size, 1 * cell_size, cell_size, cell_size),
    pygame.Rect(7 * cell_size, 1 * cell_size, cell_size, cell_size)
]
blackpeonlist = [
    pygame.Rect(0 * cell_size, 6 * cell_size, cell_size, cell_size),
    pygame.Rect(1 * cell_size, 6 * cell_size, cell_size, cell_size),
    pygame.Rect(2 * cell_size, 6 * cell_size, cell_size, cell_size),
    pygame.Rect(3 * cell_size, 6 * cell_size, cell_size, cell_size),
    pygame.Rect(4 * cell_size, 6 * cell_size, cell_size, cell_size),
    pygame.Rect(5 * cell_size, 6 * cell_size, cell_size, cell_size),
    pygame.Rect(6 * cell_size, 6 * cell_size, cell_size, cell_size),
    pygame.Rect(7 * cell_size, 6 * cell_size, cell_size, cell_size)
]
whiteking = pygame.image.load('images/Chess_klt45.svg').convert_alpha()
whitekingrect = pygame.rect.Rect(3 * cell_size, 0 * cell_size, cell_size,
                                 cell_size)
blackking = pygame.image.load('images/Chess_kdt45.svg').convert_alpha()
blackkingrect = pygame.rect.Rect(3 * cell_size, 7 * cell_size, cell_size,
                                 cell_size)
whitehorse = pygame.image.load('images/Chess_nlt45.svg').convert_alpha()
blackhorse = pygame.image.load('images/Chess_ndt45.svg').convert_alpha()
whitetower = pygame.image.load('images/Chess_rlt45.svg').convert_alpha()
blacktower = pygame.image.load('images/Chess_rdt45.svg').convert_alpha()
whiteslave = pygame.image.load('images/Chess_blt45.svg').convert_alpha()
blackslave = pygame.image.load('images/Chess_bdt45.svg').convert_alpha()
highlightimg = pygame.image.load('images/highlight.png').convert_alpha()
redrect = pygame.draw.rect(screen, 'red',
                           pygame.rect.Rect(10, 10, cell_size, cell_size))
allrects = blackpeonlist + whitepeonlist + [blackkingrect] + [whitekingrect]
selectedindex = 0

stat = 'white'
selected = any
showsuggests = False


def drawboard():
    firstcol = '#72ae50'
    for x in range(cell_number):
        if x % 2 == 0:
            for i in range(cell_number):
                if i % 2 == 0:
                    grasrect = pygame.Rect(i * cell_size, x * cell_size,
                                           cell_size, cell_size)
                    pygame.draw.rect(screen, firstcol, grasrect)
        else:
            for i in range(cell_number):
                if i % 2 != 0:
                    grasrect = pygame.Rect(i * cell_size, x * cell_size,
                                           cell_size, cell_size)
                    pygame.draw.rect(screen, firstcol, grasrect)


def highlight(x):
    global redrect, stat, selectedindex, showsuggests, blackkingrect, whitekingrect
    if showsuggests:

        if stat == 'white':
            for index, i in enumerate(whitepeonlist):
                if i == x:
                    selectedindex = index
                    if x.y == 1 * cell_size:
                        redrect = [
                            pygame.draw.rect(
                                screen, 'red',
                                pygame.rect.Rect(x.x, x.y + 50, cell_size,
                                                 cell_size)),
                            pygame.draw.rect(
                                screen, 'red',
                                pygame.rect.Rect(x.x, x.y + 100, cell_size,
                                                 cell_size))
                        ]
                    else:
                        redrect = [
                            pygame.draw.rect(
                                screen, 'red',
                                pygame.rect.Rect(x.x, x.y + 50, cell_size,
                                                 cell_size))
                        ]
            if x == whitekingrect:
                selectedindex = 17
                redrect = [
                    pygame.draw.rect(
                        screen, 'red',
                        pygame.rect.Rect(x.x + 50, x.y, cell_size, cell_size)),
                    pygame.draw.rect(
                        screen, 'red',
                        pygame.rect.Rect(x.x - 50, x.y, cell_size, cell_size)),
                    pygame.draw.rect(
                        screen, 'red',
                        pygame.rect.Rect(x.x, x.y + 50, cell_size, cell_size)),
                    pygame.draw.rect(
                        screen, 'red',
                        pygame.rect.Rect(x.x, x.y - 50, cell_size, cell_size)),
                    pygame.draw.rect(
                        screen, 'red',
                        pygame.rect.Rect(x.x + 50, x.y + 50, cell_size,
                                         cell_size)),
                    pygame.draw.rect(
                        screen, 'red',
                        pygame.rect.Rect(x.x + 50, x.y - 50, cell_size,
                                         cell_size)),
                    pygame.draw.rect(
                        screen, 'red',
                        pygame.rect.Rect(x.x - 50, x.y + 50, cell_size,
                                         cell_size)),
                    pygame.draw.rect(
                        screen, 'red',
                        pygame.rect.Rect(x.x - 50, x.y - 50, cell_size,
                                         cell_size))
                ]
        elif stat == 'black':
            for index, i in enumerate(blackpeonlist):
                if i == x:
                    selectedindex = index
                    if x.y == 6 * cell_size:
                        redrect = [
                            pygame.draw.rect(
                                screen, 'red',
                                pygame.rect.Rect(x.x, x.y - 50, cell_size,
                                                 cell_size)),
                            pygame.draw.rect(
                                screen, 'red',
                                pygame.rect.Rect(x.x, x.y - 100, cell_size,
                                                 cell_size))
                        ]
                    else:
                        redrect = [
                            pygame.draw.rect(
                                screen, 'red',
                                pygame.rect.Rect(x.x, x.y - 50, cell_size,
                                                 cell_size))
                        ]
            if x == blackkingrect:
                selectedindex = 16
                redrect = [
                    pygame.draw.rect(
                        screen, 'red',
                        pygame.rect.Rect(x.x + 50, x.y, cell_size, cell_size)),
                    pygame.draw.rect(
                        screen, 'red',
                        pygame.rect.Rect(x.x - 50, x.y, cell_size, cell_size)),
                    pygame.draw.rect(
                        screen, 'red',
                        pygame.rect.Rect(x.x, x.y + 50, cell_size, cell_size)),
                    pygame.draw.rect(
                        screen, 'red',
                        pygame.rect.Rect(x.x, x.y - 50, cell_size, cell_size)),
                    pygame.draw.rect(
                        screen, 'red',
                        pygame.rect.Rect(x.x + 50, x.y + 50, cell_size,
                                         cell_size)),
                    pygame.draw.rect(
                        screen, 'red',
                        pygame.rect.Rect(x.x + 50, x.y - 50, cell_size,
                                         cell_size)),
                    pygame.draw.rect(
                        screen, 'red',
                        pygame.rect.Rect(x.x - 50, x.y + 50, cell_size,
                                         cell_size)),
                    pygame.draw.rect(
                        screen, 'red',
                        pygame.rect.Rect(x.x - 50, x.y - 50, cell_size,
                                         cell_size))
                ]

        screen.blit(highlightimg, x)

        for i in redrect:
            if i.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    if stat == 'black':
                        for rect in allrects:
                            if rect == i:
                                print('ok')
                                allrects.remove(rect)
                                for whiterect in whitepeonlist:
                                    if whiterect == i:
                                        whitepeonlist.remove(whiterect)     
                                
                                if whitekingrect == i:
                                    print('game over , black is the winner')                           
                        if selectedindex < 16:
                            blackpeonlist[selectedindex] = i
                            allrects[selectedindex] = i
                            print(allrects)
                        else:
                            if x == blackkingrect:
                                blackkingrect = i

                            allrects[selectedindex] = i
                        stat = 'white'
                        showsuggests = False
                    elif stat == 'white':
                        for rect in allrects:
                            if rect == i:
                                allrects.remove(rect)
                                for blackrect in blackpeonlist:
                                    if blackrect == i:
                                        blackpeonlist.remove(blackrect)     
                                
                                if blackkingrect == i:
                                    print('game over , black is the winner')   
                        if selectedindex < 16:
                            whitepeonlist[selectedindex] = i
                            allrects[selectedindex - 8] = i
                        else:
                            if x == whitekingrect:
                                whitekingrect = i

                            allrects[selectedindex] = i
                        stat = 'black'
                        showsuggests = False


running = True
while running:
    screen.fill('#FFFFFF')
    drawboard()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in blackpeonlist:
        screen.blit(blackpeon, i)
        if stat == 'black':
            if i.collidepoint(pygame.mouse.get_pos()):
                selected = i
                showsuggests = True

    for i in whitepeonlist:
        screen.blit(whitepeon, i)
        if stat == 'white':
            if i.collidepoint(pygame.mouse.get_pos()):
                selected = i
                showsuggests = True
    if stat == 'black':
        if blackkingrect.collidepoint(pygame.mouse.get_pos()):
            selected = blackkingrect
            showsuggests = True
    if stat == 'white':
        if whitekingrect.collidepoint(pygame.mouse.get_pos()):
            selected = whitekingrect
            showsuggests = True

    highlight(selected)

    screen.blit(blackking, blackkingrect)
    screen.blit(whiteking, whitekingrect)
    pygame.display.update()
    pygame.time.Clock().tick(60)
