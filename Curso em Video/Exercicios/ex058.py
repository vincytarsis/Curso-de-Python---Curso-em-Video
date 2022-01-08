""" Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 a 10. Só que agora
 o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para
 vencer. """

from random import randint

n = randint(0, 10)

print('Tente acerta um número de 0 a 10')

acertou = False
tentativas = 0

while not acertou:
    jogador = int(input('Qual número:'))
    tentativas += 1
    if jogador == n:
        acertou = True
    else:
        if jogador < n:
            print('Tente novamente')
        elif jogador > n:
            print('Tente de novo')
print('Voce acertou com {} tentativas'.format(tentativas))
