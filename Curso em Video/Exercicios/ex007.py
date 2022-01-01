# Desenvolva um programa que leia as duas notas de um aluno,calcule e mostre a sua média.

n1 = float(input('\033[32mEntre com a primeira nota\033[m: '))
n2 = float(input('\033[33mEntre com a segunda nota:\033[m '))

m = (n1 + n2)/2

print('\033[34mA media das notas é:\033[m\033[4;36m{:.1f}'.format(m))