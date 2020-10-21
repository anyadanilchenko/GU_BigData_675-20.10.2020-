num = int(input('Введите количество секунд: '))
hour = (num // 60) // 60
minutes = (num - 60 * (hour * 60)) // 60
seconds = num % 60

print('Всего времени:')
print(f'{hour} : {minutes} : {seconds}')
