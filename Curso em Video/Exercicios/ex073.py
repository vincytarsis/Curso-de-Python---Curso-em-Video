""" Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Inglês de Futebol,
na ordem de colocação. Depois mostre: A: Apenas os 5 primeiros colocados; B: Os últimos 4 colocados da
tabela; C: Uma lista com os time em ordem alfabetica; D:Em que posição na tabela está o time do Tottenham."""

#Tupla com 20 times
times = ('City', 'Chelsea', 'Liverpool', 'Arsenal', 'West Ham', 'Tottenham', 'United', 'Wolves', 'Brighton', 'Leicester', 'Southampton', 'Crystal Palace', 'Brentford', 'Aston Vila', 'Everton', 'Leeds', 'Watford', 'Burnley', 'Newcastle', 'Norwich')
#Os 5 primeiros
print(times[0:5])
#Os últimos 5
print(times[-5:])
#Ordem alfabetica
print(sorted(times))
#Onde está o Tottenham
print(f'Posição do Tottenham na temporada: {times.index("Tottenham")}° position')