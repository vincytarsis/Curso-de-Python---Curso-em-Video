lanche = ('hamburger', 'sopa', 'suco', 'pudin')
#print(lanche[1:3])
#print(lanche[:2])
#print(lanche[-3:])

#Tuplas são imutaveis
# lanche[1] = 'bolacha' Modo errado

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

print(len(lanche))

#for comida in lanche:
    #print(f'Comi {comida} tudo')

#for pos, comida in enumerate(lanche):
    #print(f'Eu vou comer {comida} na position {pos}')
#print(f'Comi pra caramba')

#Trocando a ordem

#print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

#print(len(c))
#print(c)
#print(c.count(5)) # Numero de vezes que o '5' aparece
#print(c.index(8,0)) # Em que posição está o '8', pega a primeira posição (8, 1) Verifica qual a posição do 8 apartir da posição 1

#pessoa = ('Vincy', 15, 'M', 95)
#del(pessoa)#Apaga a Tupla
#print(pessoa)
