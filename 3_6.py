# Реализовать функцию int_func(), принимающую слова из маленьких латинских
# букв и возвращающую ее же, но с прописной первой буквой. Например,
# print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
# буквы. Необходимо использовать написанную ранее функцию int_func().



#def int_func(data):
   # for i in range(len(data)):
      #  if
    #print(data.capitalize())
    #print(data.title())



#line = input('Введите строку: ')
#int_func(line)
#print(*list(map(lambda x: x.title(), line.split())))

abc = set('abcdefghijklmnopqrstuvwxyz')
a = 'mama'
if a in abc:
    print('yes')
else:
    print('no')