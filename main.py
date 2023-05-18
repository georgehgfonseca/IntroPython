#################################################################################
# 1. Instalação do Python
# Sugiro usar o VS Code com a extensão Python: 
# https://code.visualstudio.com/docs/languages/python
# Para executar o programa, digite no terminal: python main.py
# ou clique no botão Run na parte superior direita do VS Code
print("Hello World!")

#################################################################################
# 2. Sintaxe básica
# Blocos de código são definidos por identação ({} ; não são usados)
altura = float(input("Informe a altura: "))
if altura >= 1.9:
    print("Alto")
elif altura >= 1.7 and altura < 1.9:
    print("Médio")
else:
    print("Baixo")
    if altura < 1.4:
        print("Anão ou criança")

#################################################################################
# 3. Exercício classificação de triângulos:
l1 = float(input("Informe o lado 1: "))
l2 = float(input("Informe o lado 2: "))
l3 = float(input("Informe o lado 3: "))

if l1 <= 0 or l2 <= 0 or l3 <= 0:
    print("O lado não pode ser 0 ou negativo")
elif l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
    print("Um lado não pode ser maior que a soma dos outros dois")
else:
    # O triângulo é valido, definir o tipo
    if l1 == l2 and l2 == l3:
        print("Triângulo equilátero")
    elif l1 != l2 and l2 != l3 and l1 != l3:
        print("Triângulo escaleno")
    else:
        print("Triângulo isósceles")

#################################################################################
# 4. Listas e operador slice
# Listas são coleções de dados, que podem ser de tipos diferentes
# O operador slice é usado para acessar partes da lista
frutas = ["Uva", "Maçã", "Banana", "Pera"]
print(frutas[1])
print(frutas[1:3]) # Do elemento 1 até o 3 (não inclui o 3)
print(frutas[1:])  # Do elemento 1 até o final
print(frutas[-1])  # Penúltima posição

#################################################################################
# 5. Operações em listas
# Adicionar elementos
frutas.append("Morango") # Adiciona no final
frutas.insert(1, "Kiwi") # Adiciona na posição 1 (desloca os demais elementos) 

# Remover elementos
frutas.remove("Banana") # Remove o primeiro elemento com o valor informado
frutas.pop(3)           # Remove o elemento da posição 3 (Pera)

print(frutas)

#################################################################################
# 6. Laços de repetição
# Laço for pode ser usado por índice ou por elemento:
for i in range(len(frutas)):
    print(frutas[i])

for fruta in frutas:
    print(fruta)

# A função range cria uma lista de números inteiros e pode receber 3 parâmetros:
# range(inicio, fim, passo)
# inicio = 0 (padrao) e passo = 1 (padrao)
for i in range(2, 10, 2):
    print(i) # 2, 4, 6, 8

# Laço while é usado quando não se sabe quantas vezes o laço será executado
# Comandos break e continue podem ser usados para controlar o laço
while True:
    print("Loop infinito")
    break # Para o laço

#################################################################################
# 7. Listas multidimensionais (matrizes, etc)
nomes = ["George", "João", "Alice"]
# Cada string na lista de nomes é uma lista de caracteres
print(nomes[0][1]) # Primeiro nome (George), segundo caractere (e)

notas = [[5, 7, 9], [4, 6, 9], [10, 8, 7]]
# Para percorrer uma lista multidimensional, é necessário usar dois laço for
for i in range(len(notas)):
    for j in range(len(notas[i])):
        print(notas[i][j])

#################################################################################
# 8. Exercício: Matriz de notas
# Percorra a matriz de notas e informe quantas notas ao todo foram maiores que 6
cont_maior_que_6 = 0
for i in range(len(notas)):
    for j in range(len(notas[i])):
        if notas[i][j] > 6.0:
            cont_maior_que_6 += 1 # Note que Python não tem operador ++ 
print("Notas maiores que 6.0: ", cont_maior_que_6)

#################################################################################
# 9. Operadores ** // in
a = 5 ** 2 # 5 elevado a 2
print(a)   # 25
a = 5 // 2 # Divisão inteira
print(a)

# Operador in recebe um valor e uma lista e verifica se o valor está na lista
carros = ["Vectra", "Fusca", "Gol", "Uno"]
print("Fusca" in carros) # True

#################################################################################
# 10. Funções
def encontra_min(elementos):
    min = elementos[0] # ou float("inf") para inicializar com infinito
    for elemento in elementos:
        if elemento < min:
            min = elemento
    return min

print(encontra_min([5, 3, 7, 1, 9])) # 1

#################################################################################
# 11. Exercício soma elementos
def soma_elementos(elementos):
    soma = 0
    for elemento in elementos:
        soma += elemento
    return soma

print(soma_elementos([5, 3, 7, 1, 9])) # 25

#################################################################################
# 12. Retorno múltiplo
# Python permite o retorno de múltiplos valores em uma função:
def encontra_min_max(elementos):
    min = elementos[0] # ou float("inf") para inicializar com infinito
    max = elementos[0] # ou float("-inf") para inicializar com -infinito
    for elemento in elementos:
        if elemento < min:
            min = elemento
        if elemento > max:
            max = elemento
    return (min, max)

elems = [5, 3, 7, 1, 9]
print(encontra_min_max(elems)) # (1, 9)

# Podemos salvar os valores retornados em variáveis separadas:
(min, max) = encontra_min_max(elems)
# Vamos explorar outras formas de imprimir os valores:
print("(%d, %d)" % (min, max)) # (1, 9)
print(f"({min}, {max})")       # (1, 9)

#################################################################################
# 13. Separação em módulos
# Vamos replicar as funções encontra_min_max e soma_elementos em um arquivo separado
# operacoes.py
# Para usar as funções, precisamos importar o módulo:
from operacoes import encontra_min_max, soma_elementos

# Agora podemos usar as funções normalmente:
print(encontra_min_max(elems)) # (1, 9)
print(soma_elementos(elems))   # 25

#################################################################################
# 14. Módulos nativos e instalação de pacotes
# Python possui uma biblioteca padrão com diversos módulos úteis
import math

print(math.sqrt(9)) # 3.0

# Para instalar pacotes de terceiros, podemos usar o pip:
# no terminal, digite: pip install numpy

# Há diversos pacotes úteis com funcionalidades prontas, alguns exemplos:
# numpy, pandas para processamento numérico e análise de dados
# matplotlib, seaborn para visualização de dados
# scikit-learn, tensorflow para machine learning
# pygame, pyglet para jogos
# flask, django para desenvolvimento web
# e muitos outros...

# Esses pacotes e a crescente comunidade que contribui com open source
# tornam o Python uma grande opção para vários projetos, em especial 
# de IA e ciência dos dados

#################################################################################
# 15. Orientação a objetos (básica)
from aluno import Aluno
a1 = Aluno("Bia", 19, 9.2, 0.8)
a2 = Aluno("Caio", 22, 4.5, 0.75)
print(a1.nome, a1.idade)
print(a2.nome, a2.idade)

# Para alterar um atributo:
a2.nota = 10.0
print(a2.nota)

# Acessar métodos da classe:
print(a2.aprovado()) # True

# Python também suporta herança e polimosfismo 
# (mas deixarei de fora desse breve tutorial)

#################################################################################