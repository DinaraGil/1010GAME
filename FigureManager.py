import random
from Figure import Figure


class FigureManager:
    def __init__(self):
        self.figures = [
            Figure(0b11111),  # палка 5 горизонт
            Figure(0b1, 0b1, 0b1, 0b1, 0b1),  # палка 5 вертикаль
            Figure(0b1111),  # палка 4 горизонт
            Figure(0b1, 0b1, 0b1, 0b1),  # палка 4 вертикаль
            Figure(0b111),  # палка 3 горизонт
            Figure(0b1, 0b1, 0b1),  # палка 3 вертикаль
            Figure(0b11),  # палка 2 горизонт
            Figure(0b1, 0b1),  # палка 2 вертикаль
            Figure(0b1),  # куб 1*1
            Figure(0b11, 0b11),  # куб 2*2
            Figure(0b111, 0b111, 0b111),  # куб 3*3
            Figure(0b11, 0b01),  # палка 2 горизонт, 1 вертик
            Figure(0b11, 0b10),  # палка 2 горизонт, 1 верт вниз
            Figure(0b01, 0b11),  # палка 1 верт, 2 горизонт
            Figure(0b10, 0b11),  # палка 1 верт, 2 горизонт
            Figure(0b111, 0b001, 0b001),  # палка три горизонталь, 2 верт.
            Figure(0b100, 0b100, 0b111)]  # палка 2 горизонт, 1 верт

    def choice_figures(self):
        return [random.choice(self.figures), random.choice(self.figures),
                random.choice(self.figures)]
