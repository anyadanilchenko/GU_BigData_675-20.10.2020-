# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('File_for_5_2', encoding='utf-8') as f:
    lines = f.readlines()
    pr = 0
    for line in lines:
        pr += 1
        k = len(line.split())
        print(f'В строке № {pr} - {k} слова. Исходная строка: {line.strip()}')
