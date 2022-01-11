""" Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar. No final, mostre: -A: quantas pessoas tem mais de 18
anos; -B: quantos homens foram cadastrados; -c: quantas mulheres tem menos de 20 anos."""

cont_id = homem = mulher = 0

while True:
        id = int(input('Idade:'))
        if id > 18:
            cont_id += 1
        sx = str(input('[H/M]')).strip().upper()
        if sx == 'H':
            homem += 1
        else:
            if id < 20:
                mulher += 1

        cont = str(input('Quer continuar?[S/N]:')).strip().upper()[0]
        if cont == 'N':
            break

print(f'Pessoas com mais de 18 anos: {cont_id}')
print(f'Homems cadastrados:{homem}')
print(f'Mulheres com menos de 20 anos: {mulher}')
print('Acabou')
