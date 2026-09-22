
# AC - AVALIAÇÃO CONTINUADA: desempenho de vendedores
# Bibliotecas:
#   pandas      -> ler, juntar e manipular as tabelas
#   statsmodels -> estimar a regressão linear (OLS)
#   seaborn     -> gráficos (matplotlib é usado só para exibir/ajustar)
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

# =====================================================================
# 1. INTEGRAÇÃO E QUALIDADE DOS DADOS
# =====================================================================

# --- Leia os dois arquivos CSV em DataFrames do Pandas.
# read_csv transforma cada arquivo em uma tabela (DataFrame).
df_desempenho = pd.read_csv('vendedores_desempenho.csv')
df_contexto = pd.read_csv('vendedores_contexto.csv')

# --- Informe a quantidade de linhas e colunas de cada base.
# .shape devolve (linhas, colunas).
print("Desempenho:", df_desempenho.shape)   # (120, 7)
print("Contexto:  ", df_contexto.shape)     # (118, 4)
_
# RESPOSTA: desempenho tem 120 linhas e 7 colunas; contexto tem 118 linhas e 4 colunas.

# --- Identifique qual coluna deve ser utilizada como chave.
# A chave é a coluna que existe nas duas bases e identifica cada vendedor.
key_column = 'id_vendedor'
# RESPOSTA: id_vendedor (única coluna em comum, identifica cada vendedor).

# --- Verifique se a chave é única em cada base.
# .is_unique retorna True se não há valores repetidos.
print("Chave única em desempenho?", df_desempenho[key_column].is_unique)  # True
print("Chave única em contexto?  ", df_contexto[key_column].is_unique)    # True
# RESPOSTA: sim, é única nas duas (um vendedor por linha), então o merge não duplica linhas.

# --- Faça o merge preservando todos os vendedores da base de desempenho.
# how='left' mantém todas as linhas da tabela da esquerda (desempenho).
# Quem não tiver correspondência em contexto fica com NaN nas colunas dessa base.
df = df_desempenho.merge(df_contexto, on=key_column, how='left')

# --- Informe a quantidade de registros após o merge.
print("Registros após o merge:", len(df))   # 120
# RESPOSTA: 120 registros (os 120 vendedores de desempenho foram preservados).

# --- Verifique a quantidade de valores ausentes em cada variável.
# isnull() marca cada célula vazia como True; sum() conta por coluna.
ausentes = df.isnull().sum()
print(ausentes)
# RESPOSTA (valores ausentes):
#   horas_treinamento = 2 | faltas = 1 | numero_clientes = 1 | vendas_mes = 1
#   distancia_empresa_km = 4 | salario = 3 | recebe_bonus = 2
#   id_vendedor, nome e idade = 0

# --- Identifique quais variáveis têm dados faltantes e comente as razões.
print(ausentes[ausentes > 0])
# RESPOSTA: horas_treinamento, faltas, numero_clientes, vendas_mes,
# distancia_empresa_km, salario e recebe_bonus têm dados faltantes.
# Possíveis razões:
#  - Os vendedores de id 116 e 120 estão na base de desempenho mas NÃO na de
#    contexto: o left join gera NaN em distancia_empresa_km, salario e recebe_bonus.
#  - Campos não preenchidos no cadastro ou não coletados (ex.: distância, salário).
#  - Erros de registro/extração (ex.: vendas do mês não lançadas, faltas não apuradas).

# =====================================================================
# 2. ESTATÍSTICA DESCRITIVA
# =====================================================================
# Obs.: o pandas ignora NaN automaticamente nesses cálculos.

# --- Média de vendas_mes
print("Média:", df['vendas_mes'].mean())         # ~ 49.473,75
# --- Mediana de vendas_mes
print("Mediana:", df['vendas_mes'].median())     # ~ 49.869,53
# --- Mínimo e máximo
print("Mínimo:", df['vendas_mes'].min())         # 20.017,28
print("Máximo:", df['vendas_mes'].max())         # 88.440,20
# RESPOSTA: média e mediana muito próximas, o que indica distribuição
# aproximadamente simétrica (sem forte assimetria).

# --- Outliers pelo critério IQR
# IQR = Q3 - Q1. Consideramos outlier o que estiver abaixo de Q1 - 1,5*IQR
# ou acima de Q3 + 1,5*IQR.
Q1 = df['vendas_mes'].quantile(0.25)
Q3 = df['vendas_mes'].quantile(0.75)
IQR = Q3 - Q1
lim_inf = Q1 - 1.5 * IQR
lim_sup = Q3 + 1.5 * IQR
outliers = df[(df['vendas_mes'] < lim_inf) | (df['vendas_mes'] > lim_sup)]
print(f"Limites: [{lim_inf:.2f}, {lim_sup:.2f}]")   # [14.317,45 ; 83.975,31]
print(outliers[[key_column, 'vendas_mes']])
# RESPOSTA: há 1 outlier (limite superior), o vendedor id 92, com vendas de 88.440,20.

# --- Compare a média de vendas entre quem recebe e quem não recebe bônus
# groupby separa em grupos (Sim/Não) e calculamos a média de cada um.
print(df.groupby('recebe_bonus')['vendas_mes'].mean())
# RESPOSTA: Sim ≈ 53.745,47 | Não ≈ 45.481,95.
# Quem recebe bônus vende, em média, cerca de 8.263 a mais.
# (Comparação descritiva, não prova que o bônus causa mais vendas.)

# --- Correlação entre as variáveis
# Só colunas numéricas; removemos id_vendedor porque é apenas um identificador.
corr = df.select_dtypes(include='number').drop(columns=[key_column]).corr()
print(corr.round(3))
print(corr['vendas_mes'].sort_values(ascending=False))
# RESPOSTA (correlação com vendas_mes):
#   numero_clientes = +0,740 | horas_treinamento = +0,284 | faltas = -0,114
#   distancia_empresa_km = -0,082 | salario = -0,058 | idade = -0,018

# --- Interprete o sinal das correlações
# RESPOSTA:
#  - Positiva: quando a variável sobe, vendas tendem a subir.
#    numero_clientes (forte) e horas_treinamento (fraca/moderada).
#  - Negativa: quando a variável sobe, vendas tendem a cair.
#    faltas, distancia_empresa_km, salario e idade, mas todas são muito
#    próximas de zero, ou seja, associação linear praticamente inexistente.
#  - Correlação mede associação, não causalidade.

# =====================================================================
# 3. REGRESSÃO LINEAR MÚLTIPLA
# =====================================================================

# --- Base para regressão só com as variáveis pedidas
vars_modelo = ['vendas_mes', 'horas_treinamento', 'faltas',
               'numero_clientes', 'distancia_empresa_km', 'salario']

# --- Remova apenas observações com ausentes nessas variáveis
# dropna() só olha as colunas selecionadas (ausência em 'recebe_bonus' não importa).
df_reg = df[vars_modelo].dropna()

# --- Quantas observações foram usadas?
print("Observações na regressão:", len(df_reg))   # 110
# RESPOSTA: 110 observações (das 120, 10 foram removidas por terem NaN).

# --- Defina vendas_mes como dependente (y) e as demais como explicativas (X)
y = df_reg['vendas_mes']
X = df_reg[['horas_treinamento', 'faltas', 'numero_clientes',
            'distancia_empresa_km', 'salario']]

# --- Adicione a constante (intercepto) e estime a regressão
# O statsmodels NÃO inclui o intercepto sozinho; add_constant cria essa coluna.
X = sm.add_constant(X)
modelo = sm.OLS(y, X).fit()      # OLS = mínimos quadrados ordinários

# --- Resumo completo
print(modelo.summary())

# --- Interpretação dos coeficientes (mantendo as demais variáveis constantes)
# RESPOSTA:
#  horas_treinamento (≈ +1.022,58): cada hora a mais de treinamento está
#    associada a ~R$ 1.022,58 a mais em vendas no mês.
#  faltas (≈ -1.014,37): cada falta a mais está associada a ~R$ 1.014,37
#    a menos em vendas no mês.
#  numero_clientes (≈ +990,38): cada cliente a mais está associado a
#    ~R$ 990,38 a mais em vendas no mês.
#  distancia_empresa_km (≈ +49,62): cada km a mais está associado a ~R$ 49,62
#    a mais em vendas, mas o efeito NÃO é estatisticamente significativo,
#    então não há evidência de que seja diferente de zero.
#  salario (≈ +0,51): cada R$ 1 a mais de salário está associado a ~R$ 0,51
#    a mais em vendas, também NÃO significativo.

# --- p-valores de todas as variáveis explicativas
print(modelo.pvalues.round(4))
# RESPOSTA:
#   horas_treinamento ≈ 0,0001 | faltas ≈ 0,0406 | numero_clientes ≈ 0,0000
#   distancia_empresa_km ≈ 0,5472 | salario ≈ 0,4628

# --- Significativas e não significativas a 5% (p < 0,05)
p = modelo.pvalues.drop('const')
print("Significativas:", p[p < 0.05].index.tolist())
print("Sem evidência:", p[p >= 0.05].index.tolist())
# RESPOSTA:
#   Significativas a 5%: horas_treinamento, faltas, numero_clientes.
#   Sem evidência de associação a 5%: distancia_empresa_km e salario.

# --- R² do modelo
print("R²:", round(modelo.rsquared, 4))   # ≈ 0,632
# RESPOSTA: R² ≈ 0,63, ou seja, o modelo explica cerca de 63% da variação
# das vendas mensais.

# =====================================================================
# 4. VISUALIZAÇÕES FINAIS
# =====================================================================
sns.set_theme(style="whitegrid")

# --- Histograma de vendas_mes (mostra a forma da distribuição)
plt.figure(figsize=(8, 5))
sns.histplot(df['vendas_mes'], bins=20, kde=True)
plt.title('Distribuição de vendas_mes')
plt.xlabel('Vendas no mês')
plt.ylabel('Frequência')
plt.show()

# --- Boxplot de vendas_mes (mediana, quartis e outliers como pontos)
plt.figure(figsize=(6, 5))
sns.boxplot(y=df['vendas_mes'])
plt.title('Boxplot de vendas_mes')
plt.ylabel('Vendas no mês')
plt.show()

# --- Dispersão com linha de regressão: numero_clientes x vendas_mes
# regplot desenha os pontos e a reta ajustada (relação positiva esperada).
plt.figure(figsize=(8, 5))
sns.regplot(data=df, x='numero_clientes', y='vendas_mes',
            scatter_kws={'alpha': 0.6}, line_kws={'color': 'red'})
plt.title('Número de clientes x Vendas no mês')
plt.xlabel('Número de clientes')
plt.ylabel('Vendas no mês')
plt.show()

# --- Coeficientes da regressão com IC de 95%
# conf_int devolve limites inferior e superior de cada coeficiente.
# Tiramos a constante (escala muito diferente) para o gráfico ficar legível.
ic = modelo.conf_int(alpha=0.05).drop('const')
ic.columns = ['inf', 'sup']
coefs = pd.DataFrame({'coef': modelo.params.drop('const')}).join(ic)
erro_inf = coefs['coef'] - coefs['inf']
erro_sup = coefs['sup'] - coefs['coef']

plt.figure(figsize=(8, 5))
plt.errorbar(coefs['coef'], coefs.index, xerr=[erro_inf, erro_sup],
             fmt='o', capsize=4, color='navy')
plt.axvline(0, color='red', linestyle='--')   # linha do zero
plt.title('Coeficientes da regressão com IC de 95%')
plt.xlabel('Coeficiente estimado')
plt.tight_layout()
plt.show()
# LEITURA: se o intervalo NÃO cruza o zero, a variável é significativa a 5%
# (horas_treinamento, faltas, numero_clientes). Se cruza o zero
# (distancia_empresa_km, salario), não há evidência de efeito.