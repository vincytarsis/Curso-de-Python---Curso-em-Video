""" Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de
uma sequência de Fibonacci. Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8 """

n = int(input('Entre com um número:'))

a = 0
b = 1
c = 0
count = 1

print('Sequencia de Fibonacci: ', end=' ')

while count <= n:
    print(c, end=' ')
    count += 1
    a = b
    b = c
    c = a + b
