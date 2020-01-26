import pygame
from pygame import Vector2, Rect
from Figure import Figure
from Settings import Settings


class FigureDraw:
    def __init__(self, figure: Figure, position):
        self.figure = figure
        self.position = Vector2(position)
        self.start_position = Vector2(position)

    def draw(self, screen):
        for row in range(self.figure.get_height()):
            for col in range(self.figure.get_width()):
                filled = self.figure.is_filled(col, row)
                if filled:
                    pos = Vector2(self.position)
                    pos.x += col * (Settings.cell_size + Settings.border_width)
                    pos.y += row * (Settings.cell_size + Settings.border_width)

                    pygame.draw.rect(
                        screen,
                        Settings.border_color,
                        Rect(pos, Vector2(
                            Settings.cell_size + 2,
                            Settings.cell_size + 2)))

                    pos.x += Settings.border_width
                    pos.y += Settings.border_width

                    pygame.draw.rect(screen, Settings.cell_color,
                                     Rect(pos, Vector2(Settings.cell_size,
                                                       Settings.cell_size)))

    def is_selected(self, pos: Vector2):
        row = (pos.y - self.position.y) // (
                Settings.cell_size + Settings.border_width)
        col = (pos.x - self.position.x) // (
                Settings.cell_size + Settings.border_width)
        if row < 0 or row > (self.figure.get_height() - 1):
            return False
        if col < 0 or col > (self.figure.get_width() - 1):
            return False
        return self.figure.is_filled(int(col), int(row))

    def set_position(self, pos: Vector2):
        self.position = pos

    def get_position(self):
        return self.position

    def get_start_position(self):
        return self.start_position

    def get_figure(self):
        return self.figure
