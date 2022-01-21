""" def lin():
    print('-' * 30)


lin()
print('  CURSO EM VIDEOS   ')
lin() """


"""def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)
titulo('Olá Vincy')"""


def soma(a, b):
    s = a + b
    print(s)


soma(10, 6)
soma(b=4, a=8)#Posso inverte os valores, desde que seja declarado antes"""

"""def contador(*num):
    #for valor in num:
     #   print(f'{valor}', end='.')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(5, 6, 8, 3)
contador(1, 2)
contador(7, 1, 0)"""


"""def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)"""


'''#Desempacotamento
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
'''