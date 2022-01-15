""" Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
 foi o maior e o menor valor digitado e as suas respectivas posições. """

#Ler 5 valores e guarde em uma lista
valores = list()
maior = pos_men = 0

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor na Posição {cont}:')))
    menor = valores[0]

    if valores[cont] > maior:
        maior = valores[cont]
        pos_mar = cont
    if valores[cont] < menor:
        menor = valores[cont]
        pos_men = cont

print('=-'*30)
print(f'Você digitou os valores {valores}')
#Maior valor e posição
print(f'O maior valor digitado foi {maior} nas posições {pos_mar}')
#Menor valor e posição
print(f'O menor valor digitado foi {menor} nas posições {pos_men}')