# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма
# собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли
# ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить
# ее в словарь (со значением убытков).
# Пример списка:
# [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json
with open('File_for_5_7', encoding='utf-8') as f:
    lines = f.readlines()
    my_dictionary_profit, my_dictionary_minus, my_dictionary_average = {}, {}, {}
    total = []
    totalsum, totalcount = 0, 0
    for line in lines:
        k = line.strip().split()
        profit = int(k[2])-int(k[3])
        if profit >= 0:
            totalsum += profit
            totalcount += 1
            my_dictionary_profit[k[0]] = profit
        if profit <= 0:
            my_dictionary_minus[k[0]] = profit
    my_dictionary_average['average_profit'] = int(totalsum/totalcount)
    total = [my_dictionary_profit,  my_dictionary_average, my_dictionary_minus]
    print(total)

with open("File_for_5_7_total.json", "w") as f1:
    json.dump(total, f1)
