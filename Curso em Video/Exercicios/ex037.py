""" Escreva um programa que leia um número inteiro qualquer e peça paro o usuário escolher qual será a base de con-
  versão: -1 para binário -2 para octal -3 para hexadecimal. """

n = int(input('Entre com um número inteiro qualquer:'))

b = bin(n)
o = oct(n)
h = hex(n)

base = int(input('Escolha a base de conversão\n(1)Binário\n(2)Octal\n(3)Hexadecimal\n'))

if base == 1:
    print(b)
elif base == 2:
    print(o)
elif base == 3:
    print(h)
