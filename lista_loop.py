# 1.	Crie uma lista frutas contendo as seguintes frutas: "maçã", "banana", "laranja", "uva".
frutas = ["maçã", "banana", "laranja", "uva"]


# 2.	Imprima o primeiro e o último elemento da lista.


print(frutas[0])
print(frutas[3])


# 3.	Adicione a fruta "manga" ao final da lista.
frutas.append("manga")
print(frutas)


# 4.	Remova a fruta "banana" da lista.
frutas.remove("banana")
print(frutas)


# 5.	Substitua "laranja" por "abacaxi".
frutas[1] = "abacaxi"
print(frutas)


# 6.	Crie uma lista numeros contendo os números de 1 a 10.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 7.	Calcule e imprima a soma de todos os números da lista.
soma = sum(numeros)
print(soma)


# 8.	Encontre e imprima o maior e o menor número da lista.
maximo = max(numeros)
print(maximo)

minimo = min(numeros)
print(minimo)


# 9.	Inverta a ordem dos elementos na lista e imprima a lista invertida.
numeros.reverse()
print(numeros)


# 10.	Crie uma lista cidades contendo as seguintes cidades: "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba".
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]


# 11.	Ordene a lista cidades em ordem alfabética.
cidades.sort()
# ordem_alfabetica = sorted(cidades)
print(cidades)


# 12.	Adicione a cidade "Porto Alegre" ao final da lista.
cidades.append("Porto Alegre")
print(cidades)


# 13.	Encontre o índice da cidade "Curitiba" na lista.
indice = cidades.index("Curitiba")
print(indice)


# 14.	Remova a cidade "Rio de Janeiro" da lista.


cidades.remove("Rio de Janeiro")
print(cidades)


# 15.	Crie duas listas lista1 e lista2, onde lista1 contém os números [1, 2, 3] e lista2 contém os números [4, 5, 6].


lista1 = [1,2,3]
lista2 = [4,5,6]


# 16.	Concatene lista1 e lista2 em uma nova lista lista3.


lista3 = lista1 + lista2


# 17.	Imprima lista3.


print(lista3)


# 18.	Crie duas listas animais_domesticos e animais_selvagens, onde animais_domesticos contém ["cachorro", "gato", "coelho"] e animais_selvagens contém ["leão", "tigre", "urso"].


animais_domesticos = ["cachorro", "gato", "coelho"]
animais_selvagens = ["leão", "tigre", "urso"]


# 19.	Concatene as duas listas em uma nova lista todos_animais.

todos_animais = animais_domesticos + animais_selvagens


# 20.	Imprima todos_animais.

print(todos_animais)



# 21.	Crie uma lista nomes contendo os nomes: "Ana", "Pedro", "Maria", "João".

nomes = ["Ana", "Pedro", "Maria", "João"]

# 22.	Utilize um loop for para imprimir cada nome da lista.

print(nomes)
for nome in nomes:
    print(nome)


# 23.	Crie uma nova lista nomes_maiusculos contendo os nomes da lista nomes em letras maiúsculas. Utilize um loop for para isso.
# .append
# .captalize

nomes_maiusculos = []
for nome in nomes:
    nomes_maiusculos.append(nome.upper())
    
print(nomes_maiusculos)

#24.Crie uma lista numeros contendo os números de 1 a 20. Utilize um loop for para imprimir apenas os números pares.
numeros = list(range(1, 21))
for num in numeros:
    if num % 2 == 0:
        print(num)
#25.Usando a lista numeros, utilize um loop for para criar uma nova lista quadrados contendo o quadrado de cada número.
quadrados = []
for num in numeros:
    quadrados.append(num ** 2)
print(quadrados)
#26.Crie uma lista palavras contendo: "python", "java", "c", "javascript". Utilize um loop for para imprimir o tamanho (número de letras) de cada palavra.
palavras = ["python", "java", "c", "javascript"]
for palavra in palavras:
    print(f"A palavra '{palavra}' tem {len(palavra)} letras.")
#27.Crie uma lista idades contendo [12, 18, 25, 40, 60]. Utilize um loop for para imprimir "maior de idade" se a idade for >= 18 ou "menor de idade" se for < 18.
idades = [12, 18, 25, 40, 60]
for idade in idades:
    if idade >= 18:
        print(f"Idade {idade}: maior de idade")
    else:
        print(f"Idade {idade}: menor de idade")
#28.Crie uma lista notas contendo [5.5, 7.0, 8.3, 4.9, 6.2]. Utilize um loop for para contar quantos alunos estão aprovados (nota >= 7) e quantos estão reprovados (nota < 7).
notas = [5.5, 7.0, 8.3, 4.9, 6.2]
aprovados = 0
reprovados = 0

for nota in notas:
    if nota >= 7:
        aprovados += 1
    else:
        reprovados += 1

print(f"Aprovados: {aprovados} | Reprovados: {reprovados}")

#29.Crie uma lista compras com ["arroz", "feijão", "batata", "carne"]. Utilize um loop for para imprimir cada item precedido da frase "Preciso comprar: ".

compras = ["arroz", "feijão", "batata", "carne"]
for item in compras:
    print(f"Preciso comprar: {item}")

#30. Escreva um programa que use um loop while para imprimir os números de 1 a 10.
contador = 1
while contador <= 10:
    print(contador)
    contador += 1
#31. Usando um loop while, peça para o usuário digitar um número inteiro. O programa deve parar quando o usuário digitar o número 0.
numero = -1
while numero != 0:
    numero = int(input("Digite um número (0 para sair): "))
#32. Utilize um loop while para calcular a soma dos números de 1 a 100.
contador = 1
soma = 0
while contador <= 100:
    soma += contador
    contador += 1
print(f"soma total: {soma}")
#33. Peça para o usuário adivinhar um número secreto (por exemplo, 7). Use um loop while para continuar pedindo até que ele acerte.
numero_secreto = 7
palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Adivinhe o numero secreto: "))
    if palpite != numero_secreto:
        print("Errado! Tente novamente.")

print("Parabens! Você acertou.")
#34. Crie um loop while que imprima todos os números pares de 2 até 20.
num = 2
while num <= 20:
    print(num)
    num += 2
