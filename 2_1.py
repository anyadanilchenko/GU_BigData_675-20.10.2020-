# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

result_list = [2, 'text', 456, 45.3, None]
for i in range(len(result_list)):
    print(f'Элемент списка {i+1} имеет тип', type(result_list[i]))
