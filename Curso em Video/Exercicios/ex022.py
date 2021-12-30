# Crie um programa que leia o nome completo de uma pessoa e mostre:
# -O nome com todas as letras maiúsculas
# -O nome como todas as letras minúsculas
# -Quantas letras ao todo (sem considerar espaços)
# -Quantas letras tem o primeiro nome

n = str(input('Digite o seu nome completo: '))

tmsc = n.upper() #Todoas as letras maiúsculas
tmic = n.lower() #Todas as letras minúsculas
qtlt = n.replace(len())  #Quantas letras ao todo

print('Nome com todas as letras maiúsculas:{}'.format(tmsc))
print('Nome com todas as letras minúsculas:{}'.format(tmic))
print('Quantas letras ao todo(sem considerar espaços:{}'.format(qtlt))
