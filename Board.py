import pygame
from pygame import Vector2, Rect
from Settings import Settings


class Board:
    cell_count = 10

    def __init__(self):
        self.board = [0b0000000000 for i in range(Board.cell_count)]
        self.board_areas = []

    def put_figure(self, figure, row, col):
        if row + figure.get_height() > Board.cell_count:
            return False
        if col + figure.get_width() > Board.cell_count:
            return False

        if not self.can_place_figure(figure, row, col):
            return False

        self.place_figure(figure, row, col)
        self.clear_board(figure, row, col)

        return True

    def can_place_figure(self, figure, row, col):
        for y in range(figure.get_height()):
            figure_row = figure.get_array()[y]
            board_y = y + row

            if not self.is_figure_row_can_placed(figure, figure_row, self.board[board_y], col):
                return False
        return True

    def place_figure(self, figure, row, col):
        for y in range(figure.get_height()):
            figure_row = figure.get_array()[y]
            board_y = y + row

            self.board[board_y] = self.merge_row(figure, figure_row, self.board[board_y], col)

    def clear_board(self, figure, row, col):
        rows_clear_list = []
        for y in range(figure.get_height()):
            figure_row = figure.get_array()[y]
            board_y = y + row

            if self.board[board_y] == 0b1111111111:
                rows_clear_list.append(board_y)

        for x in range(figure.get_width()):
            board_x = col + x
            filled = True
            for y in range(self.cell_count):
                if not self.is_filled(board_x, y):
                    filled = False
                    break

            if filled:
                for y in range(self.cell_count):
                    self.clear_cell(board_x, y)

        for y in rows_clear_list:
            self.board[y] = 0

    def merge_row(self, figure, figure_row, board_row, col):
        adjusted_figure_row = figure_row << (Board.cell_count - col - figure.get_width())
        board_area_with_figure = adjusted_figure_row ^ board_row
        return board_area_with_figure

    def is_figure_row_can_placed(self, figure, figure_row, board_row, col):
        result_mask = self.merge_row(figure, figure_row, board_row, col) & board_row
        return result_mask == board_row

    def is_filled(self, x, y):
        row = self.board[y]
        return ((row << x) & 0b1000000000) != 0

    def clear_cell(self, x, y):
        row = self.board[y]
        self.board[y] = (0b1000000000 >> x) ^ row

    def can_place_anywhere(self, figure):
        for board_row in range(Board.cell_count - figure.get_height()):
            for board_col in range(Board.cell_count - figure.get_width()):
                if self.can_place_figure(figure, board_row, board_col):
                    return True

        return False


class GraphicBoard:
    def __init__(self, top_left_pos: Vector2):
        self.board = Board()
        board_size: int = Settings.cell_size * Board.cell_count + Settings.border_width * (Board.cell_count + 1)
        self.rect = pygame.Rect(top_left_pos, Vector2(board_size, board_size))

    def draw(self, screen):
        pygame.draw.rect(screen, Settings.border_color, self.rect)
        for row in range(Board.cell_count):
            for col in range(Board.cell_count):
                filled = self.board.is_filled(col, row)
                color = Settings.cell_color if filled else Settings.board_empty_cell_color
                pos = Vector2(self.rect.topleft)
                pos.x += Settings.border_width + col * (Settings.cell_size + Settings.border_width)
                pos.y += Settings.border_width + row * (Settings.cell_size + Settings.border_width)
                pygame.draw.rect(screen, color, Rect(pos, Vector2(Settings.cell_size, Settings.cell_size)))

    def get_rect(self):
        return self.rect

    def put_figure(self, figure):
        if not(self.is_row_allowable(figure)):
            return False
        if not(self.is_col_allowable(figure)):
            return False

        print(self.get_row(figure), self.get_col(figure))
        return self.board.put_figure(figure.get_figure(), int(self.get_row(figure)), int(self.get_col(figure)))

    def get_row(self, figure):
        pos = figure.get_position() + Vector2(Settings.cell_size // 2, Settings.cell_size // 2)
        row = (pos.y - self.rect.top) // (Settings.cell_size + Settings.border_width)
        return row

    def get_col(self, figure):
        pos = figure.get_position() + Vector2(Settings.cell_size // 2, Settings.cell_size // 2)
        col = (pos.x - self.rect.left) // (Settings.cell_size + Settings.border_width)
        return col

    def is_row_allowable(self, figure):
        row = self.get_row(figure)
        if row < 0 or row > (Board.cell_count - 1):
            return False
        else:
            return True

    def is_col_allowable(self, figure):
        col = self.get_col(figure)
        if col < 0 or col > (Board.cell_count - 1):
            return False
        else:
            return True

    def get_board(self):
        return self.board
