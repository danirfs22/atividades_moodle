#1 - Crie um dicionário chamado aluno com as chaves: "nome", "idade" e "nota", e preencha com valores fictícios.
# aluno = {"nome": "Maria", "idade": 30, "nota":8.0}

# 2- Dado o dicionário:

# produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
# # Imprima o nome do produto e a quantidade em estoque.
# print(produto["nome"], produto["estoque"])

# 3 - Adicionando novos pares chave-valor

# Dado o dicionário:

# pessoa = {"nome": "Carlos", "idade": 30}
# # Adicione uma nova chave "cidade" com valor "São Paulo".
# pessoa["cidade"] = "São Paulo"
# print(pessoa)

# 4 - Removendo elementos

# Dado o dicionário:

# carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
# # Remova a chave "ano" do dicionário.
# carro.pop("ano")
# print(carro)

# 5 - Verifique se a chave "telefone" existe no dicionário:

# contato = {"nome": "Ana", "email": "ana@email.com"}
# if "telefone" in contato:
#     print("A chave 'telefone' existe no dicionário")
# else:
#     print("A chave 'telefone' não existe no dicionário")

# 6 - Escreva uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra.

# def contagem_palavras(lista):
#     contagem = {}
#     for palavra in lista:
#         if palavra in contagem:
#             contagem[palavra] += 1
#         else:
#             contagem[palavra] = 1
#     return contagem
# palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
# resultado = contagem_palavras(palavras)
# print(resultado)

# 7 - Dado o dicionário:

# d = {"a": 1, "b": 2, "c": 3}
# Crie um novo dicionário invertendo as chaves e os valores: {1: "a", 2: "b", 3: "c"}.
# inversao = {valor: chave for chave, valor in d.items()}

# print(inversao)

# 8 - Dicionário com listas

# Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.alunos = {
# alunos = {"Ana": [8.0, 7.5, 9.0],
#     "Bianca": [6.0, 7.0, 5.5],
#     "Carol": [9.5, 8.0, 10.0]
# }
# for nome, notas in alunos.items():
#     media = sum(notas) / len(notas) 
#     print(f"{nome} - Média: {media}")

# 9 - Mesclando dois dicionários

# Escreva uma função que recebe dois dicionários e retorna um novo dicionário contendo todos os pares chave-valor. Se houver chaves repetidas, o valor do segundo dicionário deve prevalecer.
# def mesclar_dicts(d1, d2):
    
#     novo = d1.copy()
#     novo.update(d2)
#     return novo

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 5, "d": 4}

# resultado = mesclar_dicts(dict1, dict2)
# print(resultado)

# 10 - Ordenando dicionário por valor

# Dado o dicionário:

pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
# Imprima os itens do dicionário ordenados pela pontuação (valor), do maior para o menor
while pontuacoes:
    
    maior = None
    for nome in pontuacoes:
        if maior is None or pontuacoes[nome] > pontuacoes[maior]:
            maior = nome
    print(maior, "-", pontuacoes[maior])
    del pontuacoes[maior]