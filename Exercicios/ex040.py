""" Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
 com a média atingida: -Média abaixo de 5.0: Reprovado; -Média entre 5.0 e 6.9: Recuperação; -Media 7.0 ou superior: Aprovado. """

n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))

m = (n1 + n2) / 2

if m < 5.0:
    print('\033[31mReprovado!\033[m')
elif m >= 5.0 and m <= 6.9:
    print('\033[33mRecuperação\033[m')
else:
    print('\033[32mAprovado!')
