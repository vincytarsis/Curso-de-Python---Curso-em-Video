""" Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos
gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado
corretamente. """

def jogador(nome, num_gols=0):
  if nome == '':
    nome = '<desconhecido>'
   if num_gols == '':
    num_gols = 0
   return f'O jogador {nome} fez {num_gols} gols(s) no campeonato'

#Programa Principal
nome = input('Nome do Jogador: ')
num_gols = str(input('Número de Gols: '))

print(jogador(nome, num_gols))

#Guanabara Solutions...

def ficha(jog='desconhecido>', gol=0):
  print(f'O jogador {jog} fez {gol} gol(s) no campeonato.)
        
#Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
  g = int(g)
else:
  g = 0
if n.strip() == '':
  ficha(gol = g)
else:
  ficha(n, g)
