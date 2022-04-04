""" Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma
 função chamada leiaDinheiro() qye seha capaz de funcionar como a função input(), mas como uma validação
 de dados para aceitar apenas valores que sejam monetários."""

from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado

p = dado.leiaDinheiro('Digite um preço: R$')
moeda.resumo(p, 20, 12)
