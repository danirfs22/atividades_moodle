1 - Crie uma interface chamada Pagamento com um método abstrato processar(valor). Depois, crie duas classes (CartaoCredito e Boleto) que implementem a interface. Mostre como chamar processar() para cada uma.
from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class CartaoCredito(Pagamento):
    def processar(self, valor):
        return f"Pagamento de R${valor} processado no cartão de crédito."

class Boleto(Pagamento):
    def processar(self, valor):
        return f"Boleto gerado no valor de R${valor}."

cartao = CartaoCredito()
boleto = Boleto()

print(cartao.processar(170))
print(boleto.processar(110))

2 - Crie duas interfaces: Ligavel (com o método ligar()) e Desligavel (com o método desligar()). Crie uma classe Computador que implemente ambas. Mostre seu uso.
from abc import ABC, abstractmethod

class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass

class Computador(Ligavel, Desligavel):
    def ligar(self):
        return "Computador ligado."

    def desligar(self):
        return "Computador desligado."

pc = Computador()
print(pc.ligar())
print(pc.desligar())

3 - Crie uma interface Imprimivel com o método imprimir(). Crie outra interface Exportavel com o método exportar(). Implemente uma classe Relatorio que herde de ambas e implemente os métodos.
from abc import ABC, abstractmethod

class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass

class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        return "Relatório impresso."

    def exportar(self):
        return "Relatório exportado."

rel = Relatorio()
print(rel.imprimir())
print(rel.exportar())

4 - Crie uma interface Repositorio com os métodos salvar(objeto) e buscar(id). Depois, crie uma classe RepositorioMemoria que não implemente um dos métodos. O que acontece quando você tenta instanciá-la? Corrija o código.
from abc import ABC, abstractmethod

class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print("Objeto salvo na memória.")

repo = RepositorioMemoria() 
TypeError: Can't instantiate abstract class RepositorioMemoria with abstract method buscar

# código corrigido:
class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print("Objeto salvo na memória.")

    def buscar(self, id):
        return f"Objeto com id {id} retornado da memória."

repo = RepositorioMemoria()
repo.salvar("Usuário 1")
print(repo.buscar(1))
