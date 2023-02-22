import pygame
import pymunk
import math
import pymunk.pygame_util

screen = pygame.display.set_mode((800,600))
drawopts = pymunk.pygame_util.DrawOptions(screen)
space = pymunk.Space()
space.gravity = (0, 400)
clock = pygame.time.Clock()
ballshown = False
delbal = False
delline = False
boxes = []
def calcdist(p1,p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def calcangle(p1, p2):
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

def showball(space, pos):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, 40)
    shape.mass = 10
    shape.elasticity = 0.6
    shape.friction = 0.9
    space.add(body, shape)
    ballshown = True
    return shape
    
def showbox(space):
    sizes = [[(40,200), (500,400)], [(200,40), (600,200)], [(40,200), (700,400)]]
    for h, w in sizes:
        body = pymunk.Body(1,10)
        body.position = w
        shape = pymunk.Poly.create_box(body, h)
        shape.mass = 100
        shape.color = (139,169,19,100)
        shape.elasticity = 0.5
        shape.friction = 0.4
        space.add(body, shape)
        boxes.append(shape)

def draw(space, window,opts, line):
    window.fill('white')
    if line:
        pygame.draw.line(screen, 'black', line[0], line[1], 3)

    space.debug_draw(opts)

def create_boundaries(space, width, height):
	rects = [
		[(width/2, height - 10), (width, 20)],
		[(width/2, 10), (width, 20)],
		[(10, height/2), (20, height)],
		[(width - 10, height/2), (20, height)]
	]

	for pos, size in rects:
		body = pymunk.Body(body_type=pymunk.Body.STATIC)
		body.position = pos
		shape = pymunk.Poly.create_box(body, size)
		shape.elasticity = 0.4
		shape.friction = 0.5
		space.add(body, shape)

bounds = create_boundaries(space, screen.get_width(), screen.get_height())
box = showbox(space)
presedpos = None
line = None
running = True
while running:
    screen.fill((0,0,0))
    if ballshown and not delline: 
        line = [presedpos, pygame.mouse.get_pos()]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ballshown and not delbal: 
                ball.body.body_type = pymunk.Body.DYNAMIC
                angle = calcangle(*line)
                force = calcdist(*line) * 50 
                fx = math.cos(angle) * force
                fy = math.sin(angle) * force
                ball.body.apply_impulse_at_local_point((fx,fy), (0,0))
                line = None
                delline = True
                delbal = True
            elif not ballshown:
                presedpos = pygame.mouse.get_pos()
                ball = showball(space, event.pos)
                delline = False
                ballshown = True
            elif delbal and ballshown:
                space.remove(ball, ball.body)
                ballshown = False
                delbal =False

    boxes[0].body.position = pygame.mouse.get_pos()
    
    draw(space, screen ,drawopts, line)

    space.step(1/60)
    pygame.display.flip()
    clock.tick(60)

