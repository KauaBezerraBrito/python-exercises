# Exercício 1
# Crie um sistema de cadastro de produtos em uma lista de produtos
# Seu sistema deve:
# - Pegar o usuário qual produto vai ser cadastrado por meio de um input
# - Garantir que se o usuário escrever com letra maiúscula ou minúscula, o produto continua sendo o mesmo produto
# - Se o usuário inserir um produto que já existe na lista, o programa deve printar a mensagem "Produto já existente, tente novamente"
# - Se o usuário inserir um produto que não existe na lista, o programa deve inserir na lista, printar a mensagem Produto X cadastrado com sucesso e em seguida printar a lista completa

produtos = ["celular", "camera", "fone de ouvido", "monitor"]

produto = input("Informe o produto a ser cadastrado: ")
produto = produto.casefold()

if produto in produtos:
    print("Produto já existente, tente novamente")
else:
    produtos.append(produto)

    print(f"Produto {produto} cadastrado com sucesso")
    print(produtos)


# Exercício 2
# Crie um sistema de consulta de preços
# Seu sistema deve:
# - Pedir para o usuário o nome de um produto
# - Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta
#        - Ex: O produto celular custa R$1500
# - Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente

produtos = ["celular", "camera", "fone de ouvido", "monitor"]
precos = [1500, 1000, 800, 2000]

produto = input("Informe o nome do produto: ")

if produto in produtos:
    print(f"O produto {produto} custa R${precos[produtos.index(produto)]}")
else:
    print("Produto não encontrado, tente novamente")

# Exercício 3
# Crie um sistema de consulta de bônus dos funcionários
# Seu sistema deve:
# - Pegar o valor de vendas do funcinoário por meio de um input
# - Calcular o bônus do funcionário de acordo com a seguinte regra:
#       - Se o funcionário vendeu mais de 1000 unidades, ele ganha R$2 de bonus para cada unidade vendida
#       - Se o funcionário vendeu mais de 5000 unidades, ele ganha R$2 de bônus para cada unidade + um valor fixo de R$1000
#       - Se o funcionário vendeu menos de 1000 unidades, ele não ganha bônus
# - Printar no final o valor do bônus do funcionário

vendas = int(input("Informe a quantidade vendida: "))

if vendas > 1000:
    bonus = vendas * 2

    if vendas > 5000:
        bonus += 1000
else:
    bonus = 0

print(f"Bonus: {bonus}")

# Exercício 4
# Crie um programa que consiga descobrir qual dos vendedores vendeu mais
# As vendas dos vendedores são listas com a quantidade vendida por cada vendedor

vendas = [
    [10, 20, 100, 80, 90, 100, 20, 30, 44, 55, 33, 34, 100, 90, 80, 39, 87, 45, 50, 50, 50, 50, 40, 30, 3, 93, 39, 49, 88],    
    [100, 1, 1, 4, 5, 90, 100, 20, 4, 5, 100, 100, 100, 100, 100, 93, 20, 15, 40, 90, 90, 90, 90, 90, 90, 33, 22, 44, 43, 34],
]

if sum(vendas[0]) > sum(vendas[1]):
    print("Vendedor 1 vendeu mais")
else:
    print("Vendedor 2 vendeu mais")