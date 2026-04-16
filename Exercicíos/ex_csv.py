# LISTA DE EXERCÍCIOS – ANÁLISE DE DADOS COM PANDAS Dataset: Ranking
# Mundial de Universidades (notas.csv)
import pandas as pd

df = pd.read_csv(r"C:\Users\julia\Documents\analisedados\notas.csv")
# ============================================================
# EXPLORAÇÃO INICIAL (EDA BÁSICA)
# ============================================================

# Exercício 1 – Conhecendo o Dataset 
# 1. Quantas linhas e colunas existem?
df.shape
# 2. Quais são os tipos de dados? 
df.dtypes
# 3. Existe coluna com valores ausentes?
df.isnull().sum()
# 4. Qual é o período de anos disponível? 
df.columns
df.loc[:,"year"].unique()
# 5. Quantos países diferentes existem?
df.loc[:,"country"].unique()

# Exercício 2 – Estatísticas Gerais 
# 1. Média do score 
df.columns
df.loc[:,"score"].mean()
# 2. Maior score 
df["score"].max()
# 3.Menor score 
df["score"].min()
# 4. Média do score por ano 
df.groupby("year")["score"].mean()
# 5. Desvio padrão do score
df["score"].std()
# ============================================================
# FILTROS E SELEÇÕES
# ============================================================

# Exercício 3 – Top Universidades 
# 1. Mostre as 10 melhores universidades do mundo (menor world_rank) 
df.columns
df.loc[:, ("institution", "world_rank") ]. sort_values("world_rank")
# 2. Mostre as 5 melhores universidades do Brasil (se existirem)
filtro = df["country"] =="Brazil"
df.loc[filtro , ("institution", "world_rank", "country")].sort_values("world_rank")
# 3. Mostre universidades com score maior que 90 
df[df["score"] > 90]
# 4. Mostre universidades dos EUA com score maior que 80
df[(df["country"] == "United States") & (df["score"] > 80)]

# Exercício 4 – Seleção Avançada 
# 1. Mostre apenas as colunas: institution, country e score 
df[["institution", "country", "score"]]
# 2. Mostre universidades entre rank 50 e 100 
df[(df["world_rank"] >= 50) & (df["world_rank"] <= 100)]
# 3. Mostre universidades cujo país é “United Kingdom”
df[df["country"] == "United Kingdom"]

# ============================================================ PARTE 3 –
# MISSING VALUES
# ============================================================

# Exercício 5 – Valores Ausentes 
# 1. Quantos valores nulos existem na coluna broad_impact? 
df["broad_impact"].isnull().sum()
# 2. Qual percentual do dataset é nulo? 
df["broad_impact"].isnull().mean() * 100
# 3. Remova linhas com broad_impact nulo 
df_sem_nulos = df.dropna(subset=["broad_impact"])
# 4. Preencha valores nulos com a média 
media = df["broad_impact"].mean()
df["broad_impact"].fillna(media, inplace=True)
# 5. Compare a média antes e depois do preenchimento
media_antes = df["broad_impact"].mean()
media_depois = df["broad_impact"].mean()
# ============================================================ PARTE 4 –
# GROUPBY (ANÁLISE POR PAÍS E ANO)
# ============================================================

# Exercício 6 – Análise por País 
# 1. Média do score por país 
df.groupby("country")["score"].mean()
# 2. País com maior média de score 
df.groupby("country")["score"].mean().sort_values(ascending=False).head(1)
# 3. Quantidade de universidades por país
df["country"].value_counts()
# 4. Top 10 países com mais universidades
df["country"].value_counts().head(10)

# Exercício 7 – Análise por Ano 
# 1. Média do score por ano 
media_ano = df.groupby("year")["score"].mean()
# 2. Qual ano teve maior média? 
media_ano.sort_values(ascending=False).head(1)
# 3. Faça um gráfico da evolução do score médio ao longo do tempo
import matplotlib.pyplot as plt

media_ano.plot()
plt.title("Evolução do Score Médio ao Longo do Tempo")
plt.xlabel("Ano")
plt.ylabel("Score Médio")
plt.show()