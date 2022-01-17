""" Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A: Quantos
números foram digitados; B: A lista de valores, ordenada de forma decrescente; C: Se o valor 5 foi digitado
e está ou não na lista. """

#Ler varios números em uma lista
lista = []
vl5 = 0
while True:
    n = int(input('Digite um valor:'))
    if n == 5:
        vl5 += 1
    lista.append(n)
    res = str(input('Quer continuar? [S/N]')).upper()
    if res in 'N':
        break
#Quantos números foram digitados
print(f'Você digitou {(len(lista))} elementos')
#Lista em ordem decesente
lista.sort(reverse=True)
print(lista)
#Se o valor 5 foi digitado
print(f'O valor 5 foi digitado {vl5}' if vl5 > 0 else 'O valor 5 não faz parte da lista!')
