import pygame


cell_size = 50
cell_number = 8
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()

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
running = True
showhighlight = False
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
            else:
                allowedmoves = [pygame.Rect(i.x, y , cell_size,cell_size)]
        if stat == 'white':
            screen.blit(highlightimg,i)
            y = i.y + 50
            if i.y == 50:
                allowedmoves = [pygame.Rect(i.x, y , cell_size,cell_size),pygame.Rect(i.x, y + 50 , cell_size,cell_size) ]
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
                    stat = 'white'
                    allowedmoves = []
                    showhighlight = False
                elif stat == 'white':
                    whitepeonlist[peonind] = move
                    stat = 'black'
                    allowedmoves = []
                    showhighlight = False
                    
    
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
    for z in whitepeonlist:
        screen.blit(whitepeon, z)
    for i in blackpeonlist:
        screen.blit(blackpeon, i)
    highlight(pe)
    
    
    pygame.display.update()
    clock.tick(60)
    
    