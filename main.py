import pygame as pg
import sys


TILE = 30
FPS = 60

RES = HIEDTH, WIDTH = 600, 700
x = y = LENGTH = TILE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
COLORS = (WHITE, BLACK, GRAY, LIGHT_BLUE, GREEN, YELLOW, PINK)
count = 0

pg.init()
sc = pg.display.set_mode(RES)
clock = pg.time.Clock()


class BRICK:

    def __init__(self):
        self.x, self.y, self.L, self.STEP, = x, y, 0, 5

    def cube(self):
        self.L = TILE
        self.BORDER = B = 5
        SX, SY, LENGTH, DEPTH, S = self.x, self.y, self.L, self.L, self.STEP
        pg.draw.rect(sc, GREEN, (SX, SY, LENGTH, DEPTH))
        pg.draw.rect(sc, GREEN, (SX, SY, LENGTH, DEPTH), B)
        pg.draw.rect(sc, PINK, (SX+S, SY+S, LENGTH-S*2, DEPTH-S*2), B)

    def L_brick(self):
        self.cube()
        count = 1
        while not count == 3:
            self.y = self.y - 35
            self.cube()
            count = count + 1
        self.y = x
        self.x = self.x - self.L
        self.cube()

    def sq_brick(self):
        t = x
        # --
        # 0-
        self.cube()
        # 0-
        # 0-
        self.y = self.y - 35
        self.cube()
        self.x = self.x + 5 # very important part, 0<-->0 more/less, if we change number
        # 0 0
        # 0 -
        self.y = t
        self.x =self.x + self.L
        self.cube()
        # 0 0
        # 0 0
        self.y = self.y - 35
        self.cube()
        self.y = y
        self.x = t

while True:

    clock.tick(FPS)

    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    sc.fill(BLACK)
    C1 = BRICK()
    C1.sq_brick()

    if y < WIDTH:
        y += 1

    pg.display.update()
