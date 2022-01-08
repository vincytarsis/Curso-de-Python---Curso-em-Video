""" Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5x4x3x2x1=120. """

n1 = int(input('Escolha um número:'))

contr = n1 #O contador começa com o valor que o usuario escolher
fato = 1  #1 é nulo na multiplicação, todos os numeros *1 é ele mesmo

while contr > 0: #O fatorial vai até 1, enquanto ele for maior que 0, ele faz o loop
    print('{}'.format(contr),end='')
    print('x' if contr > 1 else ' = ', end='')

    fato = fato * contr
    contr -= 1

print(fato)