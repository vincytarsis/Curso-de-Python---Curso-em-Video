""" Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que
 agora utilizando um laço for."""

num = int(input('Escolha um numero:'))
for cont in range(1, 11):
    print('{} x {} = {}'.format(num, cont, (num * cont)))
