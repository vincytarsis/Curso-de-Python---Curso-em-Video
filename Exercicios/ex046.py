""" Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até
 0, com uma pausa de 1 segundo entre elas."""

from time import sleep
for contagem in range(10, 0-1, -1):
    sleep(1)
    print(contagem)
print('Feliz ano novo!!!')
