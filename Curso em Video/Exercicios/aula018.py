'''teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [['Joao', 19], ['Beto', 20], ['Bia', 15], ['Pio', 30]]
print(galera[0][0])
print(galera[2][1])
print(galera[3][0])

for p in galera:#pessoas
    #print(p)
    print(f'{p[0]} tem {p[1]} anos')'''

galera = []
dado = []
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('NOme:')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()

#print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen +=1

print(f'Temos {totmai} maiores e {totmen} menores de idade')
