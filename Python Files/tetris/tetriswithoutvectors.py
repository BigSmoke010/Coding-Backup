import pygame
import random 

class oblock:
    def __init__(self):
        self.block = pygame.image.load('images/Oblock.png')
        self.rect = self.block.get_rect(topleft=[200, 1])
        
class iblock:
    def __init__(self):
        self.block = pygame.image.load('images/Iblock.png')
        self.rect = self.block.get_rect(topleft=[200, 1])


class main:
    def __init__(self) -> None:
        self.chosenblock = random.choice([iblock(), oblock()])
    def drawblock(self):
        screen.blit(self.chosenblock.block, self.chosenblock.rect)
    def newblock(self):
        copiedrect = pygame.Rect.copy(self.chosenblock.rect)
        self.chosenblock = random.choice([iblock(), oblock()])
        cop
        screen.blit(self.chosenblock.block, self.chosenblock.rect)
    
pygame.init()

screen = pygame.display.set_mode((500, 700))

running = True
mouveevent = pygame.USEREVENT + 1 
pygame.time.set_timer(mouveevent, 500)
blocky = main()

while running:
    screen.fill((0,0,0))
    pygame.draw.line(screen, 'white', (100, 100),(100, 600))
    x = pygame.draw.line(screen, 'white', (100, 600),(400, 600))
    pygame.draw.line(screen, 'white', (400, 600),(400, 100))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == mouveevent:
            blocky.chosenblock.rect.y += 26
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                blocky.chosenblock.rect.x -= 26
            if event.key == pygame.K_d:
                blocky.chosenblock.rect.x += 26

            
    blocky.drawblock()
    if blocky.chosenblock.rect.colliderect(x):
        print('ok')
        blocky.newblock()
    pygame.display.update()
