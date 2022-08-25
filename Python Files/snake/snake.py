import pygame
import random
from pygame.math import Vector2


cell_size = 30
cell_number = 20
class snake:
    def __init__(self):
        self.snacker = pygame.image.load('images/snakehead.png')
        self.snacker = pygame.transform.scale(self.snacker, (cell_size,cell_size))
        self.snackright = pygame.image.load('images/snakeheadright.png').convert_alpha()
        self.snackright = pygame.transform.scale(self.snackright, (cell_size,cell_size))
        self.snackdown = pygame.image.load('images/snakeheaddown.png').convert_alpha()
        self.snackdown = pygame.transform.scale(self.snackdown, (cell_size,cell_size))
        self.snackleft = pygame.image.load('images/snakeheadleft.png').convert_alpha()
        self.snackleft = pygame.transform.scale(self.snackleft, (cell_size,cell_size))
        self.snake_body = pygame.image.load('images/snakebody.png').convert_alpha()
        self.snake_body = pygame.transform.scale(self.snake_body, (cell_size,cell_size))
        
        self.body = [Vector2(5, 2), Vector2(4 , 2), Vector2(3, 2)]
        self.direction = Vector2(1,0)
    def drawsnake(self):
        self.headir()
        for index ,block in enumerate(self.body):
            snakblock = pygame.rect.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            if index == 0:
                screen.blit(self.snacker, snakblock)
            else:
                screen.blit(self.snake_body, snakblock)
    def headir(self):
        relation = self.body[0] - self.body[1]
        if relation == Vector2(1, 0):
            self.snacker = self.snackright
        if relation == Vector2(-1, 0):
            self.snacker = self.snackleft
        if relation == Vector2(0, 1):
            self.snacker = self.snackdown
        if relation == Vector2(0, -1):
            self.snacker = pygame.image.load('images/snakehead.png')
            self.snacker = pygame.transform.scale(self.snacker, (cell_size,cell_size))
        
    def move_snak(self):
        bodycopy = self.body[:-1]
        bodycopy.insert(0, bodycopy[0] + self.direction)
        self.body = bodycopy[:]
    
    def add_blok(self):
        bodycopy = self.body[:]
        bodycopy.insert(0, bodycopy[0] + self.direction)
        self.body = bodycopy[:]
        
class fruit:
    def __init__(self):
        self.rand()
    def drawfruit(self):
        apple = pygame.rect.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        screen.blit(munch, apple)
    def rand(self):
        self.x = random.randint(0,cell_number- 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        for i in snake().body:
            if self.pos == i:
                while self.pos == i:
                    self.x = random.randint(0,cell_number- 1)
                    self.y = random.randint(0,cell_number - 1)
                    self.pos = Vector2(self.x, self.y)
                    
            
     
class main:
    def __init__(self) -> None:
        self.snack = snake()
        self.yum = fruit()  
    
    def update(self):
        self.snack.move_snak()
        self.drawdelem()      
        self.colided()
        self.over()
        self.drawgras()
    def drawdelem(self):
        self.yum.drawfruit()
        self.snack.drawsnake()
    def colided(self):
        if self.yum.pos == self.snack.body[0]:
            self.yum.rand()
            self.snack.add_blok()
    def over(self):
        if self.snack.body[0].x >= cell_number or self.snack.body[0].x <= 0:
            exit()
        if self.snack.body[0].y >= cell_number or self.snack.body[0].y <= 0:
            exit()
        for i in self.snack.body[1:]:
            if i == self.snack.body[0]:
                exit()
    def drawgras(self):
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
                
                
class titlescreen:
    def __init__(self) -> None:
        self.font = pygame.font.Font('Fonts/ARCADECLASSIC.TTF', 50)
    def showtitle(self):
        font = self.font.render('SNAKE', False, 'green')
        screen.blit(font, (cell_size * cell_number / 2 - 60, 100))
        font = self.font.render('press s to start', False, 'red')
        screen.blit(font, (cell_size * cell_number / 2 - 180, cell_size * cell_number - 100))
        
    
pygame.init()


game = 0
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()
munch = pygame.image.load('images/apple.png')
munch = pygame.transform.scale(munch, (cell_size,cell_size))
mouvevent = pygame.USEREVENT + 1
pygame.time.set_timer(mouvevent, 150) 
delay = pygame.USEREVENT + 2
pygame.time.set_timer(delay, 150) 
gamemain = main()
mainscreen = titlescreen()

press = True
running = True
while running:
    screen.fill('#4c792b')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and press:
                    if gamemain.snack.direction != Vector2(0, 1):
                        gamemain.snack.direction = Vector2(0, -1)
                        press = False
                if event.key == pygame.K_s and press:
                    if gamemain.snack.direction != Vector2(0, -1):
                        gamemain.snack.direction = Vector2(0, 1)
                        press = False
                if event.key == pygame.K_d and press:
                    if gamemain.snack.direction != Vector2(-1, 0):
                        gamemain.snack.direction = Vector2(1, 0)
                        press = False
                if event.key == pygame.K_a and press:
                    if gamemain.snack.direction != Vector2(1, 0):
                        gamemain.snack.direction = Vector2(-1, 0)
                        press = False
            if event.type == mouvevent:
                gamemain.update()
                
            if event.type == delay:
                press = True
            gamemain.drawgras()
            gamemain.drawdelem()
        
        if game == 0:
            mainscreen.showtitle()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game = 1
                    
        pygame.display.update()
        
        
    clock.tick(60)