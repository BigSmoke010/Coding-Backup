import pygame


cell_size = 50
cell_number = 8
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()
pygame.display.set_caption('chess')
whitepeon = pygame.image.load('images/Chess_plt45.svg').convert_alpha()
blackpeon = pygame.image.load('images/Chess_pdt45.svg').convert_alpha()
whiteking = pygame.image.load('images/Chess_klt45.svg').convert_alpha()
blackking = pygame.image.load('images/Chess_kdt45.svg').convert_alpha()
whitehorse = pygame.image.load('images/Chess_nlt45.svg').convert_alpha()
blackhorse = pygame.image.load('images/Chess_ndt45.svg').convert_alpha()
whitetower = pygame.image.load('images/Chess_rlt45.svg').convert_alpha()
blacktower = pygame.image.load('images/Chess_rdt45.svg').convert_alpha()
whiteslave = pygame.image.load('images/Chess_blt45.svg').convert_alpha()
blackslave = pygame.image.load('images/Chess_bdt45.svg').convert_alpha()
highlightimg = pygame.image.load('images/highlight.png').convert_alpha()
whitepeonlist = [pygame.Rect(0 * cell_size, 1 *cell_size, cell_size, cell_size),pygame.Rect(1 * cell_size, 1 *cell_size, cell_size, cell_size),pygame.Rect(2 * cell_size, 1 *cell_size, cell_size, cell_size),pygame.Rect(3 * cell_size, 1 *cell_size, cell_size, cell_size),pygame.Rect(4 * cell_size, 1 *cell_size, cell_size, cell_size),pygame.Rect(5 * cell_size, 1 *cell_size, cell_size, cell_size),pygame.Rect(6 * cell_size, 1 *cell_size, cell_size, cell_size),pygame.Rect(7 * cell_size, 1 *cell_size, cell_size, cell_size)]
blackpeonlist = [pygame.Rect(0 * cell_size, 6 *cell_size, cell_size, cell_size),pygame.Rect(1 * cell_size, 6 *cell_size, cell_size, cell_size),pygame.Rect(2 * cell_size, 6 *cell_size, cell_size, cell_size),pygame.Rect(3 * cell_size, 6 *cell_size, cell_size, cell_size),pygame.Rect(4 * cell_size, 6 *cell_size, cell_size, cell_size),pygame.Rect(5 * cell_size, 6 *cell_size, cell_size, cell_size),pygame.Rect(6 * cell_size, 6 *cell_size, cell_size, cell_size),pygame.Rect(7 * cell_size, 6 *cell_size, cell_size, cell_size)]
whitekingrect = pygame.Rect(3* cell_size, 0 * cell_size, cell_size, cell_size)
blackkingrect = pygame.Rect(3* cell_size, 7 * cell_size, cell_size, cell_size)
running = True
showhighlight = False
showright = False
showleft = False
showrightb = False
showleftb = False
stuck = False
stuckb = False
danger = any
dangerb = any
pe = any
stat = 'white'
peonind = 0
allowedmoves = []

def drawboard():
    firstcol = '#72ae50'
    for x in range(cell_number):
        if x % 2 == 0:
            for i in range(cell_number):
                if i % 2 == 0: 
                    grasrect = pygame.Rect(i * cell_size, x * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, firstcol, grasrect)
        else:
            for i in range(cell_number):
                if i % 2 != 0: 
                    grasrect = pygame.Rect(i * cell_size, x * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, firstcol, grasrect)

    

def highlight(i):
    global allowedmoves
    if showhighlight:
        if stat == 'black':
            screen.blit(highlightimg,i)
            y = i.y - 50
            if i.y == 300:
                allowedmoves = [pygame.Rect(i.x, y , cell_size,cell_size),pygame.Rect(i.x, y - 50 , cell_size,cell_size) ]
            elif showrightb:
                allowedmoves = [pygame.Rect(i.x, y , cell_size,cell_size), pygame.Rect(i.x + 50, i.y - 50 , cell_size,cell_size)]
            elif showleftb:
                allowedmoves = [pygame.Rect(i.x, y , cell_size,cell_size), pygame.Rect(i.x - 50, i.y - 50 , cell_size,cell_size)]
            elif stuckb:
                allowedmoves = []
            else:
                allowedmoves = [pygame.Rect(i.x, y , cell_size,cell_size)]
        if stat == 'white':
            screen.blit(highlightimg,i)
            y = i.y + 50
            if i.y == 50:
                allowedmoves = [pygame.Rect(i.x, y , cell_size,cell_size),pygame.Rect(i.x, y + 50 , cell_size,cell_size)]
            elif showright:
                allowedmoves = [pygame.Rect(i.x, y , cell_size,cell_size), pygame.Rect(i.x + 50, i.y + 50 , cell_size,cell_size)]
            elif showleft:
                allowedmoves = [pygame.Rect(i.x, y , cell_size,cell_size), pygame.Rect(i.x - 50, i.y + 50 , cell_size,cell_size)]
            elif showright and showleft:
                allowedmoves = [pygame.Rect(i.x, y , cell_size,cell_size), pygame.Rect(i.x - 50, i.y + 50 , cell_size,cell_size),pygame.Rect(i.x + 50, i.y + 50 , cell_size,cell_size)]
            elif stuck:
                allowedmoves = []
            else:
                allowedmoves = [pygame.Rect(i.x, y , cell_size,cell_size)]
               
        for i in allowedmoves:
            pygame.draw.rect(screen,'red',i)
        
        

while running:
    screen.fill('#FFFFFF')
    drawboard()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    for move in allowedmoves:
        if move.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                if stat == 'black':
                    blackpeonlist[peonind] = move
                    if move == dangerb:
                        for whitepeoninlist in whitepeonlist:
                            if whitepeoninlist == dangerb:
                                whitepeonlist.remove(whitepeoninlist)
                    
                    allowedmoves = []
                    showhighlight = False
                    showleftb = False
                    showrightb = False
                    showright = False
                    showleft = False
                    stat = 'white'
                elif stat == 'white':   
                    whitepeonlist[peonind] = move
                    if move == danger:
                        for blackpeoninlist in blackpeonlist:
                            if blackpeoninlist == danger:
                                blackpeonlist.remove(blackpeoninlist)
                        
                    
                    allowedmoves = []
                    showhighlight = False
                    showleftb = False
                    showrightb = False
                    showright = False
                    showleft = False
                    stat = 'black'
    
    if stat == 'white':
        for index, i in enumerate(whitepeonlist):
            if i.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    peonind = index
                    pe = i
                    stat = 'white'
                    showhighlight = True
                    highlight(pe)
    if stat == 'black':
        for index, y in enumerate(blackpeonlist):
            if y.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    peonind = index
                    pe = y
                    stat = 'black'
                    showhighlight = True
                    highlight(pe)
                    
    for whitepeonb in whitepeonlist:
        posiblekil = pygame.Rect(whitepeonb.x + 50, whitepeonb.y + 50, cell_size, cell_size)
        posiblekil2 = pygame.Rect(whitepeonb.x - 50, whitepeonb.y + 50, cell_size, cell_size)
        blocked = pygame.Rect(whitepeonb.x, whitepeonb.y + 50, cell_size, cell_size)
        for blackpe in blackpeonlist:
            if blackpe == posiblekil:
                danger = blackpe
                showright = True
            if blackpe == posiblekil2:
                danger = blackpe
                showleft = True
            if blackpe == blocked:
                stuck = True
            if blackpe == posiblekil2 and blackpe == posiblekil:
                danger = blackpe
                showright = True
                showleft = True
    for blackpeonb in blackpeonlist:
        posiblekil = pygame.Rect(blackpeonb.x + 50, blackpeonb.y - 50, cell_size, cell_size)
        posiblekil2 = pygame.Rect(blackpeonb.x - 50, blackpeonb.y - 50, cell_size, cell_size)
        blocked = pygame.Rect(blackpeonb.x, blackpeonb.y - 50, cell_size, cell_size)
        for whitpe in whitepeonlist:
            if whitpe == posiblekil:
                dangerb = whitpe
                showrightb = True
            if whitpe == posiblekil2:
                dangerb = whitpe
                showleftb = True
            if whitpe == blocked:
                stuckb = True
            if whitpe == posiblekil and whitpe == posiblekil2:
                dangerb = whitpe
                showrightb = True
                showleftb = True
            
                
    for z in whitepeonlist:
        screen.blit(whitepeon, z)
    for i in blackpeonlist:
        screen.blit(blackpeon, i)
    screen.blit(whiteking, whitekingrect)
    screen.blit(blackking, blackkingrect)
    highlight(pe)
    
    
    pygame.display.update()
    clock.tick(60)
    
 