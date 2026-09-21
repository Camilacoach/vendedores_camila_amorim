"""
Exercício desempenho aluno
Nome do aluno: Camila Ramos de Amorim
Matrícula: 202502813708
Email: Camilaramosamorim7@gmail.com
"""

import pandas as pd
import statsmodels.api as sm
import seaborn as sns
df = pd.read_csv("alunos_desempenho.csv")
df.shape 

#1. EXPLORAÇÃO INICIAL 

#1. O que representa cada linha do DataFrame? 
df.head()
df.tail(10)

#2. O que representa cada coluna? 
df.columns

#3. Qual é a unidade de análise desta base? 
"as informações dos alunos"

#4. Quantas linhas existem? 
df.shape[0]

#5. Quantas colunas existem? 
df.shape[1]

#6. O número de linhas representa exatamente o número de estudantes? Explique. 
# Sim, cada linha representa um estudante único, pois eles tem ID único.
df["id_aluno"].duplicated().sum()

#7. Liste todas as variáveis da base. 
df.info()

#8. Classifique as variáveis como identificadoras, categóricas ou quantitativas. 
# Identificadoras: ID, aluno
# Categóricas: curso,período, trabalha_atualmente
# Quantitativas: Idade, Notas, horas_estudo, participação_aula, horas_trabalho

df["participacao_aula"].unique()
df["participou_monitoria"].unique()


#2. ESTRUTURA E ORGANIZAÇÃO 

#9. Quais variáveis são numéricas? 
df.info()

#10. Quais variáveis aparecem como object? 
"nenhuma"

#11. Por que aluno, curso e período não são variáveis numéricas? 
"porque são categóricos"

#12. A presença de dados faltantes pode alterar o tipo de uma coluna? Explique,no sentido de mudar de categórica p numérica
df.isnull().sum()
df.isna().sum()
"não"

#13. Qual a vantagem de selecionar apenas as variáveis necessárias para uma determinada análise? 
df.columns
col = ['id_aluno', 'aluno', 'curso', 'periodo', 'nota_final', 'faltas']
df_filtrado = df[col]
print(df_filtrado)

#3. QUALIDADE DOS DADOS 

#14. Quais colunas possuem valores faltantes?
df.isna().sum()

#15. Quantos valores faltantes existem em cada coluna?
df.isna().sum() 

#16. Qual variável possui maior quantidade de dados faltantes?
df.isna().sum().sort_values(ascending=False)

#17. Uma coluna com aproximadamente 3% de dados ausentes deveria ser automaticamente eliminada? Explique. 
"Não, pois perderíamos informações que podem ser relevantes para a análise"

#18. Quantos alunos estão sem nota final? 
df.isna().sum() 

#19. Podemos utilizar esses estudantes para calcular a média das notas? Explique.
"Não, pois estaríamos inferindo a nota final desses alunos"

#20. Seria correto substituir todas as notas faltantes por zero? Justifique. 
"Não, pois isso poderia distorcer os resultados da análise e não refletiria a realidade dos dados."


#4. REGISTROS DUPLICADOS 

#21. Existem linhas completamente duplicadas? 
df.duplicated().sum()

#22. Por que duplicidades podem prejudicar uma análise? 
"pois você acrescenta uma informação já existente na análise"

#23. Por que seria um problema encontrar dois alunos diferentes com o mesmo id_aluno? 
"pois a função da coluna do id estaria inutilizada"

#5. ANÁLISE DESCRITIVA BÁSICA 

#24. Qual é a média da nota final? 
df["nota_final"].mean()

#25. Qual é a mediana da nota final? 
df["nota_final"].median()

#26. Qual é o número médio de faltas? 
df["faltas"].mean()
#27. Qual é o máximo de faltas registrado? 
df["faltas"].max()

#28. Qual é a maior quantidade de horas de estudo semanal? 
df["horas_estudo_semana"].max()

#29. Algum valor parece estranho ou muito distante dos demais? Cite exemplos. 
"sim, as faltas, pois foram 45"
df["horas_estudo_semana"].describe()
df.describe()

#30. A média e a mediana da nota são semelhantes? O que essa comparação pode indicar? 
"pode indicar que existem valores extremos, mas sim são semelhantes, mostrando que não existem outliers"

#31. Compare a média, a mediana e o máximo da variável faltas. O que você observa?
df["faltas"].describe()
df["faltas"].median()
df["faltas"].max()


#6. IDENTIFICAÇÃO DE OUTLIERS 

#32. Existem estudantes com quantidade de faltas muito superior aos demais? 

#33. Existem valores muito elevados de horas de estudo? 

#34. Existem jornadas de trabalho extremamente altas? 

#35. Esses valores necessariamente são erros? Explique. 

#36. Quantos possíveis outliers foram encontrados para faltas pelo método do intervalo interquartil? 

#37. Qual é o maior número de faltas? 

#38. Um valor identificado como outlier deve ser automaticamente removido? Justifique. 


#9. FILTROS 

#47. Quantos estudantes possuem nota inferior a 7? 
filtro = df["nota_final"] < 7
df_menor_7 = df[filtro] 
#supor agr p colocar colunas
filtro = df["nota_final"] < 7
col= ["aluno", "nota_final"]
df[filtro] [col]

#48. Quantos estudantes possuem mais de 10 faltas? 
filtro = df["faltas"] > 10
df[filtro] 

#49. Quantos estudantes possuem nota inferior a 7 e mais de 10 faltas? 
filtro = (df["nota_final"] < 7) & (df["faltas"] > 10)
df_pior = df[filtro] 

# "ou" é |
#50. Todos os estudantes com nota baixa possuem muitas faltas? 
df_menor_7.shape[0]
df_pior.shape[0]
"Não pois tem alunos com notas menores que 7 e com faltas inferiores a 10"


#se quiser colocar igual a 7
filtro = df["faltas"] == 7
df[filtro] 


#10. ORDENAÇÃO DOS DADOS 

#51. Quem são os cinco estudantes com maiores notas? 
col = ["aluno", "nota_final"]
df[col].sort_values (by=["nota_final", "aluno"], ascending= False).head(5)

#ascending=True → menor → maior
#ascending=False → maior → menor

#52. Os estudantes com menores notas possuem necessariamente muitas faltas?
"Não pois tem alunos com notas menores que 7 e com faltas inferiores a 10"
df[col].sort_values (by=["nota_final"], ascending= True).head(10)



# 11. ANÁLISE POR GRUPOS 

# 53. Existe diferença relevante entre as médias dos cursos? 
df.columns
df["curso"]
df.groupby("curso")["nota_final"].mean()

#df.groupby("curso") - Agrupa os alunos de acordo com o curso.

# 54. Qual período apresenta maior média? 
df.groupby("periodo")["nota_final"].mean()

# 55. Estudantes que participaram da monitoria apresentam média maior? 
df.groupby("participou_monitoria")["nota_final"].mean()

# 56. Podemos afirmar que a monitoria causou o aumento das notas? Explique. 
"Não, pois não há nada que fale causalidade, apenas uma correlação entre as variáveis "

# 57. Existe diferença entre alunos que trabalham e alunos que não trabalham? 
df.groupby("trabalha_atualmente")["nota_final"].mean()

# 58. Essa diferença, caso exista, é suficiente para estabelecer causalidade? 
"Não"

# 59. Por que analisar somente a média pode ser insuficiente? 
"Pois os outliers podem afetar as médias"


# 12. RELAÇÃO ENTRE FALTAS E NOTAS 

# 60. A correlação entre faltas e nota final é positiva, negativa ou próxima de zero? 
col = ["nota_final", "faltas"]
df[col].corr()

#corr - correlação

# 61. O sinal da correlação está de acordo com a hipótese inicial? 
"Sim"

# 62. Quanto mais próximo de -1 estiver o valor da correlação, o que isso significa? 
"Significa que é inversamente correlacionado, ou seja, qnt mais faltas, menor a nota final"


# 13. HORAS DE ESTUDO E NOTA 

# 63. Existe associação entre horas de estudo e nota? 
col = ["horas_estudo_semana", "nota_final"]
df[col].corr() 

# 64. A associação encontrada é positiva ou negativa? 
"Positiva, mais estudo, maior a nota"

# 65. Horas de estudo parecem ter relação com desempenho? Explique com base nos dados. 
"Sim"

# 14. MATRIZ DE CORRELAÇÃO 

# 66. Qual variável apresenta maior correlação positiva com nota_final? 
df.corr(numeric_only=True).sort_values(["nota_final"])

# 67. Qual variável apresenta maior correlação negativa com nota_final? 
df.corr(numeric_only=True).sort_values(by="nota_final", ascending=True).head(1)

# 68. Alguma correlação surpreendeu você? Explique. 