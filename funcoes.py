#1 - Crie uma função chamada saudacao que imprime na tela a mensagem "Olá, bem-vindo ao Python!". Em seguida, chame a função no programa.
# def saudacao():
#     print("Olá, bem-vindo ao Python!")
# saudacao()

#2 - Crie uma função chamada dobro que recebe um número como parâmetro e retorna o dobro desse número. Teste chamando a função com diferentes valores.
# def dobro(num):
#     return num*2
# num = int(input("Digite um número: "))
# print(f"O dobro do número é: {dobro(num)}")
      
#3 - Crie uma função chamada soma que receba dois números e retorne a soma deles. Depois, use a função para somar 10 + 20.
# def soma(num1, num2):
#     return num1+num2

# operacao = soma(10,20)
# print(operacao)

# 4 - Crie uma função chamada mensagem que receba um nome como parâmetro e exiba a mensagem:

# "Olá, [nome]!"

# Caso o nome não seja informado, mostre "Olá, visitante!".
# def mensagem():
#     nome = input("Digite seu nome: ")
#     if nome == "":
#         print("Olá, visitante!")
#     else:
#         print(f"Olá, {nome}!")

# mensagem()

# #5 - Crie uma função chamada operacoes que receba dois números e retorne a soma, a subtração e a multiplicação deles.
# def operacoes():
#     a = int(input("Digite o primeiro número: "))
#     b = int(input("Digite o segundo número: "))
    
#     return a + b, a - b, a * b

# soma, subtracao, multiplicacao = operacoes()

# print("Soma:", soma)
# print("Subtração:", subtracao)
# print("Multiplicação:", multiplicacao)

#6 - Crie uma função chamada media que receba uma quantidade variável de números e retorne a média deles. Teste com 3, 5 e 7 valores diferentes.

# def media(*numeros):
#     print(numeros)
#     return sum(numeros)/len(numeros)

# print(media(3,4,5))
# print(media(3,2,6,8,5))
# print(media(7,3,8,3,4,5,9))

# 7 - Crie uma função chamada dados_pessoais que receba informações de uma pessoa (nome, idade, cidade, etc.) usando **kwargs e imprima cada dado em uma linha. Exemplo de chamada:
# dados_pessoais(nome="Ana", idade=25, cidade="Recife")
# def dados_pessoais(**kwargs):
#     print(kwargs)
#     for chave, valor in kwargs.items():
#         print(f"{chave.capitalize()}: {valor}")

# dados_pessoais(nome="Ana", idade=25, cidade="Recife")

# #8 - Crie uma função chamada calculadora que tenha dentro dela outras funções (somar, subtrair, multiplicar, dividir). A função principal deve permitir escolher a operação e retornar o resultado.
# def calculadora():
  
#     def somar(a, b):
#         return a + b

#     def subtrair(a, b):
#         return a - b

#     def multiplicar(a, b):
#         return a * b

#     def dividir(a, b):
#         if b != 0:
#             return a / b
#         else:
#             return "Não é possível dividir por zero"
    
#     def operacao(a, b, operador):
#         if operador == "soma":
#             return somar(a, b)
#         elif operador == "subtração":
#             return subtrair(a, b)
#         elif operador == "multiplicação":
#             return multiplicar(a, b)
#         elif operador == "divisão":
#             return dividir(a, b)
#         else:
#             return "Operação inválida"

#     return operacao

#9 - Crie uma função chamada aplicar_operacao que receba dois números e uma função como parâmetros. A função deve aplicar a operação recebida (ex: soma, multiplicação)
def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

def aplicar_operacao(a, b, operacao):
    return operacao(a, b)
