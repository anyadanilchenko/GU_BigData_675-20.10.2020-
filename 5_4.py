# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

numb = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('File_for_5_4', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        k = line.split()
        f1 = open('File_for_5_4_total', 'a', encoding='utf-8')
        if k[0] == 'One' or k[0] == 'Two' or k[0] == 'Three' or k[0] == 'Four':
            f1.write(line.replace(k[0], numb.get(k[0])))
    f1.close()

