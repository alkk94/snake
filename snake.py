import pygame
from element import Element
from parameters import *


class Snake(object):

    def __init__(self):
        self.head = Element()
        self.body = []
        self.hiddenTail = None

    def draw(self, screen):
        self.head.draw(screen, BLUE, DARK_BLUE)
        for element in self.body:
            element.draw(screen, GREEN, DARK_GREEN)

    def move(self, key):
        if key == pygame.K_s:
            self.moveElements((0, 1))
        if key == pygame.K_w:
            self.moveElements((0, -1))
        if key == pygame.K_d:
            self.moveElements((1, 0))
        if key == pygame.K_a:
            self.moveElements((-1, 0))

    def moveElements(self, vector):
        if self.body:
            self.hiddenTail = self.body[-1]
        else:
            self.hiddenTail = self.head

        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = self.body[i - 1]

        x = (self.head.position[0] + vector[0]) % NUMBER_X
        y = (self.head.position[1] + vector[1]) % NUMBER_Y
        if self.body:
            self.body[0] = self.head
        self.head = Element()
        self.head.setPosition(x, y)

    def extend(self):
        self.body.append(self.hiddenTail)

    def isColision(self):
        for element in self.body:
            if element.position == self.head.position:
                return True
        return False
