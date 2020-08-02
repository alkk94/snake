import pygame
from random import randint
from parameters import *


class Element(object):

    def __init__(self, snake=None):
        self.position = self.getPosition(snake)

    def getPosition(self, snake):

        def getFinalPosition(L):
            K = []
            for i in range(len(L)):
                for j in range(len(L[i])):
                    if not L[i][j]:
                        K.append((i, j))
            return K[randint(0, len(K) - 1)]

        if snake is None:
            return randint(0, NUMBER_X - 1), randint(0, NUMBER_Y - 1)
        else:
            L = [[False] * NUMBER_Y for _ in range(NUMBER_X)]
            L[snake.head.position[0]][snake.head.position[1]] = True
            for element in snake.body:
                L[element.position[0]][element.position[1]] = True
            return getFinalPosition(L)

    def draw(self, screen, color, darkColor):
        x = self.position[0] * ELEMENT_SIZE
        y = self.position[1] * ELEMENT_SIZE
        outer = pygame.Rect(x, y, ELEMENT_SIZE, ELEMENT_SIZE)
        inner = pygame.Rect(x + MARGIN, y + MARGIN, INNER_SIZE, INNER_SIZE)
        pygame.draw.rect(screen, darkColor, outer)
        pygame.draw.rect(screen, color, inner)

    def setPosition(self, x, y):
        self.position = (x, y)

    def isColision(self, snake):
        return self.position == snake.head.position
