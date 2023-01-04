*Este programa não resulta em uma recomendação de compra ou venda de ações*

Magic Formula por Joel Greenblatt
O programa executa a Fórmula Magica estabelecida por Joel GreenBlatt

As etapas que foram utilizadas:

Download dos dados das ações das empresas sem filtro prévio em formato .csv.  Nesse caso, os dados extraídos do site StatusInvest
Determinar o valor de liquidez média diária para iniciar os filtros
De forma ascendente, ordenar os dados utilizando a coluna EV/EBIT e inserir números de 1 ao número de linhas da planilha em uma coluna "RANKING EV/EBIT"
De forma descendente, ordenar os dados utilizando a coluna ROIC e inserir números, de 1 ao número de linhas da planilha em uma coluna "RANKING ROIC"
Criar uma coluna "SOMA RANKING" e somar as colunas "RANKING EV/EBIT" e "RANKING ROIC"
De forma ascendente, ordenar os dados utilizando a coluna "SOMA RANKING"
Exibir as 20 empresas dessa lista.
Fazer uma análise mais detalhada dessas empresas, pois pode haver divergências nos balanços

Feito esse programa para colocar em prática algumas funções das bibliotecas:
- OS (Encontrar arquivos em pastas)
- PANDAS (Filtro de colunas de acordo com conteúdo pré-determinado, carregar e salvar planilhas)
