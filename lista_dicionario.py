# %%
aluno = {
    "nome": "Willyan",
    "idade": 20,
    "curso": "CIC",
    "matricula": "2024001234",
    "email": "willyan@email.com",
}


for dado in aluno.items():
    print(dado)

# %%
# Exercício 1: Criando um Dicionário
# Crie um dicionário chamado 'aluno' com as seguintes chaves:
# - 'nome': contendo um nome fictício,
# - 'idade': contendo a idade do aluno,
# - 'curso': contendo o curso que ele está matriculado.
# Após criar o dicionário, exiba seus valores no seguinte formato:
# Nome: <nome>
# Idade: <idade>
# Curso: <curso>

aluno = {"nome": "Willyan", "idade": 20, "curso": "CIC"}

for info in aluno.items():
    texto = f"{info[0]}: {info[1]}".capitalize()
    print(texto)

# %%
# Exercício 2: Manipulação de Dicionário
# Dado o dicionário abaixo:
# produto = {
#     "nome": "Teclado Mecânico",
#     "preco": 350.00,
#     "estoque": 10
# }
# 1. Adicione uma nova chave chamada 'marca' com um valor de sua escolha.
# 2. Atualize o preço do produto para R$ 320,00.
# 3. Reduza o estoque em 2 unidades.
# 4. Remova a chave 'marca' do dicionário.
# 5. Exiba o dicionário atualizado.

produto = {
    "nome": "Teclado Mecânico",
    "preco": 350.00,
    "estoque": 10,
}

produto["marca"] = "Microsoft"

print(produto)
produto["preco"] = 320.00
produto["estoque"] = 8
produto.pop("marca")

print(produto)

# %%
# Exercício 3: Iterando sobre um Dicionário
# Dado o dicionário:
# notas = {
#     "Alice": 8.5,
#     "Bruno": 7.0,
#     "Carla": 9.2,
#     "Daniel": 6.8
# }
# 1. Itere sobre o dicionário e exiba os nomes dos alunos e suas respectivas notas.
# 2. Calcule a média das notas e exiba o resultado.

notas = {"Alice": 8.5, "Bruno": 7.0, "Carla": 9.2, "Daniel": 6.8}

for x in notas.items():
    print(x)
    alunos = f"{x[0]} tirou {x[1]} na prova"
    print(alunos)

media = sum(notas.values()) / len(notas.keys())
print(f"a média é {media}")

# %%
# Exercício 4: Soma de Valores
# Dado um dicionário com valores numéricos, percorra o dicionário e some todos os valores.
# Exemplo:
# numeros = {"a": 10, "b": 20, "c": 30}
# Saída esperada: 60

numeros = {"a": 10, "b": 20, "c": 30}

num = sum(numeros.values())
print(num)

# %%
# Exercício 5: Contagem de Itens Repetidos
# Dado uma lista de elementos, conte a frequência de cada elemento utilizando um dicionário.
# Exemplo:
# lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
# Saída esperada: {'maçã': 3, 'banana': 2, 'laranja': 1}

lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
contagem = {}

for fruta in lista:
    contagem[fruta] = lista.count(fruta)

print(contagem)

# %%
# Exercício 6: Filtrando Dicionário
# Dado um dicionário contendo produtos e seus preços, filtre os produtos que custam mais de R$ 50,00.
# Exemplo:
# produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}
# Saída esperada: {"mochila": 80, "notebook": 3000}

produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}


for p in produtos.copy().items():
    if p[1] < 50:
        produtos.pop(p[0])

print(produtos)

# %%
# Exercício 7: Tradutor Simples
# Crie um dicionário chamado 'tradutor' que contém algumas palavras em inglês como chaves e suas traduções para português como valores.
# Peça ao usuário para digitar uma palavra em inglês e exiba sua tradução, caso exista no dicionário.
# Se a palavra não estiver cadastrada, exiba "Palavra não encontrada".

tradutor = {
    "apple": "maçã",
    "car": "carro",
    "house": "casa",
    "dog": "cachorro",
    "cat": "gato",
    "water": "água",
    "sun": "sol",
    "moon": "lua",
    "computer": "computador",
    "book": "livro",
}

entrada = input()

if entrada not in tradutor.keys():
    print("Palavra não encontrada")
else:
    print(tradutor[entrada])

# %%
# Exercício 8: Lista de Compras
# Crie um dicionário onde as chaves são nomes de produtos e os valores são quantidades.
# Permita ao usuário adicionar produtos, atualizar quantidades e remover itens.
# No final, exiba a lista completa de compras.


compras = {}

while True:
    print("\nOpções:")
    print("1 - Adicionar/Atualizar Produto")
    print("2 - Remover Produto")
    print("3 - Exibir Lista de Compras")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        produto = input("Nome do produto: ").strip().lower()
        quantidade = int(input(f"Quantidade de {produto}: ").strip())

        if produto in compras:
            compras[produto] += quantidade
        else:
            compras[produto] = quantidade

        print(f"{produto} adicionado/atualizado com sucesso!")

    elif opcao == "2":
        produto = input("Nome do produto a remover: ").strip().lower()

        if produto in compras:
            del compras[produto]
            print(f"{produto} removido com sucesso!")
        else:
            print(f"{produto} não está na lista.")

    elif opcao == "3":
        if compras:
            print("\nLista de Compras:")
            for produto, quantidade in compras.items():
                print(f"- {produto}: {quantidade}")
        else:
            print("A lista de compras está vazia.")

    elif opcao == "4":
        print("\nLista final de compras:")
        for produto, quantidade in compras.items():
            print(f"- {produto}: {quantidade}")
        print("Saindo...")
        break

    else:
        print("Opção inválida! Tente novamente.")

# %%
# Exercício 9: Dicionário Aninhado
# Crie um dicionário chamado 'turma' onde as chaves são nomes de alunos e os valores são dicionários contendo:
# - "idade" (inteiro),
# - "notas" (lista de três notas).
# Exemplo de estrutura:
# turma = {
#     "Ana": {"idade": 17, "notas": [8, 9, 7]},
#     "Pedro": {"idade": 18, "notas": [6, 7, 8]},
#     "Mariana": {"idade": 17, "notas": [9, 10, 8]}
# }
# 1. Adicione um novo aluno ao dicionário.
# 2. Calcule a média de notas de cada aluno e exiba no formato:
#    Ana: Média 8.0
#    Pedro: Média 7.0
#    Mariana: Média 9.0
# 3. Encontre o aluno com a maior média e exiba o nome dele.

turma = {
    "Ana": {"idade": 17, "notas": [8, 9, 7]},
    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]},
}

turma["Julia"] = {"idade": 20, "notas": [10, 10, 10]}

medias = {}

for aluno in turma.items():
    # print(aluno)
    nome = aluno[0]
    infos = aluno[1]

    idade = infos["idade"]
    notas = infos["notas"]

    media = sum(notas) / len(notas)
    medias[nome] = media
    print(f"{nome}: Média {media}")


maior = max(medias.values())
for aluno in medias.items():
    if maior == aluno[1]:
        print(aluno)
        break


# %%
# Exercício 10: Cadastro de Funcionários
# Crie um programa que permita cadastrar funcionários em uma empresa.
# O programa deve permitir adicionar funcionários com os seguintes dados:
# - Nome
# - Cargo
# - Salário
# Os funcionários devem ser armazenados em um dicionário onde a chave é o nome e o valor é outro dicionário com os dados do funcionário.
# O programa deve permitir consultar funcionários pelo nome e exibir suas informações.

funcionarios = {}

while True:
    print("\nOpções:")
    print("1 - Adicionar Funcionário")
    print("2 - Consultar Funcionário")
    print("3 - Exibir Todos")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nome = input("Nome do funcionário: ").strip()
        cargo = input("Cargo: ").strip()
        salario = input("Salário: ").strip()

        funcionarios[nome] = {"Cargo": cargo, "Salário": salario}
        print(f"Funcionário {nome} cadastrado com sucesso!")

    elif opcao == "2":
        nome = input("Digite o nome do funcionário para consulta: ").strip()
        if nome in funcionarios:
            print(f"\nNome: {nome}")
            print(f"Cargo: {funcionarios[nome]['Cargo']}")
            print(f"Salário: {funcionarios[nome]['Salário']}")
        else:
            print("Funcionário não encontrado.")

    elif opcao == "3":
        if funcionarios:
            print("\nLista de Funcionários:")
            for nome, dados in funcionarios.items():
                print(f"- {nome}: {dados['Cargo']} - R${dados['Salário']}")
        else:
            print("Nenhum funcionário cadastrado.")

    elif opcao == "4":
        print("Saindo... Aqui está a lista final de funcionários:")
        for nome, dados in funcionarios.items():
            print(f"- {nome}: {dados['Cargo']} - R${dados['Salário']}")
        break

    else:
        print("Opção inválida! Tente novamente.")