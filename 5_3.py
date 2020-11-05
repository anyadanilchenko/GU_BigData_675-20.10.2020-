# Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет
# оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
# величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('File_for_5_3', encoding='utf-8') as f:
    lines = f.readlines()
    pr = []
    totalsum = 0
    totalcount = 0
    for line in lines:
        k = line.strip().split()
        totalsum += float(k[1])
        totalcount += 1
        if float(k[1]) < 20000:
            pr.append(k[0])
    print('Сотрудники с зарплатой меньше 20 000 руб.:', *pr)
    print(f'Средняя зарплата сотрудников {totalsum/totalcount:.2f}')
