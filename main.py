from tkinter import *
from tkinter import messagebox
import pygame

from Board import Board, GraphicBoard
from FigureDraw import FigureDraw
from FigureManager import FigureManager
from Settings import Settings
from pygame import Vector2

pygame.init()


class Game:
    def __init__(self):
        self.fps = 50
        self.clock = pygame.time.Clock()
        self.cell_size = 10

        self.screen_size = 1000, 1000
        self.screen = pygame.display.set_mode(self.screen_size)

        self.figure_manager = FigureManager()

        self.graph_board = GraphicBoard(pygame.Vector2(Settings.cell_size, Settings.cell_size))

        self.figures = None
        self.create_figures()

        self.selected_figure = None
        self.mouse_offset_of_selected_figure = Vector2(0, 0)

    def end_game(self):
        Tk().wm_withdraw()  # to hide the main window
        messagebox.showinfo('END OF GAME', 'RESTART')
        self.graph_board = GraphicBoard(pygame.Vector2(Settings.cell_size, Settings.cell_size))
        self.selected_figure = None
        self.create_figures()

    def create_figures(self):
        figures = self.figure_manager.choice_figures()

        x = self.graph_board.get_rect().right + Settings.cell_size
        y = self.graph_board.get_rect().top

        self.figures = []
        for fig in figures:
            self.figures.append(FigureDraw(fig, Vector2(x, y)))
            y += fig.get_height() * (Settings.cell_size + Settings.border_width) + Settings.cell_size

    def draw(self):
        self.screen.fill(Settings.background_color)

        self.graph_board.draw(self.screen)
        for figure in self.figures:
            if figure != self.selected_figure:
                figure.draw(self.screen)

        if self.selected_figure is not None:
            self.selected_figure.draw(self.screen)

        pygame.display.flip()

    def is_end_of_game(self):
        for figure in self.figures:
            if self.graph_board.get_board().can_place_anywhere(figure.get_figure()):
                return False
        return True

    def loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for figure in self.figures:
                        if figure.is_selected(Vector2(event.pos)):
                            print('selected')
                            self.selected_figure = figure
                            self.mouse_offset_of_selected_figure = event.pos - figure.get_position()

                elif event.type == pygame.MOUSEBUTTONUP:

                    if self.selected_figure is not None:
                        if self.graph_board.put_figure(self.selected_figure):
                            del self.figures[self.figures.index(self.selected_figure)]

                            if len(self.figures) == 0:
                                self.create_figures()

                            if self.is_end_of_game():
                                self.end_game()
                        else:
                            self.selected_figure.set_position(self.selected_figure.get_start_position())

                        self.selected_figure = None

                if event.type == pygame.MOUSEMOTION and self.selected_figure is not None:
                    self.selected_figure.set_position(event.pos - self.mouse_offset_of_selected_figure)

                self.draw()

            self.clock.tick(self.fps)


game_session = Game()
game_session.loop()
