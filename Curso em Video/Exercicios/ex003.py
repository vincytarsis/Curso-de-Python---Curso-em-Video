# Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('\033[34mDigite um número: '))
n2 = int(input('\033[33mDigite um número:\033[m '))

soma = n1 + n2

print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))