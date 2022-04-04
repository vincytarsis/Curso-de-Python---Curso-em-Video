""" Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador
PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

from random import randint

cont = 0

while True:
    n = int(input('Digite um número:'))
    pc = randint(1, 10)

    p_i = ' '
    soma = n + pc

    while p_i not in 'PI':
        p_i = str(input('[P/I]:').strip().upper()[0])
    print('Deu Par' if soma % 2 == 0 else print('Deu Impar'))

    if p_i == 'P':
        if soma % 2 == 0:
            print('Ganhei')
            cont += 1
        else:
            print('Perdeu')
            break
    elif p_i == 'I':
        if soma % 2 == 1:
            print('Ganhei')
            cont += 1
        else:
            print('Perdeu')
            break

print(f'Ganhou {cont} em seguidas')

