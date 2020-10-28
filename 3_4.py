# Программа принимает действительное положительное число x и целое отрицательное
# число y. Необходимо выполнить возведение числа x в степень y. Задание необходимо
# реализовать в виде функции my_func(x, y). При решении задания необходимо
# обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение
# в степень с помощью оператора **. Второй — более сложная реализация без
# оператора **, предусматривающая использование цикла
try:
    def my_func(x, y):
        totalnum = 1
        if y > 0:
            for i in range(y):
                totalnum *= x
            print(f'Число {x} в степени {y} равно {totalnum}')
        elif y == 0:
            print(f'Число {x} в степени {y} равно {totalnum}')
        elif y < 0:
            for i in range(abs(y)):
                totalnum *= x
            print(f'Число {x} в степени {y} равно {1/totalnum:.5f}')

    def my_func2(x, y):
        print(f'Число {x} в степени {y} равно {x ** y:.5f}')


    numone = int(input('Введите число: '))
    numtwo = int(input('Введите степень числа: '))
    my_func(numone, numtwo)
    my_func2(numone, numtwo)
except ValueError:
    print('Ошибка! Вы ввели не число!')
except TypeError:
    print('Ошибка! Вы ввели не число!')
