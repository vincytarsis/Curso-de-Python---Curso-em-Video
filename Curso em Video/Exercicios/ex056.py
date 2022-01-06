""" Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. No final do programa, mostre:
 -A média da idade do grupo; -Qual é o nome do homem mais velho; -Quantas mulheres têm menos de 20 anos. """

total_idade = 0
man_velho = 0

for i in range(1, 3):
    name = str(input('People {}\nName:'.format(i)))
    age = int(input('Age:'))
    sex = int(input('[1] Man | [2] Woman:'))

    #Homem mais velho
    if i == 1:
        man_velho = age
    else:
        if age > man_velho:
            man_velho = age
            name_hv = name
    total_idade = total_idade + age

#print('Media de idade do grupo:{} anos'.format(total_idade / i))
print('{} mais velho:{}'.format(, man_velho))
