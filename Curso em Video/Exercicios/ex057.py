""" Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' e 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto. """

sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo:[M]|[F]? ').strip().upper()[0])
print('OK')


