# Desenvolva um programa que leia as duas notas de um aluno,calcule e mostre a sua média.

n1 = float(input('Entre com a primeira nota: '))
n2 = float(input('Entre com a segunda nota: '))

m = (n1 + n2)/2

print('A media das notas é:{:.1f}'.format(m))