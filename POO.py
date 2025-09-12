# 1 - Crie uma classe chamada Pessoa que tenha os atributos nome e idade. Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

# p1 = Pessoa("Maria", 25)
# p2 = Pessoa("João", 30)

# print("Nome:", p1.nome, "- Idade:", p1.idade)
# print("Nome:", p2.nome, "- Idade:", p2.idade)

# 2 - Expanda a classe Pessoa para incluir um método apresentar() que imprima uma frase como:"Olá, meu nome é João e tenho 25 anos.". Teste o método chamando-o a partir de um objeto.
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def apresentar(self):
#         print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# p1 = Pessoa("João", 25)
# p1.apresentar()

# 3 - Crie uma classe Carro com os atributos marca, modelo e ano. Use o método __init__ para inicializar esses valores. Crie três objetos e mostre suas informações

# class Carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano

#     def informacoes(self):
#         print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")
    
# carro01 = Carro("Chevrolet", "Onix", 2025)
# carro02 = Carro("Fiat", "Uno", 2022)
# carro03 = Carro("Renault", "Logan", 2024)

# carro01.informacoes()
# carro02.informacoes()
# carro03.informacoes()

# #4 - Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos (por exemplo, mudar o ano). Imprima antes e depois da alteração.
# class Carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano

# carro = Carro("Toyota", "Corolla", 2020)

# print("Antes da alteração:")
# print(f"Marca: {carro.marca}, Modelo: {carro.modelo}, Ano: {carro.ano}")

# carro.ano = 2022

# print("Depois da alteração:")
# print(f"Marca: {carro.marca}, Modelo: {carro.modelo}, Ano: {carro.ano}")


# 5 - Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione um método depositar(valor) que aumenta o saldo e um método sacar(valor) que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques.
# class ContaBancaria:
  
#     def __init__(self, titular, saldo=0):
#         self.titular = titular
#         self.saldo = saldo
#         self.operacoes = []

#     def __str__(self):
#         return f"Conta do titular {self.titular} tem {self.saldo} de saldo"
    
#     def deposito(self, valor):
#         self.saldo += valor
#         self.operacoes.append(["Deposito", valor])
#         print(f"Foi depositado {valor} reais na sua conta")
    
#     def saque(self, valor):
#           if valor <= self.saldo:
#             self.saldo -= valor
#             print(f"Foi sacado {valor} reais da sua conta")
#           else:
#             print("Saldo insuficiente para o saque.")
#             self.operacoes.append(["Saque", valor])
        
#     def extrato(self):
#         for operacao in self.operacoes:
#             print(operacao)
#         print(f"Saldo: {self.saldo}")

# conta1 = ContaBancaria("Mário",15)
# conta2 = ContaBancaria("Bianca", 300)

# print(conta1)
# print(conta2)

# conta1.deposito(250)
# conta1.saque(120)
# conta2.saque(400)
# conta1.extrato()

# 6 - Modifique a classe ContaBancaria para que o método sacar retorne True se a operação for bem-sucedida e False caso contrário. Teste o retorno e imprima mensagens adequadas.
# class ContaBancaria:
  
#     def __init__(self, titular, saldo=0):
#         self.titular = titular
#         self.saldo = saldo
#         self.operacoes = []

#     def __str__(self):
#         return f"Conta do titular {self.titular} tem {self.saldo} de saldo"
    
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

# conta1 = ContaBancaria("Mário", 200)
# conta1.saque(100)
# conta1.saque(250)
# conta1.extrato()

# 7 - Crie uma classe Aluno com atributos nome e nota. Depois crie uma classe Turma que tenha uma lista de alunos e um método adicionar_aluno(aluno). Crie alguns objetos Aluno e adicione-os à turma.
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def __str__(self):
        return f"{self.nome} - Nota: {self.nota}"
class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        print(f"Aluno {aluno.nome} adicionado à turma.")

    def listar_alunos(self):
        print("Lista de alunos da turma:")
        for aluno in self.alunos:
            print(aluno)

aluno1 = Aluno("Ana", 9.0)
aluno2 = Aluno("Carol", 7.5)
aluno3 = Aluno("Beatriz", 8.3)

turma = Turma()
turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)
turma.adicionar_aluno(aluno3)

turma.listar_alunos()

# 8 - Na classe Aluno, implemente o método __str__ para que, ao imprimir um objeto da classe, apareça algo como:"Aluno: Maria - Nota: 9.5". Teste imprimindo os objetos.
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return f"Aluno: {self.nome} - Nota: {self.nota}"


aluno1 = Aluno("Maria", 9.5)
aluno2 = Aluno("Márcia", 8.0)
aluno3 = Aluno("Ana", 7.3)

print(aluno1)
print(aluno2)
print(aluno3)

# 9 - Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" e atributos de instância nome e idade. Mostre a diferença entre acessar especie pelo objeto e pela classe.
class Cachorro:
    especie = "Canis familiaris"  

    def __init__(self, nome, idade):
        self.nome = nome         
        self.idade = idade        

cachorro1 = Cachorro("Mel", 9)
cachorro2 = Cachorro("Nega", 12)

print(Cachorro.especie)

print(cachorro1.especie)

print(f"{cachorro1.nome} tem {cachorro1.idade} anos.")
print(f"{cachorro2.nome} tem {cachorro2.idade} anos.")