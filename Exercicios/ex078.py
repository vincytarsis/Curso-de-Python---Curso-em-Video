""" Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
 foi o maior e o menor valor digitado e as suas respectivas posições. """

#Ler 5 valores e guarde em uma lista
valores = []

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor na Posição {cont}:')))

print('=-'*30)
print(f'Você digitou os valores {valores}')
#Maior valor e posição
print(f'O maior valor digitado foi {max(valores)} nas posições {(valores.index(max(valores)))}')
#Menor valor e posição
print(f'O menor valor digitado foi {min(valores)} nas posições {(valores.index(min(valores)))}')

#Solução Guanabation
'''listanum = []
mai = men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para Posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()'''