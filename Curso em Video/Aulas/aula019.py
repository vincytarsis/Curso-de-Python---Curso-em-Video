'''pessoas = {'nomes':'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nomes"]} tem {pessoas["idade"]}anos de idade') #Jeito correto de formatar
pessoas['nomes'] = 'Leandro'#Adicionar
pessoas['peso'] = 95
print(pessoas.keys()) #Chaves
print(pessoas.values()) #Valores
print(pessoas.items()) #Itens
for k, v in pessoas.items():
    print(f'{k} = {v}')
del pessoas["sexo"] #apagar'''

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])'''

estado = {}
brasil = []

for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Siglado do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    #print(e) #Visualização simples
    #for k, v in e.items():
       # print(f'O campo{k} tem valor {v}')
    for v in e.values():
        print(v, end=' ')
    print()

