""" Desenvolva um programa que leia seis números inteiros e mostre a soma apensa daqueles
 qie foram pares. Se o valor digitado for impar, desconsidere-o."""

soma = 0
for i in range(1,7):
    num = int(input('Entre com um numero:'))
    if num % 2 == 0:
        soma += num
print(soma)