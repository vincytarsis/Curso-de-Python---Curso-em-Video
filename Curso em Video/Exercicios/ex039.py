""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: -Se ele ainda vai se alistar
ao serviço militar; -Se é a hora de se alistar; -Se já passou do tempo de alistamento. Seu programa também deverá mostra
o tempo que falta ou que passou do prazo. """

from datetime import datetime

aat = datetime.today().strftime('%Y') #Ano atual

ano = int(input('Informe seu ano de nascimento:'))

id = int(aat) - ano #Idade da pessoa atualmente

ali = id - 18

if id <= 17:
    print('Você \033[34mainda vai se alistar!\033[m\nFalta {} anos!'.format(ali * -1))
elif id == 18:
    print('\033[32mHora de se alistar!\033[m')
else:
    print('\033[31mPassou do tempo!\033[m\nPassou {} anos!'.format(ali))
