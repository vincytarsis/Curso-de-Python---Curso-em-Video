""" Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho adaptável. """


"""def lin(txt):
    tam = len(txt)
    print('~'*tam)
    print(f'{txt}')
    print('~'*tam)


lin(str(input('Digite algo: ')))"""


# Guanabara

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal
escreva('Gustvao Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')