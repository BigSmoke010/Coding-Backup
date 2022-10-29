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
whitekingrect = pygame.rect.Rect(4 * cell_size, 0 * cell_size, cell_size,
                                 cell_size)
blackking = pygame.image.load('images/Chess_kdt45.svg').convert_alpha()
blackkingrect = pygame.rect.Rect(4 * cell_size, 7 * cell_size, cell_size,
                                 cell_size)
whitehorse = pygame.image.load('images/Chess_nlt45.svg').convert_alpha()
whitehorserects = [
    pygame.rect.Rect(1 * cell_size, 0 * cell_size, cell_size, cell_size),
    pygame.rect.Rect(6 * cell_size, 0 * cell_size, cell_size, cell_size)
]
blackhorse = pygame.image.load('images/Chess_ndt45.svg').convert_alpha()
blackhorserects = [
    pygame.rect.Rect(1 * cell_size, 7 * cell_size, cell_size, cell_size),
    pygame.rect.Rect(6 * cell_size, 7 * cell_size, cell_size, cell_size)
]
whitetower = pygame.image.load('images/Chess_rlt45.svg').convert_alpha()
whitetowerrects = [
    pygame.rect.Rect(0 * cell_size, 0 * cell_size, cell_size, cell_size),
    pygame.rect.Rect(7 * cell_size, 0 * cell_size, cell_size, cell_size)
]
blacktower = pygame.image.load('images/Chess_rdt45.svg').convert_alpha()
blacktowerrects = [
    pygame.rect.Rect(0 * cell_size, 7 * cell_size, cell_size, cell_size),
    pygame.rect.Rect(7 * cell_size, 7 * cell_size, cell_size, cell_size)
]
whitebishop = pygame.image.load('images/Chess_blt45.svg').convert_alpha()
whitebishoprects = [
    pygame.rect.Rect(2 * cell_size, 0 * cell_size, cell_size, cell_size),
    pygame.rect.Rect(5 * cell_size, 0 * cell_size, cell_size, cell_size)
]
blackbishop = pygame.image.load('images/Chess_bdt45.svg').convert_alpha()
blackbishoprects = [
    pygame.rect.Rect(2 * cell_size, 7 * cell_size, cell_size, cell_size),
    pygame.rect.Rect(5 * cell_size, 7 * cell_size, cell_size, cell_size)
]
blackqueen = pygame.image.load('images/Chess_qdt45.svg').convert_alpha()
blackqueenrect = pygame.rect.Rect(3 * cell_size, 7 * cell_size, cell_size,
                                  cell_size)
whitequeen = pygame.image.load('images/Chess_qlt45.svg').convert_alpha()
whitequeenrect = pygame.rect.Rect(3 * cell_size, 0 * cell_size, cell_size,
                                  cell_size)
highlightimg = pygame.image.load('images/highlight.png').convert_alpha()

redrect = pygame.draw.rect(screen, 'red',
                           pygame.rect.Rect(10, 10, cell_size, cell_size))
selectedindex = 0
allblackdoublerects = blackbishoprects + blacktowerrects + blackhorserects
allwhitedoublerects = whitebishoprects + whitetowerrects + whitehorserects
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


def queenhighlights(x):
    xpos = 50
    ypos = 50
    for pos in range(10):
        redrect.append(
            pygame.draw.rect(
                screen, 'red',
                pygame.rect.Rect(x.x + xpos, x.y, cell_size, cell_size)))
        xpos += 50
    xpos = 50
    for pos in range(10):
        redrect.append(
            pygame.draw.rect(
                screen, 'red',
                pygame.rect.Rect(x.x + xpos, x.y + ypos, cell_size,
                                 cell_size)))
        xpos += 50
        ypos += 50
    ypos = 50
    for pos in range(10):
        redrect.append(
            pygame.draw.rect(
                screen, 'red',
                pygame.rect.Rect(x.x, x.y + ypos, cell_size, cell_size)))
        ypos += 50
    xpos = 50
    ypos = 50
    for pos in range(10):
        redrect.append(
            pygame.draw.rect(
                screen, 'red',
                pygame.rect.Rect(x.x - xpos, x.y + ypos, cell_size,
                                 cell_size)))
        ypos += 50
        xpos += 50
    xpos = 50
    for pos in range(10):
        redrect.append(
            pygame.draw.rect(
                screen, 'red',
                pygame.rect.Rect(x.x - xpos, x.y, cell_size, cell_size)))
        xpos += 50
    xpos = 50
    ypos = 50
    for pos in range(10):
        redrect.append(
            pygame.draw.rect(
                screen, 'red',
                pygame.rect.Rect(x.x - xpos, x.y - ypos, cell_size,
                                 cell_size)))
        ypos += 50
        xpos += 50
    ypos = 50
    for pos in range(10):
        redrect.append(
            pygame.draw.rect(
                screen, 'red',
                pygame.rect.Rect(x.x, x.y - ypos, cell_size, cell_size)))
        ypos += 50
    xpos = 50
    ypos = 50
    for pos in range(10):
        redrect.append(
            pygame.draw.rect(
                screen, 'red',
                pygame.rect.Rect(x.x + xpos, x.y - ypos, cell_size,
                                 cell_size)))
        ypos += 50
        xpos += 50
    xpos = 50
    ypos = 50
    for pos in range(10):
        redrect.append(
            pygame.draw.rect(
                screen, 'red',
                pygame.rect.Rect(x.x - xpos, x.y - ypos, cell_size,
                                 cell_size)))
        ypos += 50
        xpos += 50


def bishophighlights(x):
    xpos = 50
    ypos = 50
    for pos in range(10):
        redrect.append(
            pygame.draw.rect(
                screen, 'red',
                pygame.rect.Rect(x.x + xpos, x.y - ypos, cell_size,
                                 cell_size)))
        ypos += 50
        xpos += 50
    xpos = 50
    ypos = 50
    for pos in range(10):
        redrect.append(
            pygame.draw.rect(
                screen, 'red',
                pygame.rect.Rect(x.x - xpos, x.y - ypos, cell_size,
                                 cell_size)))
        ypos += 50
        xpos += 50
    xpos = 50
    ypos = 50
    for pos in range(10):
        redrect.append(
            pygame.draw.rect(
                screen, 'red',
                pygame.rect.Rect(x.x + xpos, x.y + ypos, cell_size,
                                 cell_size)))
        ypos += 50
        xpos += 50
    xpos = 50
    ypos = 50
    for pos in range(10):
        redrect.append(
            pygame.draw.rect(
                screen, 'red',
                pygame.rect.Rect(x.x - xpos, x.y + ypos, cell_size,
                                 cell_size)))
        ypos += 50
        xpos += 50


def towerhighlights(x):
    xpos = 50
    ypos = 50
    for pos in range(8):
        redrect.append(
            pygame.draw.rect(
                screen, 'red',
                pygame.rect.Rect(x.x + xpos, x.y, cell_size, cell_size)))
        xpos += 50
    xpos = 50
    for pos in range(8):
        redrect.append(
            pygame.draw.rect(
                screen, 'red',
                pygame.rect.Rect(x.x - xpos, x.y, cell_size, cell_size)))
        xpos += 50
    for pos in range(8):
        redrect.append(
            pygame.draw.rect(
                screen, 'red',
                pygame.rect.Rect(x.x, x.y + ypos, cell_size, cell_size)))
        ypos += 50
    ypos = 50
    for pos in range(8):
        redrect.append(
            pygame.draw.rect(
                screen, 'red',
                pygame.rect.Rect(x.x, x.y - ypos, cell_size, cell_size)))
        ypos += 50


def horsehighlights(x):
    global redrect
    redrect = [
        pygame.draw.rect(
            screen, 'red',
            pygame.rect.Rect(x.x + 50, x.y - 100, cell_size, cell_size)),
        pygame.draw.rect(
            screen, 'red',
            pygame.rect.Rect(x.x - 50, x.y - 100, cell_size, cell_size)),
        pygame.draw.rect(
            screen, 'red',
            pygame.rect.Rect(x.x + 100, x.y - 50, cell_size, cell_size)),
        pygame.draw.rect(
            screen, 'red',
            pygame.rect.Rect(x.x + 100, x.y + 50, cell_size, cell_size)),
        pygame.draw.rect(
            screen, 'red',
            pygame.rect.Rect(x.x + 50, x.y + 100, cell_size, cell_size)),
        pygame.draw.rect(
            screen, 'red',
            pygame.rect.Rect(x.x - 50, x.y + 100, cell_size, cell_size)),
        pygame.draw.rect(
            screen, 'red',
            pygame.rect.Rect(x.x - 100, x.y + 50, cell_size, cell_size)),
        pygame.draw.rect(
            screen, 'red',
            pygame.rect.Rect(x.x - 100, x.y - 50, cell_size, cell_size))
    ]


def highlight(x):
    global redrect, stat, selectedindex, showsuggests, blackkingrect, whitekingrect, whitequeenrect, blackqueenrect, posibility, posibility2
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
            posibility = pygame.rect.Rect(x.x + 50, x.y + 50, cell_size,
                                          cell_size)
            posibility2 = pygame.rect.Rect(x.x - 50, x.y + 50, cell_size,
                                           cell_size)
            for i in blackpeonlist:
                for y in whitepeonlist:
                    if y == x:
                        posibility = pygame.rect.Rect(x.x + 50, x.y + 50,
                                                      cell_size, cell_size)
                        posibility2 = pygame.rect.Rect(x.x - 50, x.y + 50,
                                                       cell_size, cell_size)
                        if posibility == i or posibility == blackkingrect or posibility == blackqueenrect:
                            if posibility not in redrect:
                                redrect.append(
                                    pygame.draw.rect(screen, 'red',
                                                     posibility))

                        if posibility2 == i or posibility2 == blackkingrect or posibility2 == blackqueenrect:
                            if posibility2 not in redrect:
                                redrect.append(
                                    pygame.draw.rect(screen, 'red',
                                                     posibility2))
            for fr in allblackdoublerects:
                print(f'piece{fr}')
                print(f'posibility1 {posibility}')
                print(f'posibility2 {posibility2}')
                if posibility.x == fr.x and posibility.y == fr.y:
                    print('ni-')
                    if posibility not in redrect:
                        print('tri')
                        redrect.append(
                            pygame.draw.rect(screen, 'red', posibility))
                if posibility2 == fr:
                    print('tiri')
                    if posibility2 not in redrect:
                        print('ti')
                        redrect.append(
                            pygame.draw.rect(screen, 'red', posibility2))

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

            if x == whitequeenrect:
                selectedindex = 19
                redrect = []
                queenhighlights(x)
            for i in whitebishoprects:
                if i == x:
                    if whitebishoprects.index(i) == 0:
                        selectedindex = 23
                    else:
                        selectedindex = 24
                    redrect = []
                    bishophighlights(x)
            for i in whitehorserects:
                if i == x:
                    if whitehorserects.index(i) == 0:
                        selectedindex = 27
                    else:
                        selectedindex = 28
                    redrect = []
                    horsehighlights(x)
            for i in whitetowerrects:
                if i == x:
                    if whitetowerrects.index(i) == 0:
                        selectedindex = 31
                    else:
                        selectedindex = 32
                    redrect = []
                    towerhighlights(x)

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
                    for i in whitepeonlist:
                        for y in blackpeonlist:
                            if y == x:
                                posibility = pygame.rect.Rect(
                                    x.x + 50, x.y - 50, cell_size, cell_size)
                                posibility2 = pygame.rect.Rect(
                                    x.x - 50, x.y - 50, cell_size, cell_size)
                                if posibility == i or posibility == whitekingrect or posibility == whitequeenrect:
                                    if posibility not in redrect:
                                        redrect.append(
                                            pygame.draw.rect(
                                                screen, 'red', posibility))
                                if posibility == whitetowerrects[
                                        0] or posibility == whitetowerrects[1]:
                                    if posibility not in redrect:
                                        redrect.append(
                                            pygame.draw.rect(
                                                screen, 'red', posibility))
                                if posibility == whitehorserects[
                                        0] or posibility == whitehorserects[1]:
                                    if posibility not in redrect:
                                        redrect.append(
                                            pygame.draw.rect(
                                                screen, 'red', posibility))
                                if posibility == whitebishoprects[
                                        0] or posibility == whitehorserects[1]:
                                    if posibility not in redrect:
                                        redrect.append(
                                            pygame.draw.rect(
                                                screen, 'red', posibility))
                                if posibility2 == i or posibility2 == whitekingrect or posibility2 == whitequeenrect:
                                    if posibility2 not in redrect:
                                        redrect.append(
                                            pygame.draw.rect(
                                                screen, 'red', posibility2))
                                if posibility2 == whitetowerrects[
                                        0] or posibility2 == whitetowerrects[1]:
                                    if posibility2 not in redrect:
                                        redrect.append(
                                            pygame.draw.rect(
                                                screen, 'red', posibility2))
                                if posibility2 == whitehorserects[
                                        0] or posibility2 == whitehorserects[1]:
                                    if posibility2 not in redrect:
                                        redrect.append(
                                            pygame.draw.rect(
                                                screen, 'red', posibility2))
                                if posibility2 == whitebishoprects[
                                        0] or posibility2 == whitehorserects[1]:
                                    if posibility2 not in redrect:
                                        redrect.append(
                                            pygame.draw.rect(
                                                screen, 'red', posibility2))
            for i in blackbishoprects:
                if i == x:
                    if blackbishoprects.index(i) == 0:
                        selectedindex = 21
                    else:
                        selectedindex = 22
                    redrect = []
                    bishophighlights(x)
            for i in blackhorserects:
                if i == x:
                    if blackhorserects.index(i) == 0:
                        selectedindex = 25
                    else:
                        selectedindex = 26
                    horsehighlights(x)
            for i in blacktowerrects:
                if i == x:
                    if blacktowerrects.index(i) == 0:
                        selectedindex = 29
                    else:
                        selectedindex = 30
                    redrect = []
                    towerhighlights(x)

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
            if x == blackqueenrect:
                selectedindex = 20
                redrect = []
                queenhighlights(x)

        screen.blit(highlightimg, x)

        for i in redrect:
            if i.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    if stat == 'black':
                        for whiterect in range(len(whitepeonlist)):
                            if whitepeonlist[whiterect] == i:
                                whitepeonlist[whiterect] = ''

                        if whitebishoprects[0] == i:
                            whitebishoprects[0] = ''
                        elif whitebishoprects[1] == i:
                            whitebishoprects[1] = ''
                        elif whitehorserects[0] == i:
                            whitehorserects[0] = ''
                        elif whitehorserects[1] == i:
                            whitehorserects[1] = ''
                        elif whitetowerrects[0] == i:
                            whitetowerrects[0] = ''
                        elif whitetowerrects[1] == i:
                            whitetowerrects[1] = ''

                        if whitekingrect == i:
                            print('game over , black is the winner')
                            whitekingrect = ''
                        if whitequeenrect == i:
                            whitequeenrect = ''

                        else:
                            if x == blackkingrect:
                                blackkingrect = i
                            if x == blackqueenrect:
                                blackqueenrect = i
                        if selectedindex < 16:
                            blackpeonlist[selectedindex] = i
                        elif selectedindex == 21:
                            blackbishoprects[0] = i
                        elif selectedindex == 22:
                            blackbishoprects[1] = i
                        elif selectedindex == 25:
                            blackhorserects[0] = i
                        elif selectedindex == 26:
                            blackhorserects[1] = i
                        elif selectedindex == 29:
                            blacktowerrects[0] = i
                        elif selectedindex == 30:
                            blacktowerrects[1] = i
                        stat = 'white'
                        showsuggests = False

                    elif stat == 'white':
                        for blackrect in range(len(blackpeonlist)):
                            if blackpeonlist[blackrect] == i:
                                blackpeonlist[blackrect] = ''

                        if blackbishoprects[0] == i:
                            blackbishoprects[0] = ''
                        if blackbishoprects[1] == i:
                            blackbishoprects[1] = ''
                        if blackbishoprects[0] == i:
                            blackbishoprects[0] = ''
                        if blackbishoprects[1] == i:
                            blackbishoprects[1] = ''
                        if blackhorserects[0] == i:
                            blackhorserects[0] = ''
                        if blackhorserects[1] == i:
                            blackhorserects[1] = ''
                        if blacktowerrects[0] == i:
                            blacktowerrects[0] = ''
                        if blacktowerrects[1] == i:
                            blacktowerrects[1] = ''

                        if blackkingrect == i:
                            print('game over , white is the winner')
                            blackkingrect = ''
                        if blackqueenrect == i:
                            blackqueenrect = ''
                        if selectedindex < 16:
                            whitepeonlist[selectedindex] = i
                        else:
                            if x == whitekingrect:
                                whitekingrect = i
                            if x == whitequeenrect:
                                whitequeenrect = i
                        if selectedindex < 16:
                            whitepeonlist[selectedindex] = i
                        elif selectedindex == 23:
                            whitebishoprects[0] = i
                        elif selectedindex == 24:
                            whitebishoprects[1] = i
                        elif selectedindex == 27:
                            whitehorserects[0] = i
                        elif selectedindex == 28:
                            whitehorserects[1] = i
                        elif selectedindex == 31:
                            whitetowerrects[0] = i
                        elif selectedindex == 32:
                            whitetowerrects[1] = i
                        redrect = []
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
        if i != '':
            screen.blit(blackpeon, i)
            if stat == 'black':
                if i.collidepoint(pygame.mouse.get_pos()):
                    selected = i
                    showsuggests = True

    for i in blackbishoprects:
        if i != '':
            screen.blit(blackbishop, i)
            if stat == 'black':
                if i.collidepoint(pygame.mouse.get_pos()):
                    selected = i
                    showsuggests = True
    for i in blackhorserects:
        if i != '':
            screen.blit(blackhorse, i)
            if stat == 'black':
                if i.collidepoint(pygame.mouse.get_pos()):
                    selected = i
                    showsuggests = True

    for i in blacktowerrects:
        if i != '':
            screen.blit(blacktower, i)
            if stat == 'black':
                if i.collidepoint(pygame.mouse.get_pos()):
                    selected = i
                    showsuggest = True
    for i in whitepeonlist:
        if i != '':
            screen.blit(whitepeon, i)
            if stat == 'white':
                if i.collidepoint(pygame.mouse.get_pos()):
                    selected = i
                    showsuggests = True
    for i in whitebishoprects:
        if i != '':
            screen.blit(whitebishop, i)
            if stat == 'white':
                if i.collidepoint(pygame.mouse.get_pos()):
                    selected = i
                    showsuggests = True
    for i in whitehorserects:
        if i != '':
            screen.blit(whitehorse, i)
            if stat == 'white':
                if i.collidepoint(pygame.mouse.get_pos()):
                    selected = i
                    showsuggests = True
    for i in whitetowerrects:
        if i != '':
            screen.blit(whitetower, i)
            if stat == 'white':
                if i.collidepoint(pygame.mouse.get_pos()):
                    selected = i
                    showsuggest = True
    if whitekingrect != '':
        screen.blit(whiteking, whitekingrect)
        if stat == 'white':
            if whitekingrect.collidepoint(pygame.mouse.get_pos()):
                selected = whitekingrect
                showsuggests = True
    if whitequeenrect != '':
        screen.blit(whitequeen, whitequeenrect)
        if stat == 'white':
            if whitequeenrect.collidepoint(pygame.mouse.get_pos()):
                selected = whitequeenrect
                showsuggests = True
    if blackkingrect != '':
        screen.blit(blackking, blackkingrect)
        if stat == 'black':
            if blackkingrect.collidepoint(pygame.mouse.get_pos()):
                selected = blackkingrect
                showsuggests = True
    if blackqueenrect != '':
        screen.blit(blackqueen, blackqueenrect)
        if stat == 'black':
            if blackqueenrect.collidepoint(pygame.mouse.get_pos()):
                selected = blackqueenrect
                showsuggests = True

    highlight(selected)
    pygame.display.update()
    pygame.time.Clock().tick(60)
