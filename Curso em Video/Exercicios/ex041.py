""" A Confereação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade: -Até 9 anos: MIRIM; -Até 14 anos: INFANTIL; -Até 19 anos: JUNIOR; -Até 20 anos:
SENIOR; -Acima: MASTER. """

cor = {'azul': '\033[34m',
       'limpa': '\033[m'}

from datetime import datetime

ano = int(input('Entre com seu ano de nascimento:'))

an = datetime.today().strftime('%Y')

id = int(an) - ano

if id <= 9:
    print('{}MIRIM'.format(cor['azul']))
elif 9 < id <= 14:
    print('{}INFANTIL'.format(cor['azul']))
elif 14 < id <= 19:
    print('{}JUNIOR'.format(cor['azul']))
elif 19 < id <= 20:
    print('{}SÊNIOR'.format(cor['azul']))
else:
    print('\033[33mMASTER')

