""" Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
lista única que mantenha separados os valores pares e impares. No final, mostre os valores
pares e ímpares em ordem crescente. """

'''princ = []
par = []
imp = []
#Ler 7 valores numéricos
for c in range(1, 8):
    n = int(input(f'Digite o {c}°. valor:'))
    if n % 2 == 0:
        par.append(n)
    else:
        imp.append(n)
    # Cadastrar em uma lista única
    princ.extend(par)
    princ.extend(imp)
    imp.clear()
    par.clear()
#Separ pares e impares
p = 0
if princ[p] % 2 ==0:
    print(princ)
    p +=1
else:
    print(princ)
    p+=1
#print(par)
#print(imp)

#Mostre os valores separados'''

#Guanabara
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite {c}° o valor'))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores impares digitados foram {num[1]}')