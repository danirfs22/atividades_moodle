# 1 - Crie uma classe Usuario com atributos nome e email. Depois, crie uma classe Cliente que herde de Usuario. Crie uma instancia de um cliente e acesse todos os atributos.

# class Usuario:
#     def __init__(self, nome, email):
#         self.nome = nome
#         self.email = email

# class Cliente(Usuario): 
#     def __init__(self, nome, email):
#         super().__init__(nome, email)  

#     def __str__(self):
#         return f"Cliente: {self.nome}, possui e-mail: {self.email}"

# cliente1 = Cliente("Maria", "maria@gmail.com")
# print(cliente1)
        
# # 2 - Implemente um método exibir_informacoes() na classe Usuario e herde esse método em Cliente. Mostre como chamar o método herdado a partir de um objeto Cliente.
# class Usuario:
#     def __init__(self, nome, email):
#         self.nome = nome
#         self.email = email

#     def exibir_informacoes(self):
#         return f"Nome: {self.nome}, Email: {self.email}"
    
# class Cliente(Usuario): 
#     def __init__(self, nome, email):
#         super().__init__(nome, email) 

# cliente1 = Cliente("Maria", "maria@gmail.com")
# print(cliente1.exibir_informacoes())

# 3 - Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário". Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente". Mostre como funciona a chamada.
class Usuario:
    def __init__(self, usuario):
        self.usuario = usuario

    def saudacao(self):
        return "Olá, usuário"

class Cliente(Usuario): 
    def __init__(self, usuario):
        super().__init__(usuario) 
    
    def saudacao(self):
        return "Olá, cliente"

class User(Cliente):
    pass

user = User("Joana") 
print(user.saudacao())  

# 4 - Na classe Cliente, adicione o atributo saldo. Adicione um método construtor em Cliente que inicialize também os atributos de Usuario usando super().
# class Usuario:
#     def __init__(self, nome, email):
#         self.nome = nome
#         self.email = email
 
# class Cliente(Usuario):
#     def __init__(self, nome, email, saldo):
#         super().__init__(nome, email)
#         self.saldo = saldo

#     def __str__(self):      
#         return f"Cliente: {self.nome}, e-mail: {self.email}, possui saldo: R$ {self.saldo}"

# cliente1 = Cliente("Ana Maria", "anamaria@gmail.com", 1500.75)
# print(cliente1)

# 5 - Crie uma classe Funcionario que herda de Usuario e, em seguida, crie uma classe Gerente que herda de Funcionario. Mostre como instanciar um gerente e acessar seus atributos.
# class Usuario:
#     def __init__(self, nome, email):
#         self.nome = nome
#         self.email = email

# class Funcionario(Usuario):
#     def __init__(self, nome, email, setor):
#         super().__init__(nome, email)  
#         self.setor = setor
        
# class Gerente(Funcionario):
#     def __init__(self, nome, email, setor):
#         super().__init__(nome, email, setor)
       
#     def __str__ (self):
#         return f"Nome: {self.nome}, e-mail: {self.email}, Setor: {self.setor}"

# gerente1 = Gerente("Carlos Souza", "carlos@empresa.com", "Vendas")
# print(gerente1)

# # 6 - Crie uma classe Autenticacao com um método login(). Crie outra classe Permissao com um método verificar_permissao(). Em seguida, crie uma classe Administrador que herda de ambas. Como usar os métodos herdados?
# class Autenticacao:
#     def __init__(self, usuario, senha):
#         self.usuario = usuario
#         self.senha = senha

#     def login(self):
#         return f"Login de {self.usuario} realizado."

# class Permissao:
#     def __init__(self, permissao):
#         self.permissao = permissao

#     def verificar_permissao(self):
#         return f"Permissão: {self.permissao}"

# class Administrador(Autenticacao, Permissao):
#     def __init__(self, usuario, senha, permissao):
#         Autenticacao.__init__(self, usuario, senha)
#         Permissao.__init__(self, permissao)

#     def __str__(self):
#         return f"Usuário: {self.usuario}, Senha: {self.senha}, {self.verificar_permissao()}"

# adm = Administrador("Danielle", "123", "total")
# print(adm)

# 7 - Usando o exemplo anterior, adicione um método status() em Autenticacao e também em Permissao. Se a classe Administrador herda das duas, qual versão de status() será chamada? Use Administrador.__mro__ para mostrar a ordem.
# class Autenticacao:
#     def __init__(self, usuario, senha):
#         self.usuario = usuario
#         self.senha = senha

#     def status(self):
#         return "Status vindo de Autenticacao"

# class Permissao(Autenticacao):
#     def __init__(self, usuario, senha, permissao):
#         super().__init__(usuario, senha) 
#         self.permissao = permissao

#     def status(self):
#         return "Status vindo de Permissao"

# class Administrador(Permissao):
#         pass

# adm = Administrador("Danielle", "123", "total")
# print(adm.status())  
# print(Administrador.__mro__)