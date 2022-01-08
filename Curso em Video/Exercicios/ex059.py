""" Crie um programa que leia dois valores e mostre um menu na tela: -[1]Somar; -[2]Multiplicar; -[3]Maior;
[4]Novos números; [5] sair do programa. Seu programa deverá realizar operação solicitada em cada caso. """

n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))

menu = 0

while menu != 5:
    print('='*30)
    menu = int(input('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novo número\n[5]Sair\nEscolha uma opção:'))

    if menu == 1:#Somar
        print('{}+{}={}'.format(n1, n2, n1 + n2))
    elif menu == 2:#Multiplocar
        print('{}x{}={}'.format(n1, n2, n1 * n2))
    elif menu == 3:#Maior
        if n1 > n2:
            print('Maior:{}'.format(n1))
        else:
            print('Maior:{}'.format(n2))
    elif menu == 4:#Troca de valores
        n1 = int(input('Escolha outro valor:'))
        n2 = int(input('Escolha mais uma valor:'))

print('Encerrou!')
