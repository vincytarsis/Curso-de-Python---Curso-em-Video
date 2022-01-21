""" Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular(largura e comprimento) e mostre a área do terreno. """


def area(a, b):
    terreno = a * b
    print(f'A area de um terreno {a}x{b} é de {terreno}m²')


area(a=float(input('A:')), b=float(input('B:')))

