import pygame
import random
from pygame import Vector2



class oblock:
    def __init__(self):
        self.blocks= [Vector2(15, 5), Vector2(16, 5), Vector2(15, 6), Vector2(16, 6)]
    def drawblocks(self):
        for i in self.blocks:
            rect = pygame.rect.Rect(i.x * cell_size, i.y * cell_size, cell_size,  cell_size)
            pygame.draw.rect(screen, 'yellow', rect)

class iblock:
    def __init__(self) -> None:
        self.blocks = [Vector2(15,5),Vector2(15,6),Vector2(15,7), Vector2(15,8)]
        self.blocksflipped = [Vector2(self.blocks[0].x - 2, self.blocks[0].y -2)]
    def drawblocks(self):
        for i in self.blocks:
            rect = pygame.rect.Rect(i.x * cell_size, i.y * cell_size, cell_size,  cell_size)
            pygame.draw.rect(screen, 'blue', rect)
            

class main:
    def __init__(self) -> None:
        self.chosenblock = random.choice([iblock(), oblock()])
    def drawblocks(self):
        self.chosenblock.drawblocks()
    def down(self):
        for i in self.chosenblock.blocks:
            i.y += 1
    def left(self):
        for i in self.chosenblock.blocks:
            i.x -= 1
    def right(self):
        for i in self.chosenblock.blocks:
            i.x += 1
    def stop(self):
        for i in self.chosenblock.blocks:
            i.x += 0
    def flip(self):
        self.chosenblock.blocks = [Vector2(self.chosenblock.blocks[0].x -2, self.chosenblock.blocks[0].y +2)]
        
        
pygame.init()
cell_size = 20
cell_number = 30
screen = pygame.display.set_mode((cell_size * 15, cell_size * 20))


mouveevent = pygame.USEREVENT + 1 
pygame.time.set_timer(mouveevent, 450)
player = main()
print(player)
running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == mouveevent:
            player.down()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.flip()
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.right()
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.left()


    player.drawblocks()

    pygame.display.update()

