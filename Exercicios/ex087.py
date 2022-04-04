""" Aprimore o desafio anterior, mostrando no final: A: A soma de todos os valores digitado. B: A soma
dos valores da terceira coluna. C: O maior valor da segunda linha."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma = mai = 0
for l in range(0, 3):#Linha
    for c in range(0, 3): #Coluna
        matriz[l][c] = int(input(f'Digite os números para {[l],[c]}'))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]

print('=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
#Soma dos valores pares
print(f'A soma dos valores pares é {pares}')
#Soma dos valores da 3ª linha
for l in range(0, 3):
    soma += matriz[l][2]
print(f'A soma dos valores das 3ª coluna é {soma}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da 2ª linha é {mai}')
