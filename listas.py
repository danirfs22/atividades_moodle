# #1-	Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela.
# livros = ["Cavalo de guerra", "Ensinamentos sobre o amor", "Marley & eu"]
# # print(livros)

# #2- Usando a lista livros, exiba apenas o primeiro e o último elemento
# print(livros[0])
# print(livros[-1])

# #3- Adicione mais dois livros à lista livros usando o método append() e exiba a lista atualizada.
# livros.append("Felicidade clandestina")
# livros.append("Amar e ser livre")
# print(livros)

# #4- Insira o livro "Duna" na segunda posição da lista livros usando insert().
# livros.insert(1, "Duna")
# print(livros)

# #5- Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".
# livro = "Silêncio dos inocentes"
# if livro in livros:
#     livros.remove(livro)
# else:
#     print("Livro não encontrado")

#6- Crie uma lista chamada números com os valores [1, 2, 3, 2, 4, 2, 5]. Mostre quantas vezes o número 2 aparece na lista.
# numeros = [1, 2, 3, 2, 4, 2, 5]
# quantidade = numeros.count(2)
# print(f"O número 2 aparece {quantidade} vezes na lista")

#7- Percorra a lista livros e exiba cada livro com a frase: "O livro <nome do livro> é interessante"
# livros = ["Cavalo de guerra", "Ensinamentos sobre o amor", "Marley & eu"]
# for i in livros:
#     print(f"O livro {i} é interessante")

#8- Dada a lista idades = [12, 18, 25, 14, 30], use um laço para exibir somente as idades maiores ou iguais a 18.
# idades = [12, 18, 25, 14, 30]
# for i in idades:
#     if i>=18:
#         print(i)

#9- Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores.
    
# valores = [10, 20, 30, 40]

# soma = 0
# for i in valores:
#     soma += i
# print(f"A soma dos valores é: {soma}")

# #10- Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
# notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.

# notas = []  

# for i in range(2):
#     aluno = []  
#     print(f"Digite as 3 notas do aluno {i+1}:")
#     for n in range(3):
#         nota = float(input(f"Nota {n+1}: "))
#         aluno.append(nota)
#     notas.append(aluno)


# print("\nNotas registradas:", notas)

# for i in range(2):
#     media = sum(notas[i]) / 3
#     print(f"Média do aluno {i+1}: {media}")

# 11- Usando list comprehension, crie um tabuleiro de xadrez vazio e depois adicione todas as peças do jogo na posição inicial. Para melhorar a visualização do tabuleiro, identifique as posições do tabuleiro da seguinte forma:
# •	[ ] - para posições vazias
# •	tor - para a torre
# •	cav - para o cavalo
# •	bis - para o bispo
# •	rai - para a rainha
# •	rei - para o rei
# •	pea - para o peão
# Por fim imprima o tabuleiro na tela, deixando cada linha da matriz abaixo da outra.
tabuleiro = [["[ ]" for _ in range(8)] for _ in range(8)]

tabuleiro[0] = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]
tabuleiro[1] = ["pea"] * 8

tabuleiro[7] = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]
tabuleiro[6] = ["pea"] * 8

for linha in tabuleiro:
    for item in linha:
        print(item, end=" ")
    print()  

