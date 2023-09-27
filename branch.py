import pygame as py
from math import cos, sin, radians

CHILDLENFACTOR = 0.7
ANGLECHANGE = 40

class Branch:

    def __init__(self, x, y, length, width, angle) -> None:
        
        self.x = x
        self.y = y
        self.x2 = 0
        self.y2 = 0
        self.length = length
        self.width = width
        self.angle = angle
        self.child = False

    def draw(self, screen, color):

        self.x2 = self.x + self.length * cos(radians(self.angle))
        self.y2 = self.y - self.length * sin(radians(self.angle))

        py.draw.line(screen, color, (self.x, self.y), (self.x2, self.y2), self.width)

    def drawChild(self):
    
        child1 = Branch(self.x2, self.y2, self.length * CHILDLENFACTOR, self.width, self.angle - ANGLECHANGE)
        child2 = Branch(self.x2, self.y2, self.length * CHILDLENFACTOR, self.width, self.angle + ANGLECHANGE)
        self.child = True
        return child1, child2