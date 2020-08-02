import pygame
import sys
from parameters import *
from snake import Snake
from element import Element


class Game(object):

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake')
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.snake = Snake()
        self.item = Element(self.snake)
        self.key = pygame.K_d
        self.font = pygame.font.SysFont("georgia", 20)
        self.counter = 0
        self.text_render = self.font.render(str(self.counter), 1, WHITE)

        self.run()

    def handleEvents(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s and self.key != pygame.K_w:
                self.key = pygame.K_s
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_w and self.key != pygame.K_s:
                self.key = pygame.K_w
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d and self.key != pygame.K_a:
                self.key = pygame.K_d
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a and self.key != pygame.K_d:
                self.key = pygame.K_a

    def ticking(self):
        self.tps_delta += self.tps_clock.tick() / 1000.0
        while self.tps_delta > 1 / TPS_MAX:
            self.snake.move(self.key)

            if self.snake.isColision():
                sys.exit(0)

            if self.item.isColision(self.snake):
                self.snake.extend()
                self.counter += 1
                self.text_render = self.font.render(str(self.counter), 1, WHITE)
                self.item = Element(self.snake)

            self.tps_delta -= 1 / TPS_MAX

    def draw(self):
        self.screen.fill(BLACK)
        self.item.draw(self.screen, RED, DARK_RED)
        self.snake.draw(self.screen)
        self.screen.blit(self.text_render, (MARGIN, MARGIN))
        pygame.display.flip()

    def run(self):
        while True:
            self.handleEvents()
            self.ticking()
            self.draw()


Game()
