# Algoritmos Genéticos: Sudoku
Este repositório conterá uma proposta para resolução do jogo **sudoku** através dos
algoritmos genéticos.

## Função de avaliação
Para avaliar um dado tabuleiro, é dada uma função que calcula a quantidade de linhas (**m0**),
colunas (**n0**) e diagonais (**d0**) (sub-blocos ainda não) corretas atualmente e divide pela quantidade
máxima de acertos (**m**,**n**,**d**), por fim, multiplica-se o valor por 10 - apenas para mudar a escala.
Portanto temos:

**score** = _(m0+n0+d0) / (m+n+d) * 10_

Onde o objetivo do GA é encontrar soluções que maximizem este score ao máximo possível (10), onde teremos
uma resolução perfeita para o sudoku.
