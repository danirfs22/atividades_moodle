1 - Dada a lista [1, 2, 3, 4, 5], use map com lambda para gerar uma nova lista com o dobro de cada número.
lista = [1, 2, 3, 4, 5]
print(list(map(lambda num:num*2, lista)))

2 - Dada a lista [10, 15, 20, 25, 30], use filter com lambda para obter apenas os números pares.
lista = [10, 15, 20, 25, 30]
print(list(filter(lambda num:num % 2 == 0, lista)))

3 - Usando reduce, some todos os números da lista [1, 2, 3, 4, 5].
from functools import reduce
lista = [1, 2, 3, 4, 5]
print(reduce(lambda x, y : x + y, lista))

4 - Dada a lista ["uva", "banana", "maçã", "laranja"], ordene as palavras pelo tamanho usando sorted e lambda.
lista= ["uva", "banana", "maçã", "laranja"]
ordenados = sorted(lista,key=lambda x:len(x))
print(ordenados)

5 - Dada a lista ["ana", "pedro", "maria"], use map e lambda para transformar em ["Ana", "Pedro", "Maria"].
lista = ["ana", "pedro", "maria"]
print(list(map(lambda x:x.capitalize(), lista)

6 - Usando reduce, calcule o produto (multiplicação) de todos os elementos da lista [2, 3, 4, 5].
from functools import reduce
lista = [2, 3, 4, 5]
print(reduce(lambda x, y : x * y, lista))

7 - Dada a lista ["banana", "uva", "maçã", "laranja"], ordene as palavras pelo último caractere.
frutas = ["banana", "uva", "maçã", "laranja"]
ordenadas = sorted(frutas, key=lambda x: x[-1])
print(ordenadas)