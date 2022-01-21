""" Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho adaptável. """


def lin(txt):
    tam = len(txt) + 5
    print('~'*tam)
    print(f'{txt}')
    print('~'*tam)


lin(str(input('Digite algo: ')))
