# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить ее на экран.

with open('File_for_5_5.txt', 'w') as f:
    while True:
        n = input('введите строку: ')
        if n != '':
            f.write(n)
            f.write('\n')
        else:
            break
with open('File_for_5_5.txt', encoding='utf-8') as f:
    lines = f.readlines()
    totalsum = 0
    for line in lines:
        k = line.strip().split()
        for i in range(len(k)):
            totalsum += int(k[i])
    print(f'Сумма всех введенных чисел: {totalsum}')
