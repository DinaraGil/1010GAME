import pygame
import random
pygame.init()

class Board:
    def __init__(self):
        self.board = [0b0000000000 for i in range(10)]

    def update_board(self):
        pass

    def put_figure(self, coord):
        pass

    def possible_to_put(self, coord):
        pass


class Figure:
    def __init__(self):
        pass


class FigureManager:
    def __init__(self):
        pass

    def create_figure_list(self):
        f1 = [0b11111, 0b00000, 0b00000, 0b00000, 0b00000] #палка 5 горизонт
        f2 = [0b10000, 0b10000, 0b10000, 0b10000, 0b10000] #палка 5 вертикаль
        f3 = [0b11110, 0b00000, 0b00000, 0b00000, 0b00000] #палка 4 горизонт
        f4 = [0b10000, 0b10000, 0b10000, 0b10000, 0b00000] #авлка 4 вертикаль
        f5 = [0b11100, 0b00000, 0b00000, 0b00000, 0b00000] #палка 3 горизонт
        f6 = [0b10000, 0b10000, 0b10000, 0b00000, 0b00000] #палка 3 вертикаль
        f7 = [0b11000, 0b00000, 0b00000, 0b00000, 0b00000] #палка 2 горизонт
        f8 = [0b10000, 0b10000, 0b00000, 0b00000, 0b00000] #палка 2 вертикаль

        f9 = [0b10000, 0b00000, 0b00000, 0b00000, 0b00000] #куб 1*1
        f10 = [0b11000, 0b11000, 0b00000, 0b00000, 0b00000] #куб 2*2
        f11 = [0b11100, 0b11100, 0b11100, 0b00000, 0b00000] #куб 3*3

        f12 = [0b11000, 0b01000, 0b00000, 0b00000, 0b00000] #палка 2 горизонт, 1 вертик
        f13 = [0b11000, 0b10000, 0b00000, 0b00000, 0b00000] #палка 2 горизонт, 1 верт вниз
        f14 = [0b01000, 0b11000, 0b00000, 0b00000, 0b00000] #палка 1 верт, 2 горизонт
        f15 = [0b10000, 0b11000, 0b00000, 0b00000, 0b00000] #палка 1 верт, 2 горизонт
        f16 = [0b11100, 0b00100, 0b00100, 0b00000, 0b00000] #палка три горизонталь, 2 верт.
        f17 = [0b10000, 0b10000, 0b11100, 0b00000, 0b00000] #палка 2 горизонт, 1 верт

        figures = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17]
        return figures

    def choice_figures_3(self):
        figures = self.create_figure_list()
        random_figure1 = random.choice(figures)
        random_figure2 = random.choice(figures)
        random_figure3 = random.choice(figures)

        return random_figure1, random_figure2, random_figure3

        
class Game:
    def __init__(self):
        self.fps = 50
        self.clock = pygame.time.Clock()

    def loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                #draw
        pygame.display.flip()
        self.clock.tick(self.fps)