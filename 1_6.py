day1 = int(input('Введите результат 1го дня: '))
day2 = int(input('Введите итоговый результат: '))
i = 1
while True:
    day1 *= 1.1
    i += 1
    if day1 >= day2:
        break
print(f'На {i}-й день спортсмен достиг результата — не менее {day2} км')
