""" Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim
e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1; b) De 10 até 0, de 2 em 2; c) Uma contagem personalizada. """

"""from time import sleep


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


cont_pers()"""

# Guanabara
from time import sleep


def contador(i, f, p):
    if p < 0:
        p += -1
    if p == 0:
        p = 1
    print('==' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(0.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end=' ')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end=' ')
            sleep(0.5)
            cont -= p
        print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
