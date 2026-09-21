"""
Exercício desempenho aluno merge
Nome do aluno: Camila Ramos de Amorim
Matrícula: 202502813708
Email: Camilaramosamorim7@gmail.com
"""
#merge = qnd temos que trabalhar com duas tabelas diferentes
#a gnt pega uma coluna em comum, e as tabelas se juntam
# ex = ID

import pandas as pd
df_localidades = pd.read_excel("alunos_localidade_carro_merge.xlsx")
df_alunos = pd.read_csv("alunos_desempenho.csv")
pd.merge(df_alunos, df_localidades, on="id_aluno")


#inner join = pega oq tem em comum nas duas tabelas
#left join = pega tudo da tabela da esquerda e oq tem em comum da tabela da direita
#right join = pega tudo da tabela da direita e oq tem em comum da tabela da esquerda
#outer join = pega tudo das duas, mesmo q n tenha em comum


#. Quais variáveis existem na base de desempenho e quais existem na base complementar? 
df_localidades.info()
df_alunos.info()

#2. Qual variável deve ser utilizada como chave para realizar o pd.merge? 
pd.merge(df_alunos, df_localidades, on="id_aluno", how= "left")

#3. Por que id_aluno é uma chave mais segura do que o nome do estudante? 
# O ID é único para cada aluno, enquanto o nome pode se repetir ou ter variações (ex: apelidos, erros de digitação).

# 4. Antes do merge, quantos registros existem em cada base? 
df_localidades.shape
df_alunos.shape

# 5. Realize o merge utilizando id_aluno. Quantos estudantes existem na base resultante? 
df = pd.merge(df_alunos, df_localidades, on="id_aluno", how= "left")

# 6. Todos os estudantes foram associados corretamente? Como você verificou isso? 
df = pd.merge(df_alunos, df_localidades, on="id_aluno", how= "outer", indicator = True)

#pq usamos indicator = True,pq ele vai criar uma coluna chamada_merge, e vai mostrar se o aluno está presente em ambas as tabelas,ou só em uma

# 7. Existe algum estudante presente apenas em uma das bases? Se houver, como você identificaria esses casos? 
#Não

# 8. Qual tipo de merge é mais adequado para preservar todos os estudantes da base principal? Justifique. 
# é o left join, pq vai pegar tds os alunos da tabela da esquerda, e os q tiverem em comum na tabela da direita, vai trazer tbm

#JSON tem formato de dicionário no Python

#API é um conjunto de regras e protocolos que permite que diferentes sistemas de software se comuniquem e troquem dados entre si

import requests
cep = "72015025"
url = f"https://viacep.com.br/ws/{cep}/json/"
response =requests.get(url)
dados = response.json()  #to perguntando p site, ode é o lugar do cep e ele me da em json
pd.DataFrame([dados])

#oq é um formato json = é um formato de texto que permite a representação de dados estruturados em JavaScript
# qnd ta o status 200 ta falando ok


import requests
import pandas as pd
ceps = df["cep"].unique()
dados_ceps = []
for cep in ceps:
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response =requests.get(url)
    dados = response.json()
    dados_ceps.append(dados)
    print(cep)
df_endereco=pd.DataFrame(dados_ceps)

#consulta latitude e longitude a partir dos endereços

import requests
endereco = "SQN 216 Brasília DF"
url = "https://nominatim.openstreetmap.org/search"
params = {
    "q": endereco,
    "format": "json",
    "limit": 1,
    "countrycodes": "br"
    
}
headers = {
    "User-Agent": "meu_projeto_geocoding/1.0"
}
response =requests.get(url,params=params, headers = headers)
dados = response.json()
dados
lat_ibmec = float(dados[0]["lat"])
lon_ibmec = float(dados[0]["lon"])
print(lat_ibmec, lon_ibmec)


#############################################################################
#############################################################################

import requests
import pandas as pd
from math import radians, sin, cos, sqrt, atan2


# 1. Pegar os endereços dos CEPs dos alunos
ceps = df["cep"].unique()

dados_ceps = []

for cep in ceps:
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    dados = response.json()
    dados_ceps.append(dados)

df_endereco = pd.DataFrame(dados_ceps)


# 2. Descobrir a latitude e longitude do IBMEC
endereco_ibmec = "SQN 216 Brasília DF"

url = "https://nominatim.openstreetmap.org/search"

params = {
    "q": endereco_ibmec,
    "format": "json",
    "limit": 1,
    "countrycodes": "br"
}

headers = {
    "User-Agent": "meu_projeto_geocoding/1.0"
}

response = requests.get(url, params=params, headers=headers)
dados = response.json()

lat_ibmec = float(dados[0]["lat"])
lon_ibmec = float(dados[0]["lon"])

##############################################################
##############################################################


import requests
import pandas as pd
import time
enderecos = df_endereco["logradouro"].unique()
lista_enderecos = []
for endereco in enderecos:
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": endereco,
        "format": "json",
        "limit": 1,
        "countrycodes": "br"
    }
    headers = {
        "User-Agent": "meu_projeto_geocoding/1.0"
    }
    response = requests.get(url, params=params, headers=headers)
    dados = response.json()
    if dados:
        latitude = float(dados[0]["lat"])
        longitude = float(dados[0]["lon"])
        lista_enderecos.append({
            "logradouro": endereco,
            "latitude": latitude,
            "longitude": longitude
        })
    time.sleep(1)
    print(endereco)
df_coordenadas = pd.DataFrame(lista_enderecos)
# Latitude e longitude do Ibmec
import requests
endereco_ibmec = "SIG Quadra 4, Brasília, DF, Brasil"
url = "https://nominatim.openstreetmap.org/search"
params = {
    "q": endereco_ibmec,
    "format": "json",
    "limit": 1,
    "countrycodes": "br"
}
headers = {"User-Agent": "meu_projeto_geocoding/1.0"}
response = requests.get(url, params=params, headers=headers)
dados_ibmec = response.json()
lat_ibmec = float(dados_ibmec[0]["lat"])
lon_ibmec = float(dados_ibmec[0]["lon"])
print(lat_ibmec, lon_ibmec)
# Calcula a distacia entre dois pontos (latitude e longitude)
from math import radians, sin, cos, sqrt, atan2
def calcular_distancia(lat1, lon1, lat2, lon2):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distancia = 6371 * c
    return distancia

import requests
import pandas as pd
import time
from math import radians, sin, cos, sqrt, atan2





















#alternativa

import time

latitudes = []
longitudes = []

for _, linha in df_endereco.iterrows():
    
    endereco = f"{linha['logradouro']}, {linha['bairro']}, {linha['localidade']}, {linha['uf']}, Brasil"
    
    url = "https://nominatim.openstreetmap.org/search"
    
    params = {
        "q": endereco,
        "format": "json",
        "limit": 1,
        "countrycodes": "br"
    }
    
    headers = {
        "User-Agent": "meu_projeto_geocoding/1.0"
    }
    
    response = requests.get(url, params=params, headers=headers)
    dados = response.json()
    
    if len(dados) > 0:
        latitudes.append(float(dados[0]["lat"]))
        longitudes.append(float(dados[0]["lon"]))
    else:
        latitudes.append(None)
        longitudes.append(None)
    
    time.sleep(1)

df_endereco["latitude"] = latitudes
df_endereco["longitude"] = longitudes

from math import radians, sin, cos, sqrt, atan2
def distancia(lat1, lon1, lat2, lon2):
    
    R = 6371
    
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    return R * c

df_endereco["distancia_ibmec"] = df_endereco.apply(
    lambda linha: distancia(
        linha["latitude"],
        linha["longitude"],
        lat_ibmec,
        lon_ibmec
    ),
    axis=1
)

df_endereco.head()