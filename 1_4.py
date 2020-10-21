num = int(input('Введите число: '))
max_n = 0

while num > 0:
    last_digit = num % 10
    if last_digit > max_n:
        max_n = last_digit
    num = num // 10
print(f'Максимальная цифра равна {max_n}')

