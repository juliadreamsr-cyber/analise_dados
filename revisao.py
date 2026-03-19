#1- Como identificar uma lista em python?
#Um conteúdo de elementos em colchetes

#2- Como pegar o primeiro elemento?
#Primeiro elemento é o 0

#3-Como  identificar um dicionário em python?
#Chaves

#4- Uma lista de dicionários é identificada pela presença de colchetes [] (que indicam a lista) contendo uma ou mais estruturas de chaves {} (que indicam os dicionários).
#Modelo padrão: [ { "chave": "valor" } , { "chave": "valor" } ]


#5- Pela estrutura de ter colchetes por fora e chave por dentro

#6-Utiliza-se a função com a biblioteca pandas -> pd.dataframe. se tiver um dicionário, precisa transformar em uma lista

#7-read.csv

#8-read.excel

#9-utiliza-se dois colchetes ou .loc

#10- string usa o == e coloca entre “ o elemento que deseja 

#11- coloca entre parênteses os filtros e  & entre eles
dicionario = {
"nome": ["laerte", "Ricardo", "Fred"],
"idade": 47,
"endereco": "rua teste"
}
#4
dicionario["nome"]
# 5
lista2 = [dicionario]
lista2[0]
#
import pandas as pd
df = pd. DataFrame(lista)
df = pd. DataFrame([dicionario])
# consumir csv
arquivo = "notas.csv"
df = pd.read_esv(arquivo)
# consumir excel
arquivo = "cadastro_alunos.x1sx"
df = pd.read_excel(arquivo)
#
filtro = df[ "national_rank"] > 4
df[filtro, ["institution", "country"]]
# filtro str
filtro = df[ "institution"].str.contains("^C")
df[filtro]
#
filtro1 = df[ "national_rank"] › 4
filtro2 = df["institution"].str.contains("^(")
df[filtro1 & filtro2]

#O Camo IDentificaR uma Lista em opthon?
#3 Como pegaR o le elemeno de uma lista en pthan?
#3 Como zDentificaR um DicionáRio em pyton?
#E Como pegaR um elemento em dicioníRio?
#3) Como IDentificaR uma lista de DicionaRio?
#Como tRans-DemaR uma lista de dicuraRo em um DAtafene?!
#* Como Consumi um ARQUiVO ESV no DAARame?
#4
#" exce"" ?
#9 Como filtRar uma coluna De valores?
#O Como filtRae uma coluna de stRing?