""" Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim
e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1; b) De 10 até 0, de 2 em 2; c) Uma contagem personalizada. """

from time import sleep


def lin():
    print('=-' * 30)


# Contagem de 1 a 10
def cont1a10():
    for c in range(1, 11):
        print(c, end=' ')
        c += 1
        sleep(0.5)
    print('FIM!')


lin()
print('Contagem de 1 até 10 de 1 em 1')


# cont1a10()


# Contagem de 10 a 0
def cont10a0():
    for c in range(10, 0, -2):
        print(c, end=' ')
        c += 1
        # sleep(0.5)
    print('FIM!')


lin()


# cont10a0()
# Contagem personalizada

def cont_pers():
    a = int(input('Inicio:'))
    b = int(input('Fim:'))
    c = int(input('Passo: '))
    for a in range(a, b, c):
        print(a, end=' ')
        if a < b:
            c = c * (-1)
            c += 1
        elif c > 0:
            a += c
        else:
            a -= c
        # sleep(0.5)
    print('FIM!')


cont_pers()
