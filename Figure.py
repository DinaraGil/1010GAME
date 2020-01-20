class Figure:
    def __init__(self, *args):
        self.figure_array = args
        max_row = max(self.figure_array)
        self.width = 0
        while max_row != 0:
            max_row = max_row >> 1
            self.width += 1
        self.height = len(self.figure_array)
        self.high_bit = 1 << (self.width - 1)

    def is_filled(self, x, y):
        row = self.figure_array[y]
        return ((row << x) & self.high_bit) != 0

    def get_array(self):
        return self.figure_array

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

