""" Escreva um programa que leia um número inteiro qualquer e peça paro o usuário escolher qual será a base de con-
  versão: -1 para binário -2 para octal -3 para hexadecimal. """

n = int(input('Entre com um número inteiro qualquer:'))

b = n
o = n
h = n

if n == 1:
    print(b)
elif n == 2:
    print(o)
else:
    print(h)
