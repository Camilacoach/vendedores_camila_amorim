import sqlite3 #conexão com banco de dados sqlite
import pandas as pd
engine = sqlite3.connect('db_alunos.db')
query = 'select * from tb_alunos_final'
df_carros = pd.read_sql(query, con=engine)
col  = ['id_aluno','valor_carro_10mil']
df_carros = df_carros[col]
df_carros

# regressao linear
import sqlite3 # conexão com banco de dados sqlite
import pandas as pd
engine = sqlite3.connect('db_alunos.db')
query = 'select * from tb_alunos_final'
df_final = pd.read_sql(query, con=engine)
df_final

#usa statsmodel p rodar a regressão
import statsmodels.api as sm
X = df_final['faltas']
Y = df_final['nota_final']
X = sm.add_constant(X)
modelo = sm.OLS(Y, X, missing='drop').fit()
print(modelo.summary())
#definiçao colunas- variaveis independentes
col = ['faltas','horas_estudo_semana','participacao_aula','horas_trabalho_semana','horas_sono_noite','distancia_faculdade_km','valor_carro_10mil']
x = df_final[col]
y = df_final['nota_final']
x = sm.add_constant(x)
modelo = sm.OLS(y, x, missing='drop').fit()
print(modelo.summary())


#################################
#################################
#GRAFICOS 

#correlação
df_final_numerico = df_final[col]
df_final_numerico.corr()
import seaborn as sns
sns.heatmap(df_final_numerico.corr())

#histograma
sns.histplot(df_final_numerico, x='faltas', bins=12)    
#boxplot
sns.boxplot(df_final_numerico)
#dispersão
col = ['nota_final','faltas']
df_final_regressao = df_final[col]
sns.regplot(df_final_regressao, x='nota_final', y ='faltas')