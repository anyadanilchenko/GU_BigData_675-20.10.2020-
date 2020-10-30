# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

try:
    def my_func(num1, num2, num3):
        a = [num1, num2, num3]
        total = sum(a) - min(a)
        print(f'Сумма наибольших двух элементов {total}')

    my_func(2, -6, 6)

except ValueError:
    print('Ошибка! Вы ввели не число!')
except TypeError:
    print('Ошибка! Вы ввели не число!')
