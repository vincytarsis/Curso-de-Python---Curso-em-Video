""" Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar. No final, mostre: -A: quantas pessoas tem mais de 18
anos; -B: quantos homens foram cadastrados; -c: quantas mulheres tem menos de 20 anos."""

maior18 = homens = menos20 = 0
# Ler idade
while True:
    idade = int(input('Idade:'))
    if idade > 18:
        maior18 += 1
# Ler sexo
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('[M/F]')).strip().upper()[0]
    if sexo == 'M':
        homens += 1

    else:
        if idade < 20:
            menos20 += 1

# Perguntar se quer continuar
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]')).strip().upper()
    if resp == 'N':
        break
# Pessoas com mais de 18 anos
print(f'Pessoas com mais de 18 anos: {maior18}')
# Homens cadastrados
print(f'Homens cadastrados: {homens}')
# Mulheres com menos de 20 anos
print(f'Mulheres com menos de 20 anos:{menos20}')