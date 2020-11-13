# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной
# схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
# матрицы складываем с первым элементом первой строки второй матрицы и т.д.


from random import randint
class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list
        self.__str__()

    def __str__(self):
        for i in self.my_list:
            for j in i:
                print(f'{j} ', end='')
            print()
        return ''

    def __add__(self, two):
        for i in range(len(self.my_list)):
            for j in range(len(two.my_list[i])):
                self.my_list[i][j] = self.my_list[i][j] + two.my_list[i][j]
        return Matrix.__str__(self)


x = input('Введите размерность матрицы: ').split()
matrix1 = Matrix([[randint(-10, 10) for j in range(int(x[0]))] for i in range(int(x[1]))])
new_matrix2 = Matrix([[randint(-10, 10) for j in range(int(x[0]))] for i in range(int(x[1]))])
print(matrix1.__add__(new_matrix2))
