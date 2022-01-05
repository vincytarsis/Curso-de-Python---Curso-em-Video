""" Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
-Equilátero: todos os lados iguais; -Isosceles: dois lados iguais; -Escaleno: todos os lados diferentes. """

r1 = int(input('R1:'))
r2 = int(input('R2:'))
r3 = int(input('R3:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma um triângulo')
    if r1 == r2 == r3:
        print('\033[34mEquilátero\033[m')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('\033[33mIsósceles\033[m')
    else:
        print('\033[32mEscalano')
else:
    print('Não forma um triângulo')