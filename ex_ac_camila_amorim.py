# AC - AVALIAÇÃO CONTINUADA: desempenho de vendedores 
import pandas as pd
import statsmodels.api as sm
import seaborn as sns





# Orientações: Utilize Pandas para manipulação dos dados, Statsmodels para a regressão e Seaborn para as visualizações. 

# Arquivos fornecidos: vendedores_desempenho.csv ; vendedores_contexto.csv 

# Objetivo: A empresa deseja investigar quais fatores estão associados ao desempenho mensal de seus vendedores. As duas bases contêm informações complementares que deverão ser integradas antes da análise. 

# 1. Integração e qualidade dos dados 

# Leia os dois arquivos CSV em DataFrames do Pandas. 

# Informe a quantidade de linhas e colunas de cada base. 

# Identifique qual coluna deve ser utilizada como chave para integrar as duas bases. 

# Verifique se a chave identificada é única em cada base. 

# Faça o merge das duas bases preservando todos os vendedores da base de desempenho. 

# Informe a quantidade de registros após o merge. 

# Verifique a quantidade de valores ausentes em cada variável da base integrada. 

# Identifique quais variáveis possuem dados faltantes e comente possíveis razões para isso. 

# 2. Estatística descritiva 

# Calcule a média de vendas_mes. 

# Calcule a mediana de vendas_mes. 

# Informe o valor mínimo e o valor máximo de vendas_mes. 

# Identifique possíveis outliers em vendas_mes usando o critério do intervalo interquartil (IQR). 

# Compare a média de vendas entre vendedores que recebem bônus e vendedores que não recebem bônus. 

# Calcule a correlação entre as variáveis 

# Interprete o sinal das correlações encontradas. 

# 3. Regressão linear múltipla 

# Crie uma base para regressão contendo apenas as variáveis: vendas_mes, horas_treinamento, faltas, numero_clientes, distancia_empresa_km e salario. 

# Remova apenas as observações com dados ausentes nas variáveis que serão utilizadas no modelo. 

# Informe quantas observações foram utilizadas na regressão. 

# Defina vendas_mes como variável dependente. 

# Utilize como variáveis explicativas: horas_treinamento, faltas, numero_clientes, distancia_empresa_km e salario. 

# Adicione a constante ao modelo e estime uma regressão linear múltipla utilizando Statsmodels. 

# Apresente o resumo completo da regressão. 

# Interprete o coeficiente de horas_treinamento, mantendo as demais variáveis constantes. 

# Interprete o coeficiente de faltas, mantendo as demais variáveis constantes. 

# Interprete o coeficiente de numero_clientes, mantendo as demais variáveis constantes. 

# Interprete o coeficiente de distancia_empresa_km. 

# Interprete o coeficiente de salario. 

# Apresente os p-valores de todas as variáveis explicativas. 

# Identifique quais variáveis são estatisticamente significativas ao nível de 5%. 

# Identifique quais variáveis não apresentam evidência estatística de associação com vendas_mes ao nível de 5%. 

# Informe o valor do R² do modelo. 

# 4. Visualizações finais 

# Construa um histograma de vendas_mes utilizando Seaborn. 

# Construa um boxplot de vendas_mes utilizando Seaborn. 

# Construa um gráfico de dispersão com linha de regressão entre numero_clientes e vendas_mes. 

# Construa um gráfico com os coeficientes da regressão e seus intervalos de confiança de 95%. 