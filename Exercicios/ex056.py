""" Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. No final do programa, mostre:
 -A média da idade do grupo; -Qual é o nome do homem mais velho; -Quantas mulheres têm menos de 20 anos. """

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
total_mulher_20 = 0

for p in range(1, 5):
    print('------- {}º PESSOA -------'.format(p))

    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()

    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher_20 += 1

    soma_idade += idade

media_idade = soma_idade / 4

print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho se chama {} e tem {} anos'.format(nome_velho, maior_idade_homem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(total_mulher_20))