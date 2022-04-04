""" Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
usuário. O programa será interrompido quando o número solicitado for negativo."""


while True:
    n = int(input('Digite um número:'))
    print('='*20)

    if n < 0:
        break

    for tab in range(1, 11):
        print(f'{n} x {tab} = {n * tab}')
        tab += 1

print('Acabou')
