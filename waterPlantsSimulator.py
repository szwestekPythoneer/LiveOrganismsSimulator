from random import *
from tkinter import *
from time import *

screenSize = 600
mapSize = 50

root = Tk ()
screen = Canvas (root, width=screenSize, height=screenSize, bg='blue')
screen.pack ()

class Fish ():
    pass

class Plant ():
    def __init__ (self, dna):
        self.energy = dna [0]
        self.time = dna [1]
        self.seeds = dna [2]
        self.mutationChance = dna [3]
        self.color = dna [4]
        self.dna = dna
    def mutate (self):
        _ = []
        for genom in range (0, 4):
            _.append (self.dna [genom] + choices ((0, 1, -1), weights=(-self.mutationChance + 100, self.mutationChance, self.mutationChance)) [0])
        b = self.dna [4] + choices ((0, 1, -1), weights=(-self.mutationChance + 100, self.mutationChance, self.mutationChance)) [0]
        if b in range (0, 6):
            _.append (b)
        else:
            _.append (self.dna [4])
        self.dna = _
    def seed (self, x, y):
        for _ in range (0, self.seeds):
            wee = choice ([(1, 0), (-1, 0), (0, 1), (0, -1)])
            if x + wee [0] != -1 and y + wee [1] != -1:
                if x + wee [0] < len (worldMap) and y + wee [1] < len (worldMap):
                    if worldMap [x + wee [0]][y + wee [1]][0] == 'water' and worldMap [x][y][0] != 'seed':
                        if self.energy >= self.dna [0]:
                            worldMap [x + wee [0]][y + wee [1]] = {0 : 'seed', 1 : Plant (self.dna)}
                            self.energy -= self.dna [0]
    def enjoyYourLife (self, x, y):
        if self.time <= 0 or self.energy <= 0:
            worldMap [x][y] = {0 : 'water'}
        if self.energy != 0:
            self.energy += 1
        if self.time != 0:
            self.time -= 1

def makeLine (a, b, c):
    lista = [a, b, c]
    map1 = []
    for i in range (0, mapSize):
        map1.append (choices (lista, weights = [70, 29, 1]) [0])
    return map1

worldMap = [makeLine ({0 : 'water'}, {0 : 'sand'}, {0: 'plant0', 1 : Plant ([1, 2, 1, 50, 0])}) for i in range (0, mapSize)]

def showMap (x, y):
    if worldMap [x][y][0] == 'sand':
        screen.create_rectangle (n * x, n * y, n * x + n, n * y + n, fill='yellow')
    elif worldMap [x][y][0] == 'plant0':
        screen.create_oval (n * x, n * y, n * x + n, n * y + n, fill='green2')
    elif worldMap [x][y][0] == 'plant1':
        screen.create_oval (n * x, n * y, n * x + n, n * y + n, fill='green3')
    elif worldMap [x][y][0] == 'plant2':
        screen.create_oval (n * x, n * y, n * x + n, n * y + n, fill='green4')
    elif worldMap [x][y][0] == 'plant3':
        screen.create_oval (n * x, n * y, n * x + n, n * y + n, fill='SpringGreen2')
    elif worldMap [x][y][0] == 'plant4':
        screen.create_oval (n * x, n * y, n * x + n, n * y + n, fill='SpringGreen3')
    elif worldMap [x][y][0] == 'plant5':
        screen.create_oval (n * x, n * y, n * x + n, n * y + n, fill='SpringGreen4')
    elif worldMap [x][y][0] == 'seed':
        screen.create_oval (n * x, n * y, n * x + 0.5 * n, n * y + 0.5 * n, fill='cyan')

def adult (x, y):
    colors = ('plant0', 'plant1', 'plant2', 'plant3', 'plant4', 'plant5')
    if worldMap [x][y][0] == 'seed':
        worldMap [x][y][0] = colors [worldMap [x][y][1].color]

def age (x, y):
    if 1 in worldMap [x][y] and worldMap [x][y][0] != 'seed':
        worldMap [x][y][1].enjoyYourLife (x, y)

def sew (x, y):
    if 1 in worldMap [x][y]:
        worldMap [x][y][1].seed (x, y)
        worldMap [x][y][1].mutate ()

n = screenSize / mapSize
while True:
    screen.delete ('all')
    for x in range (0, mapSize):
        for y in range (0, mapSize):
            age (x, y)
            sew (x, y)
            showMap (x, y)
    for x in range (0, mapSize):
        for y in range (0, mapSize):
            adult (x, y)
    screen.update ()
