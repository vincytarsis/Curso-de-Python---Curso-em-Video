""" Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente. """

#Cadastrar valores em uma lista

numeros = []
while True:
    n = int(input('Digite um valor: '))
#Não pode repetir o número
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado. Não vou adicionar...')
#Deseja continuar ao usuario
    res = str(input('Deseja continuar? [S/N]')).upper()
    if res in 'N':
        break

#todos os valores unicos digitados em ordem crescente
print(f'Você digitou os valores {sorted(numeros)}')