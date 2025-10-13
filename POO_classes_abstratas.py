1 - Crie uma classe abstrata chamada Animal que possua um método abstrato falar(). Em seguida, crie duas classes concretas (Cachorro e Gato) que implementem esse método. Mostre o uso criando objetos e chamando o método falar().

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

dog = Cachorro()
cat = Gato()

print(dog.falar()) 
print(cat.falar()) 

2 - Tente instanciar diretamente a classe Animal da questão anterior e explique o erro gerado pelo Python.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass

bicho = Animal()

TypeError: Can't instantiate abstract class Animal with abstract method falar (O erro acontece porque não é permitido criar objetos de classes que ainda contêm métodos abstratos, pois classes abstratas servem apenas como modelos — elas definem o que deve ser feito, mas não como).

3 - Defina uma classe abstrata FormaGeometrica com dois métodos abstratos: area() e perimetro(). Crie uma classe concreta Retangulo que herde de FormaGeometrica e implemente os dois métodos. Teste criando um objeto e calculando sua área e perímetro.
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

ret = Retangulo(4, 7)
print("Área do retângulo:", ret.area())
print("Perímetro do retângulo:", ret.perimetro())

4 - Crie uma classe abstrata Transporte com dois métodos abstratos: mover() e parar(). Depois, crie uma subclasse Carro que implemente apenas o método mover(). O que acontece quando você tenta instanciar Carro? Corrija implementando o segundo método.
from abc import ABC, abstractmethod

# método errado:
class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass

class Carro(Transporte):
    def mover(self):
        return "O carro está se movendo."

meu_carro = Carro()
TypeError: Can't instantiate abstract class Carro with abstract method parar (o erro ocorre porque uma classe só pode ser instanciada se todas as abstrações forem implementadas, no caso, faltou implementar o método parar).

# código corrigido:
from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass

class Carro(Transporte):
    def mover(self):
        return "O carro está se movendo."

    def parar(self):
        return "O carro parou."

meu_carro = Carro()
print(meu_carro.mover())
print(meu_carro.parar())
