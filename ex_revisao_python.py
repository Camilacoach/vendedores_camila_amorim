"""
Lista de exercícios de revisão de Python
Disciplina: Programação para Análise de Dados
Nome do aluno: Camila Ramos de Amorim
Matrícula: 202502813708
Email: Camilaramosamorim7@gmail.com

Orientações:
- Resolva cada exercício separadamente.
- Execute o arquivo após cada solução para conferir o resultado.
- Use apenas os comandos básicos estudados em aula.
- Não use IA para resolver os exercícios, pois o objetivo é relembrar e praticar os conceitos aprendidos.
- Duvidas, mande um e-mail para o professor: laerte.takeuti@professores.ibmec.edu.br
- Se quiser mais exercícios, consulte o site: https://www.w3schools.com/python/default.asp
- Se quiser aulas em vídeo, consulte o canal: https://www.youtube.com/watch?v=S9uPNppGsGo&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6
"""
# ============================================================================
# 1. VARIÁVEIS — EXERCÍCIOS 1 A 10
# ============================================================================

# Exercício 1 — Dados pessoais
# Crie quatro variáveis para armazenar seu nome, sua idade, sua altura e se você
# é estudante. Mostre o valor e o tipo de cada variável usando print() e type().

nome = "Camila"
idade = 19
altura = 1.55
estudante = True

print(nome, type(nome))
print(idade, type(idade))
print(altura, type(altura))
print(estudante, type(estudante))


# Exercício 2 — Saudação
# Peça ao usuário seu nome e sua cidade. Depois, mostre a mensagem:
# "Olá, <nome>! Você mora em <cidade>."
nome = input("digite seu nome")
cidade = input("digite sua cidade")
print(f"Olá, {nome}! Você mora em {cidade}.")
# f usa p colocar variável em uma frase


# Exercício 3 — Soma de dois números
# Leia dois números inteiros usando input(), converta-os com int() e mostre
# a soma dos valores.
n1 = input("digite um numero")
n2 = input("digite outro numero")
n1 = int(n1)
n2 = int(n2)
total = n1 + n2
print(total)

# round(n1 variavel, 2) é duas casas decimais depois

# Exercício 4 — Operações básicas
# Leia dois números e mostre o resultado da soma, subtração, multiplicação
# e divisão entre eles.
n1 = 10
n2 = 20
soma = n1 + n2
subtração = n1 - n2
multiplicação = n1 * n2
divisão = n1 / n2
print(soma)
print(subtração)
print(multiplicação)
print(divisão)

# Exercício 5 — Média de três notas
# Leia três notas do tipo float, calcule a média aritmética e mostre o resultado
# com duas casas decimais.
nota1 = float(input("digite a primeira nota"))
nota2 = float(input("digite a segunda nota"))
nota3 = float(input("digite a terceira nota"))
media = (nota1 + nota2 + nota3) / 3
print(f"a média é {media:.2f}")

# Exercício 6 — Idade no futuro
# Peça a idade atual do usuário e informe quantos anos ele terá daqui a 10 anos.
idade = int(input("digite sua idade atual"))
idade_futura = idade + 10
print(f"daqui 10 anos terei {idade_futura} anos")

# Exercício 7 — Conversão de temperatura
# Leia uma temperatura em graus Celsius e converta para Fahrenheit.
# Fórmula: fahrenheit = (celsius * 9 / 5) + 32
celsius = float(input("digite a temperatura em Celsius"))
fahrenheit = (celsius * 9 / 5) + 32
print(fahrenheit)

# Exercício 8 — Área de um retângulo
# Leia a largura e a altura de um retângulo. Calcule e mostre sua área.
# Fórmula: area = largura * altura
largura = 10
altura = 5
area = largura * altura
print(area)

# Exercício 9 — Manipulação de texto
# Peça uma frase ao usuário e mostre:
# a) a frase em letras maiúsculas;
# b) a frase em letras minúsculas;
# c) a quantidade de caracteres da frase.
frase = input("digite uma frase")
print(frase.upper())
print(frase.lower())
print(len(frase))

# Exercício 10 — Preço com desconto
# Leia o nome de um produto, seu preço e um percentual de desconto.
# Calcule e mostre o nome do produto, o valor do desconto e o preço final.
nome = input("digite o nome")
preço = float(input("digite o preço"))
desconto_percentual = float(input("digite o percentual de desconto"))
valor_desconto = preço * desconto_percentual / 100
preço_final = preço - valor_desconto
print(nome)
print(valor_desconto)
print(preço_final)

# ============================================================================
# 2. ESTRUTURA CONDICIONAL — EXERCÍCIOS 11 A 20
# ============================================================================

# Exercício 11 — Positivo, negativo ou zero
# Leia um número e informe se ele é positivo, negativo ou igual a zero.
numero = 10
if numero > 0:
    print("o número é positivo")
elif numero < 0:
    print("o número é negativo")
else:
    print("o número é zero")

# == ta comparando duas variaveis

# Exercício 12 — Par ou ímpar
# Leia um número inteiro e informe se ele é par ou ímpar.
# Dica: use o operador de resto da divisão (%).
numero = 10
resto = numero % 2
if resto == 0:
    print("o número é par")
else:
    print("o número é ímpar")

# % é resto

# Exercício 13 — Aprovação
# Leia a média de um aluno. Mostre "Aprovado" se a média for maior ou igual
# a 7 e "Reprovado" caso contrário.
nota1 = float(input("digite sua nota"))
nota2 = float(input("digite sua nota"))
nota3 = float(input("digite sua nota"))
media = (nota1 + nota2 + nota3) / 3   # atenção: os parênteses precisam envolver as 3 notas
print(media)
if media >= 7:
    print("aprovado")
else:
    print("reprovado")

# Exercício 14 — Aprovação com recuperação
# Leia a média de um aluno e mostre:
# - "Aprovado", se a média for maior ou igual a 7;
# - "Recuperação", se a média estiver entre 5 e 6.9;
# - "Reprovado", se a média for menor que 5.
media = float(input("digite a média do aluno"))
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# Exercício 15 — Maior entre dois números
# Leia dois números e mostre qual é o maior. Se forem iguais, informe isso.
n1 = int(input("digite seu numero"))
n2 = int(input("digite outro numero"))
if n1 > n2:
    print(f"o maior número é {n1}")
elif n2 > n1:
    print(f"o maior número é {n2}")
else:
    print("os números são iguais")

# Exercício 16 — Faixa etária
# Leia a idade de uma pessoa e classifique-a como:
# - "Criança": até 11 anos;
# - "Adolescente": de 12 a 17 anos;
# - "Adulto": de 18 a 59 anos;
# - "Idoso": 60 anos ou mais.
idade = int(input("digite a idade"))
if idade <= 11:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")

# Exercício 17 — Desconto na compra
# Leia o valor de uma compra. Se o valor for maior que R$ 100,00, aplique
# desconto de 10%. Caso contrário, mantenha o valor original. Mostre o total.
valor_compra = float(input("digite o valor da compra"))
if valor_compra > 100:
    total_compra = valor_compra * 0.9
else:
    total_compra = valor_compra
print(total_compra)

# Exercício 18 — Acesso ao sistema
# Leia o nome de usuário e a senha. Mostre "Acesso permitido" somente quando
# o usuário for "admin" e a senha for "1234". Caso contrário, mostre
# "Acesso negado".
usuario = input("digite o nome de usuário")
senha = input("digite a senha")
if usuario == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")

# Exercício 19 — Número dentro do intervalo
# Leia um número e informe se ele está entre 10 e 50, incluindo os limites.
# Use os operadores and, >= e <=.
numero = int(input("digite um número"))
if numero >= 10 and numero <= 50:
    print("o número está entre 10 e 50")
else:
    print("o número não está entre 10 e 50")

# Exercício 20 — Calculadora simples
# Leia dois números e uma operação (+, -, * ou /). Use if/elif/else para
# realizar a operação escolhida e mostrar o resultado. Não permita divisão
# por zero.
n1 = float(input("digite o primeiro número"))
n2 = float(input("digite o segundo número"))
operacao = input("digite a operação (+, -, * ou /)")
if operacao == "+":
    print(n1 + n2)
elif operacao == "-":
    print(n1 - n2)
elif operacao == "*":
    print(n1 * n2)
elif operacao == "/":
    if n2 != 0:
        print(n1 / n2)
    else:
        print("Não é possível dividir por zero")
else:
    print("Operação inválida")

# ============================================================================
# 3. LISTAS — EXERCÍCIOS 21 A 30
# ============================================================================

# Exercício 21 — Criando uma lista
# Crie uma lista com as frutas "maçã", "banana", "laranja" e "uva".
# Mostre a lista completa.
frutas = ["maçã", "banana", "laranja", "uva"]
print(frutas)

# Exercício 22 — Acessando elementos
# Usando a lista abaixo, mostre o primeiro e o último elemento.
# cores = ["azul", "verde", "amarelo", "vermelho"]
cores = ["azul", "verde", "amarelo", "vermelho"]
print(cores[0])

print(cores[-1])

# Exercício 23 — Adicionando elementos
# Crie uma lista com três nomes. Peça outro nome ao usuário, adicione-o ao
# final da lista com append() e mostre a lista atualizada.
nomes = ["Ana", "Bruno", "Carla"]
novo_nome = input("digite outro nome")
nomes.append(novo_nome)
print(nomes)

# Exercício 24 — Removendo elementos
# Dada a lista abaixo, remova "banana" com remove() e mostre o resultado.
# frutas = ["maçã", "banana", "laranja", "uva"]
frutas = ["maçã", "banana", "laranja", "uva"]
frutas.remove("banana")
print(frutas)

# Exercício 25 — Alterando um elemento
# Dada a lista abaixo, substitua "laranja" por "abacaxi" usando seu índice.
# frutas = ["maçã", "banana", "laranja", "uva"]
frutas = ["maçã", "banana", "laranja", "uva"]
frutas[2] = "abacaxi"
print(frutas)

# Exercício 26 — Tamanho e presença
# Dada a lista abaixo, mostre a quantidade de elementos e verifique se
# o número 30 pertence à lista.
# numeros = [10, 20, 30, 40, 50]
numeros = [10, 20, 30, 40, 50]
print(len(numeros))
print(30 in numeros)

# Exercício 27 — Soma, maior e menor
# Dada a lista abaixo, mostre a soma, o maior valor e o menor valor usando
# sum(), max() e min().
# valores = [12, 5, 28, 9, 17]
valores = [12, 5, 28, 9, 17]
print(sum(valores))
print(max(valores))
print(min(valores))

# Exercício 28 — Ordenação
# Coloque a lista abaixo em ordem alfabética usando sort() e mostre o resultado.
# cidades = ["Curitiba", "Salvador", "Recife", "Goiânia", "Manaus"]
cidades = ["Curitiba", "Salvador", "Recife", "Goiânia", "Manaus"]
cidades.sort()
print(cidades)

# Exercício 29 — Concatenação
# Una as duas listas abaixo em uma terceira lista e mostre o resultado.
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)

# Exercício 30 — Fatiamento
# Dada a lista abaixo, use fatiamento para mostrar:
# a) os três primeiros números;
# b) os três últimos números;
# c) os números do índice 2 ao índice 5.
# numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeros[:3])
print(numeros[-3:])
print(numeros[2:6])

# ============================================================================
# 4. ESTRUTURAS DE REPETIÇÃO — EXERCÍCIOS 31 A 40
# ============================================================================

# Exercício 31 — Números de 1 a 10
# Use um laço for e range() para mostrar os números de 1 a 10.
for n in range(1, 11):
    print(n)

# Exercício 32 — Números pares
# Use um laço for para mostrar apenas os números pares de 2 a 20.
for n in range(2, 21, 2):
    print(n)

# Exercício 33 — Percorrendo nomes
# Use um laço for para mostrar cada nome da lista abaixo em uma linha.
# nomes = ["Ana", "Bruno", "Carla", "Diego"]
nomes = ["Ana", "Bruno", "Carla", "Diego"]
for nome in nomes:
    print(nome)

# Exercício 34 — Quadrados
# Use um laço for para criar uma nova lista contendo o quadrado de cada número.
# numeros = [1, 2, 3, 4, 5]
numeros = [1, 2, 3, 4, 5]
quadrados = []
for n in numeros:
    quadrados.append(n ** 2)
print(quadrados)

# Exercício 35 — Soma com for
# Use um laço for e uma variável acumuladora para somar os valores abaixo.
# Não use a função sum().
# valores = [10, 20, 30, 40, 50]
valores = [10, 20, 30, 40, 50]
soma = 0
for v in valores:
    soma += v
print(soma)

# Exercício 36 — Contando aprovados
# Percorra a lista e conte quantas notas são maiores ou iguais a 7.
# notas = [8.0, 5.5, 7.0, 9.2, 4.0, 6.8]
notas = [8.0, 5.5, 7.0, 9.2, 4.0, 6.8]
contador = 0
for nota in notas:
    if nota >= 7:
        contador += 1
print(contador)

# Exercício 37 — Contagem com while
# Use um laço while para mostrar os números de 1 a 10.
i = 1
while i <= 10:
    print(i)
    i += 1

# Exercício 38 — Contagem regressiva
# Use um laço while para fazer uma contagem regressiva de 10 até 1.
# Ao terminar, mostre a mensagem "Fim!".
i = 10
while i >= 1:
    print(i)
    i -= 1
print("Fim!")

# Exercício 39 — Senha correta
# Peça uma senha ao usuário repetidamente usando while. O programa deve parar
# somente quando a senha digitada for "python123".
senha = ""
while senha != "python123":
    senha = input("digite a senha")
print("senha correta!")

# Exercício 40 — Somando até zero
# Peça números inteiros ao usuário e some os valores digitados. Use while para
# continuar a leitura até que o usuário digite 0. Ao final, mostre a soma.
soma = 0
while True:
    numero = int(input("digite um número (0 para parar)"))
    if numero == 0:
        break
    soma += numero
print(soma)

# ============================================================================
# 5. DICIONÁRIOS — EXERCÍCIOS 41 A 50
# ============================================================================

# Exercício 41 — Criando um dicionário
# Crie um dicionário chamado aluno com as chaves "nome", "idade" e "curso".
# Preencha com valores fictícios e mostre o dicionário completo.
aluno = {"nome": "Camila",
         "idade": 19,
         "curso": "economia"}
print(aluno)

# Exercício 42 — Acessando valores
# Dado o dicionário abaixo, mostre separadamente o nome e o preço do produto.
# produto = {"nome": "Teclado", "preco": 150.0, "estoque": 8}
produto = {"nome": "Teclado",
           "preco": 150.0,
           "estoque": 8}
print(produto["nome"])
print(produto["preco"])

# Exercício 43 — Adicionando uma chave
# Adicione a chave "marca" ao dicionário abaixo e mostre o resultado.
# produto = {"nome": "Mouse", "preco": 80.0}
produto = {"nome": "Mouse", "preco": 80.0}
produto["marca"] = "Logitech"
print(produto)

# Exercício 44 — Atualizando um valor
# Altere o estoque do produto abaixo para 15 unidades e mostre o dicionário.
# produto = {"nome": "Monitor", "preco": 900.0, "estoque": 5}
produto = {"nome": "Monitor", "preco": 900.0, "estoque": 5}
produto["estoque"] = 15
print(produto)

# Exercício 45 — Removendo uma chave
# Remova a chave "cor" do dicionário abaixo usando pop() e mostre o resultado.
# carro = {"marca": "Ford", "modelo": "Ka", "ano": 2020, "cor": "prata"}
carro = {"marca": "Ford", "modelo": "Ka", "ano": 2020, "cor": "prata"}
carro.pop("cor")
print(carro)

# Exercício 46 — Verificando uma chave
# Verifique se a chave "telefone" existe no dicionário abaixo. Mostre uma
# mensagem informando o resultado.
# contato = {"nome": "Marina", "email": "marina@email.com"}
contato = {"nome": "Marina", "email": "marina@email.com"}
if "telefone" in contato:
    print("a chave 'telefone' existe no dicionário")
else:
    print("a chave 'telefone' não existe no dicionário")

# Exercício 47 — Chaves e valores
# Use keys() para mostrar todas as chaves e values() para mostrar todos os
# valores do dicionário abaixo.
# capitais = {"Brasil": "Brasília", "Argentina": "Buenos Aires", "Chile": "Santiago"}
capitais = {"Brasil": "Brasília", "Argentina": "Buenos Aires", "Chile": "Santiago"}
print(capitais.keys())
print(capitais.values())

# Exercício 48 — Percorrendo um dicionário
# Use um laço for e items() para mostrar o nome de cada produto e seu preço.
# produtos = {"caderno": 25.0, "caneta": 4.5, "mochila": 120.0}
produtos = {"caderno": 25.0, "caneta": 4.5, "mochila": 120.0}
for nome, preco in produtos.items():
    print(nome, preco)

# Exercício 49 — Soma dos valores
# Calcule a soma de todas as quantidades do dicionário abaixo e mostre o total.
# estoque = {"notebook": 5, "mouse": 20, "teclado": 12, "monitor": 4}
estoque = {"notebook": 5, "mouse": 20, "teclado": 12, "monitor": 4}
total = 0
for quantidade in estoque.values():
    total += quantidade
print(total)

#ou 
estoque = {"notebook": 5, "mouse": 20, "teclado": 12, "monitor": 4}
sum(estoque.values())

# Exercício 50 — Frequência de palavras
# Percorra a lista abaixo e crie um dicionário que conte quantas vezes cada
# palavra aparece. Ao final, mostre o dicionário de frequências.
# palavras = ["python", "dados", "python", "lista", "dados", "python"]
palavras = ["python", "dados", "python", "lista", "dados", "python"]
frequencia = {}
for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1
print(frequencia)


