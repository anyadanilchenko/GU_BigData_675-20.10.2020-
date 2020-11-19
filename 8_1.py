import random
import time


class Matrix:
    def __init__(self, name):
        self.name = name
        self.matrix = []
        self.lst = random.sample(range(1, 90), 15)
        self.generator_matrix()
        self.rt = 0
        self.__str__()

    def __str__(self):
        name_total = ' ' + self.name + ' '
        if len(name_total) <= 22:
            print(name_total.center(22, '-'))
        else:
            print(name_total)
            print('-' * 22)
        for row in range(0, 3):
            for column in range(0, 9):
                print(f'{self.matrix[row][column]} ', end='')
            print()
        print('-' * 22)

    def generator_matrix(self):
        for row in range(3):
            lst3 = list(self.lst[:5])
            lst3.sort()
            for column in range(4):
                lst3.insert(random.randint(0, 4), '_')
            self.matrix.append(lst3)
            del self.lst[:5]
        return self.matrix

    def find_number(self, value):
        for row in range(0, 3):
            for column in range(0, 9):
                if self.matrix[row][column] == value:
                    return True
        return False

    def find_none(self):
        for row in range(0, 3):
            for column in range(0, 9):
                try:
                    if 1 >= int(self.matrix[row][column]) >= 90:
                        self.rt += 1
                except ValueError:
                    continue
        if self.rt > 0:
            return False
        return True

    def del_num(self, value):
        for row in range(0, 3):
            for column in range(0, 9):
                if self.matrix[row][column] == value:
                    self.matrix[row][column] = '*'
        return Matrix.__str__(self)


class Randon_num():
    def __init__(self):
        self.number = int()
        self.num_list = list(range(1, 91))

    def __str__(self):
        print()
        print(f'Новое число {self.number[0]}. Осталось {len(self.num_list)} чисел')

    def random_num(self):
        self.number = random.sample(self.num_list, 1)
        self.num_list.remove(self.number[0])
        return self.number


print('Игра началась!')
print()
time.sleep(2)
user = input('Введите имя игрока: ')
print(f'Создается карточка для {user}')
time.sleep(3)
your_matrix = Matrix(user)
print(f'Создается карточка для Computer')
time.sleep(3)
comp_matrix = Matrix('Computer')
num = Randon_num()
for i in range(91):
    n = num.random_num()
    num.__str__()
    if input('Зачеркнуть цифру? (y/n): ') == 'y':
        if your_matrix.find_number(n[0]):
            print(f'Число {n[0]} удалено из карточки {user}')
            your_matrix.del_num(n[0])
            if not your_matrix.find_none():
                print(f'{user}, поздравляем с победой!')
            else:
                if comp_matrix.find_number(n[0]):
                    print(f'Число {n[0]} удалено из карточки Computer')
                    comp_matrix.del_num(n[0])
                    if not your_matrix.find_none():
                        print(f'Computer одержал победу :(')

        else:
            print(f'Будьте внимательнее! Числа {n[0]} нет в вашей карточке')
            break
    else:
        if your_matrix.find_number(n[0]):
            print(f'Будьте внимательнее! Число {n[0]} есть в вашей карточке')
            break
        else:
            if comp_matrix.find_number(n[0]):
                print(f'Число {n[0]} удалено из карточки Computer')
                your_matrix.__str__()
                comp_matrix.del_num(n[0])
                if not your_matrix.find_none():
                    print(f'Computer одержал победу :(')
            else:
                your_matrix.__str__()
                comp_matrix.__str__()
print()
print('Игра окончена!')
