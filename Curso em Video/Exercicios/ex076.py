"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na
sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabula. """

print('-' * 20, '\n', 'LISTAGEM DE PREÇOS', '\n', '-' * 20)
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

for n in range(0, len(lista)):
    if n % 2 == 0:
        print(f'{lista[n]:.<30}', end='R$ ')
    else:
        print(f'{lista[n]:>7.2f}')
