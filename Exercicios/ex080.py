""" Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""

#Usuario digita 5 valores
numeros = []
for c in range(0, 4):
    n = int(input('Digite um valor:'))
#Cadastra em uma lista
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
#Posição correta(sem sorted())
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista ...')
                break
            pos += 1
#Lista ordenada
print('=-*30')
print(f'Os valores digitados em ordem foram {numeros}')