""" Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5x4x3x2x1=120. """

# Utilizando modulo

'''from math import factorial
n = int(input('Digite um número para calcular seu fatorial:'))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''

n = int(input('Escolha um número:'))

contr = n  # O contador começa com o valor que o usuário escolher
fato = 1   # 1 é nulo na multiplicação, todos os números *1 é ele mesmo

while contr > 0:  # O fatorial vai até 1, enquanto ele for maior que 0, ele faz o ‘loop’
    print('{}'.format(contr), end='')
    print('x' if contr > 1 else ' = ', end='')

    fato = fato * contr
    contr -= 1

print(fato)

