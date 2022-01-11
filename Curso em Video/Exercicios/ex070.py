""" Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
 vai continuar. No final, mostre: -A: Qual é o total gasto na compra; -B:Quantos produtos custam mais de R$1000;
 -C: Qual é o nome do produto mais barato. """

total = mais1 = mpreco = cot = 0
barato = ''
while True:
    # Ler nome
    nome = str(input('Nome do produto:')).strip().upper()
    cot += 1
    # Ler preço
    preco = float(input('Qual preço:R$'))
    mpreco = preco
    total += preco


    if preco > 1000:
        mais1 += 1

    if cot == 1:
        mpreco = preco
    else:
        if preco < mpreco:
            mpreco = preco
            barato = nome
    # pergunta se o usuário vai continuar
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Digite novamente:[S/N]?')).strip().upper()[0]
    if cont == 'N':
        break
# Total gasto
print(f'Total gasto R${total:.2f}')
# Quantidade de produtos que custam mais de 1000 reais
print(f'Produtos que custam mais de R$1000 reais:{mais1}')
# Nome do produto mais barato
print(f'Produto mais barato:{barato} custa R${mpreco}')
