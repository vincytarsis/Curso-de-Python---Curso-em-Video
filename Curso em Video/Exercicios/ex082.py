""" Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final,
mostre o conteúdo das três listas geradas"""

lista = []
par = []
impar = []
#Ler vários números
while True:
    n = int(input('Digite um número: '))
    # Colocar em uma lista
    lista.append(n)
    # Crie duas listas, par e ímpar
    # Separe os números
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    res = str(input('Quer continuar? [S/N] ')).upper()
    if res == 'N':
        break
#Mostre as 3 listas
print('=-'*30)
print(f'Lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')

#Guanabara

'''num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um número:')))
    resp = str(input('Quer continuar? [S/N')).upper()
    if resp in 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('=-'*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')'''
