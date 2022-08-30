import pygame 
from pygame import Vector2

class board:
    def __init__(self) -> None:
        pass
    def drawboard(self):
        firstcol = '#769656'
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
class king:
    def __init__(self) -> None:
        self.vect = Vector2(4,0)
        self.blackvect = Vector2(4,7)
        self.king = pygame.image.load('images/Chess_klt45.svg')
        self.blackking = pygame.image.load('images/Chess_kdt45.svg')
        self.highlight = pygame.image.load('images/highlight.png')
        self.rects = []
        self.rect = pygame.rect.Rect(self.vect.x * cell_size, self.vect.y * cell_size, cell_size, cell_size)
        self.blackrect = pygame.rect.Rect(self.blackvect.x * cell_size, self.blackvect.y * cell_size, cell_size, cell_size)
        self.moves = [Vector2(1,0),Vector2(1,1),Vector2(1,-1),Vector2(0,1),Vector2(0,-1),Vector2(-1,0),Vector2(-1,1),Vector2(-1,-1)]
    def drawwhiteking(self):
        screen.blit(self.king, self.rect)
    def drawblackking(self):
        screen.blit(self.blackking, self.blackrect)
        
    def showsuggests(self, vect):
        if showsugges:
            self.moves = [Vector2(1,0),Vector2(1,1),Vector2(1,-1),Vector2(0,1),Vector2(0,-1),Vector2(-1,0),Vector2(-1,1),Vector2(-1,-1)]
            for i in self.moves:
                for x in peon.vects:
                    if i.x + i.y != x.x + x.y:
                        x = vect.x  + i.x
                        y = vect.y  + i.y
                        self.highlightrect = pygame.rect.Rect(x * cell_size, y * cell_size , cell_size, cell_size)
                        self.rects.append(self.highlightrect)
                        screen.blit(self.highlight, self.highlightrect)
    def hidesuggests(self):
        global showsugges
        for i in self.moves:
            showsugges = False
            i.x = self.rect.x
            i.y = self.rect.y
    def move(self, vect, rect):
        global showsugges
        
        if vect == self.vect:
            self.rect = pygame.rect.Rect(rect.x , rect.y , cell_size, cell_size)
            self.vect = Vector2(rect.x / cell_size, rect.y/cell_size )
        if vect == self.blackvect:
            self.blackrect = pygame.rect.Rect(rect.x , rect.y , cell_size, cell_size)
            self.blackvect = Vector2(rect.x / cell_size, rect.y/cell_size )
            
        showsugges = False
        king.hidesuggests()
        self.rects.clear()
        
        
        
class peons:
    def __init__(self) -> None:
        self.peon = pygame.image.load('images/Chess_plt45.svg')
        self.blackpeon = pygame.image.load('images/Chess_pdt45.svg')
        self.vects = [Vector2(0,1),Vector2(1,1),Vector2(2,1),Vector2(3,1),Vector2(4,1),Vector2(5,1),Vector2(6,1),Vector2(7,1)]
        self.blackvects = [Vector2(0,6),Vector2(1,6),Vector2(2,6),Vector2(3,6),Vector2(4,6),Vector2(5,6),Vector2(6,6),Vector2(7,6)]
        self.moves = Vector2(1,0)
    def drawwhitepeon(self):
        for i in self.vects:
            rect = pygame.rect.Rect(i.x * cell_size, i.y * cell_size, cell_size, cell_size)
            screen.blit(self.peon, rect)
    def drawblackpeon(self):
        for i in self.blackvects:
            blackrect = pygame.rect.Rect(i.x * cell_size, i.y * cell_size, cell_size, cell_size)
            screen.blit(self.blackpeon, blackrect)
            
class main:
    def __init__(self) -> None:
        pass
cell_size = 45
cell_number = 8
showsugges = False

screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

board = board()
king = king()
x = king.blackvect
peon = peons()

running = True
while running:
    if not showsugges:
        king.showsuggests(x)
    screen.fill('#EEEED2')
    board.drawboard()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    king.drawwhiteking()
    king.drawblackking()
    peon.drawblackpeon()
    peon.drawwhitepeon()
    
    if king.rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            showsugges = True
            x = king.vect
            y = king.rect
            king.showsuggests(x)
    if king.blackrect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            showsugges = True
            x = king.blackvect
            y = king.blackrect
            king.showsuggests(x)
    
    if showsugges:
        king.showsuggests(x)
    else:
        showsugges = False
    
    for i in king.rects:
        if i.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                king.move(x, i)
              
    pygame.display.update()
    clock.tick(60)    
    
    
