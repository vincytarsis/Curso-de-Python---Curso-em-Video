""" Crie um pacote chamado utilidadeCeV que tenha dois internos chamados moedas e dado. Transfira todas as funções
utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcioando. """

from ex111.utilidadescev import moeda,dado


p = float(input('Digite o preço: R$'))
moeda.resumo(p, 20, 12)
