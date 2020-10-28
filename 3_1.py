# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

try:
    def delnum(num1, num2):
        total = num1/num2
        print(f'При делении {num1} на {num2} итог {total:.2f}')

    numone = int(input('Введите первое число: '))
    numtwo = int(input('Введите второе число: '))
    delnum(numone, numtwo)


except ZeroDivisionError:
    print('Деление на ноль!')
except ValueError:
    print('Ошибка! Вы ввели не число!')
except TypeError:
    print('Ошибка! Вы ввели не число!')
