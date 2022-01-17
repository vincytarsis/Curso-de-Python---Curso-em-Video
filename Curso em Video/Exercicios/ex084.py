""" Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A: Quantas pessoas foram cadastras; B: Uma listagem com as pessoas mais pesadas; C: Uma listagem com as
pessoas mais leves."""

princ = []
temp = []
mai = men = 0
#Ler nome e peso  de varias pessoas
while True:
    temp.append(str(input('Nome:')))
    temp.append(str(input('Peso:')))
    if len(princ) == 0:#primeiro loop verifica se tem algum peso
        mai = men = temp[1] #maior e menor peso recebe o temp na posição 1
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    #Guardar em uma princpal
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]')).lower()
    if resp == 'n':
        break
#Quantas pessoas foram cadastradas
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
#Pessoas mais pesadas
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
#Pessoas mais leves
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()