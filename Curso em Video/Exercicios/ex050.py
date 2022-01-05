""" Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que
 agora utilizando um laço for."""

num = int(input('Escolha um numero:'))

for num in range(1, 11):
    num += 1
print('{} x {} = {}'.format(num,'X','X'))
