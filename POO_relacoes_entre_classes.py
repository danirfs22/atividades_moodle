1 - Crie as classes Pessoa e Livro e demonstre uma relação de associação entre eles.
class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.livro = None  

    def pegar_livro(self, livro):
        self.livro = livro
        print(f"{self.nome} está lendo '{self.livro.titulo}'.")

livro1 = Livro("Dom Casmurro")
pessoa1 = Pessoa("João")
pessoa1.pegar_livro(livro1)

2 - Crie as classes Aluno e Onibus. Crie um método em Aluno que use a classe Onibus.
class Onibus:
    def embarcar(self, aluno_nome):
        print(f"{aluno_nome} embarcou no ônibus")

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def ir_para_curso(self, onibus):
        onibus.embarcar(self.nome)

onibus = Onibus()
aluno = Aluno("Carlos")
aluno.ir_para_curso(onibus)

3 - Crie uma classe Funcionario e Departamento que contém uma lista de Funcionarios.Departamento deve agregar funcionários já criados.
class Funcionario:
    def __init__(self, nome):
        self.nome = nome

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"Departamento: {self.nome}")
        for f in self.funcionarios:
            print(f"- {f.nome}")

f1 = Funcionario("Carlos")
f2 = Funcionario("Ana")

dep = Departamento("Recursos Humanos")
dep.adicionar_funcionario(f1)
dep.adicionar_funcionario(f2)
dep.listar_funcionarios()

4 - Crie as classes Time e Jogador. Um Jogador tem nome e posição como atributos, enquanto Time agrega jogadores em uma lista.

class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def listar_jogadores(self):
        print(f"Time: {self.nome}")
        for i in self.jogadores:
            print(f"- {i.nome} ({i.posicao})")

j1 = Jogador("Romarinho", "Atacante")
j2 = Jogador("Gabriel", "Goleiro")

time = Time("Sport")
time.adicionar_jogador(j1)
time.adicionar_jogador(j2)
time.listar_jogadores()

5 - Crie a classe Carro que possui um Motor. O Motor deve ser criado dentro do Carro. Se o Carro deixar de existir, o Motor também deixa. Mostre isso criando e depois apagando o objeto.

class Motor:
    def __init__(self):
        print("Motor criado.")

    def ligar(self):
        print("Motor ligado.")

    def __del__(self):
        print("Motor destruído.")

class Carro:
    def __init__(self):
        self.motor = Motor()
        print("Carro criado.")

    def ligar(self):
        self.motor.ligar()

    def __del__(self):
        print("Carro destruído.")

carro = Carro()
carro.ligar()

del carro  

6 - Crie a classe Casa que é composta por vários Comodos (sala, cozinha, quarto, etc.). Cada Comodo deve ser criado dentro da Casa.
class Comodo:
    def __init__(self, nome):
        self.nome = nome

class Casa:
    def __init__(self):
        self.comodos = [
            Comodo("Sala"),
            Comodo("Cozinha"),
            Comodo("Quarto")
        ]
        print("Casa criada com cômodos")

    def listar_comodos(self):
        print("Cômodos da casa:")
        for i in self.comodos:
            print(f"- {i.nome}")

casa = Casa()
casa.listar_comodos()
