# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность
# (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды
# в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер
# (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу
# декоратора @property.

class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square_coat(self):
        return self.width / 6.5 + 0.5

    def square_suit(self):
        return self.height * 2 + 0.3

    @property
    def total_square(self):
        return f'Потребуется {self.square_coat() + self.square_suit():.2f} метров ткани'

class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = self.width / 6.5 + 0.5

    def __str__(self):
        return f'Ткани на пальто {self.square_c:.2f}'


class Suit(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_s = self.height * 2 + 0.3

    def __str__(self):
        return f'Ткани на пальто {self.square_s:.2f}'

coat = Coat(2, 4)
suit = Suit(1, 2)
print(coat)
print(suit)
print(coat.total_square)
print(suit.total_square)
