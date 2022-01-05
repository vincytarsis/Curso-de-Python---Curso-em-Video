""" Crie um programa que faça o computador jogar Jokenpô com você. """
import random
from random import randint

jk = int(input('Escolha uma das 3 formas\n\033[37m[1]Pedra\033[m\n\033[30m[2]Papel\033[m\n\033[34m[3]Tesoura\033[m\n'))

pc = random.randint(1, 3)

if pc == jk:
    print('Empate')
elif pc == 1 and jk == 2:
    print('Você ganhou!\nPapel ganha de Pedra')
elif pc == 1 and jk == 3:
    print('Você perdeu\nPedra ganha de Tesoura')
elif pc == 2 and jk == 1:
    print('Você perdeu!\nPapel ganha de Pedra')
elif pc == 2 and jk == 3:
    print('Você ganhou!\nTesoura ganha de papel')
elif pc == 3 and jk == 1:
    print('Você ganhou\nPedra ganha de Tesoura')
else:
    print('Você perdeu!\nTesoura ganhde Papel')

print(pc)