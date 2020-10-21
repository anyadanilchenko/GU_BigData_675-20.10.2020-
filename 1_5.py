revenue = int(input('Введите выручку: '))
cost = int(input('Введите  издержки: '))
if revenue > cost:
    print('Работаем с прибылью')
    profit = revenue - cost
    profitability = int((profit/revenue) * 100)
    print(f'Рентабельность выручки {profitability}%')
    person = int(input('Введите количество людей в фирме: '))
    perprofit = profit / person
    print("Прибыль фирмы в расчете на одного сотрудника {:.2f} рублей ".format(perprofit))
else:
    print('Фирма работает с убытком')
