#1 - Escreva um programa que peça ao usuário para digitar um número. Trate o erro caso ele digite algo que não seja um número inteiro.
#try:
#     idade = int(input("Digite um número: "))
# except ValueError:
#     print("Só informar número inteiro")

# 2 - Peça ao usuário dois números e tente multiplicá-los. Se o usuário digitar algo inválido, exiba uma mensagem de erro.
# try:
#     num1 = int(input("Informe o primeiro numero: "))
#     num2 = int(input("Informe o segundo numero: "))
#     mult = num1*num2
#     print(f"O resultado da multiplicação é: {mult}")
# except:
#     print("Só informar numeros")

# 3 - Crie um programa que peça ao usuário um número inteiro. Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.
# try:
#     numero = int(input("Digite um número inteiro: "))
# except ValueError:
#     print("Erro: esse não é um número inteiro. Tente novamente.")
# else:
#     print(f"Parabéns! Você digitou o número inteiro {numero}.")
         
# 4 - Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir). Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.
# try:
#     arquivo = open('dados.txt')
#     print("Arquivo aberto com sucesso!")
# except FileNotFoundError:
#     print("O arquivo 'dados.txt' não foi encontrado.")
# finally:
#     print("Encerrando programa.")

# 5 - Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError se b for igual a zero. Caso contrário, retorne o resultado da divisão.
# def dividir(a, b):
#     if b == 0:
#         raise ZeroDivisionError("Não é possível dividir por zero!")
#     return a / b

# try:
#         a = int(input("Digite o primeiro número: "))
#         b = int(input("Digite o segundo número: "))
#         resultado = dividir(a, b)
# except ValueError:
#         print("Erro: o número não é válido")
# except ZeroDivisionError as e:
#         print(e)
# else:
#         print(f"O resultado da divisão é: {resultado}")

# 6 - Crie uma exceção personalizada chamada IdadeInvalidaError. Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa.
# IdadeInvalidaError = type("IdadeInvalidaError", (Exception,), {})

# def cadastrar_idade(idade):
#     if idade < 0:
#         raise IdadeInvalidaError(f"Idade inválida: {idade}. A idade não pode ser negativa.")
#     print(f"Idade {idade} cadastrada com sucesso!")

# 7 - Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro:

# ValueError se o usuário digitar algo inválido

# ZeroDivisionError se tentar dividir por zero

# try:
#     a = float(input("Digite o primeiro número: "))
#     b = float(input("Digite o segundo número: "))
#     resultado = a / b
# except ValueError:
#     print("Digite apenas números")
# except ZeroDivisionError:
#     print("Erro: não é possível dividir por zero.")
# else:
#     print(f"O resultado da divisão é: {resultado}")

# 8 - Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use:

# try para a conversão,

# else para verificar se é par ou ímpar,
# finally para exibir "Fim do programa".

# try:
#     numero = int(input("Digite um número inteiro: "))
# except ValueError:
#     print(" Valor inválido, digite um número inteiro.")
# else:
#     if numero % 2 == 0:
#         print(f"O número {numero} é par.")
#     else:
#         print(f"O número {numero} é ímpar.")
# finally:
#     print("Fim do programa.")

# 9 - Crie uma função sacar(saldo, valor) que:

# Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo.

# Caso contrário, retorne o novo saldo. Teste a função dentro de um try-except e exiba uma mensagem apropriada ao usuário.

class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError(f"Saldo insuficiente! Saldo disponível: {saldo}, valor solicitado: {valor}.")
    return saldo - valor
try:
    saldo_inicial = 10
    valor_saque = float(input("Digite o valor do saque: "))
    novo_saldo = sacar(saldo_inicial, valor_saque)
except SaldoInsuficienteError as e:
    print("Operação não realizada:", e)
else:
    print(f"Saque realizado com sucesso! Novo saldo: {novo_saldo}")