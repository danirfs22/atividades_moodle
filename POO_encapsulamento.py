# 1 - Na classe, ContaBancaria, converta saldo para uma atributo privado. Crie um método setter e um getter para acessar e modificar essa atributo, seguindo uma regra lógica (Ex: saldo não pode ser negativo)
# class ContaBancaria:
  
#     def __init__(self, titular, saldo=0): 
#         self.titular = titular
#         self.__saldo = saldo
#         self.operacoes = []

#     def __str__(self):
#         return f"Conta do titular {self.titular} tem {self.__saldo} de saldo"
    
#     def get_saldo(self):
#         return self.__saldo
    
#     def set_saldo(self, valor):
#         if valor < 0:
#             print("Saldo não pode ser negativo")
#         else:
#             self.__saldo = valor

#     def deposito(self, valor):
#         self.saldo += valor
#         self.operacoes.append(("Depósito", valor))
#         print(f"Foi depositado {valor} reais na sua conta")
    
#     def saque(self, valor):
#         if valor <= self.saldo:
#             self.saldo -= valor
#             self.operacoes.append(("Saque", valor))
#             return True
#         else:
#             self.operacoes.append(("Saque negado", valor))
#             return False
    
#     def extrato(self):
#         for operacao, valor in self.operacoes:
#             print(f"{operacao}: {valor} reais")
#         print(f"Saldo atual: {self.saldo}")

  
# 2 - Crie uma classe, Pessoa, que tenha os atributos: nome, data de nascimento, cpf, identidade. Deixe os atributos cpf e identidade como privado e monte os métodos setters e getters para acessar e editar os valores
class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__identidade = identidade

    def __str__(self):
        return f"Nome = {self.nome}, Data de Nascimento = {self.data_nascimento}, CPF = {self.__cpf}, Identidade = {self.__identidade}"

def get_cpf(self):
        return self.__cpf

def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

def get_identidade(self):
        return self.__identidade

def set_identidade(self, nova_identidade):
        self.__identidade = nova_identidade

p1 = Pessoa("João", "10/05/1990", "123.456.789-00", "1.234.567")
print(p1)