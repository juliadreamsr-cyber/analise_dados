# O dataset LOGCP - base_tickets_manutencao_historico.xlsx contém o histórico de incidentes da empresa.
# Através da importantação dos dados através da biblioteca pandas, responda as perguntas abaixo.

import pandas as pd
import requests
import yfinance as yf

import pandas as pd


df = pd.DataFrame
df = pd.read_excel(r"C:\Users\julia\Documents\analisedados\historico_manutencao.xlsx")

arquivo = "historico_manutencao.xlsx"
df = pd.read_excel(arquivo)

df = pd.DataFrame

# 1 - (1,0) Quantos tickets foram (utilize a coluna "des_status"):
#    - Abertos?
#    - Concluídos?
#    - Cancelados?
df.loc[:,"des_status"].unique()
# 2 - (1,0) Qual a taxa de conclusão dos tickets em relação ao total?
df["des_status"].value_counts()
# 3 - (1,0) Qual categoria tem mais tickets(utilize a coluna "des_categoria")?
df["des_categoria"].max()
# 4 - (1,0) Qual categoria tem maior numero de de cancelamento?


# 5 - (1,0) Quanto rendeu a VALE3 nos ultimos 5 anos entre 2020 e 2025?
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# params = {"ticker": "VALE3", "data_ini": "2001-01-01", "data_fim": "2026-12-31"}
# response = requests.get(
#     f"{base_url}/preco/corrigido",
#     headers={"Authorization": f"Bearer {token}"},
#     params=params,
# )

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc4MTUxNzUyLCJpYXQiOjE3NzU1NTk3NTIsImp0aSI6IjgzYjg2ZDc0NTQzMDQzNWRhOThmMmMwODlhYmNlOWFjIiwidXNlcl9pZCI6IjEwMCJ9.ztG3Gcv5p5CYyU2MTYZcVvW0XqcOdPN9Oi1hODzaUxk"
params = {"ticker": "VALE3", "data_ini": "2024-01-01", "data_fim": "2025-12-31"}
resp = requests.get(
    f"{base_url}/preco/diversos",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
print(resp.json())

dados = resp.json()
df_preco = pd.DataFrame(dados)
preco_fechamento = df_preco.loc[:, ["data", "fechamento"]]
preco_fechamento["fechamento"] = preco_fechamento["fechamento"].str.replace(',', '.').astype(float)
rendimento = preco_fechamento["fechamento"].iloc[-1] / preco_fechamento["fechamento"].iloc[0] - 1
print(f"Rendimento: {rendimento:.2%}")



# 6 - (1,0) A BrasilAPI disponibiliza informações da tabela FIPE, incluindo marcas, modelos e preços de veículos.
# Acesse o endpoint de marcas da FIPE para o tipo de veículo carros.
# import requests
# import pandas as pd
# Transforme em DataFrame e acha o codigo BYD através da coluna "nome"
# Use esse código para acessar o endpoint de modelos da marca BYD.
# codigoMarca=""
# api = f"https://brasilapi.com.br/api/fipe/veiculos/v1/{tipoVeiculo}/{codigoMarca}"
# Construa um DataFrame com os modelos disponíveis.
# Responda: quantos modelos de veículos BYD estão cadastrados na FIPE?

import pandas as pd
import requests

tipoVeiculo = "carros"
api = f"https://brasilapi.com.br/api/fipe/marcas/v1/{tipoVeiculo}"

df_carros = pd.DataFrame
print(df_carros)

url_meta  = "http://www.ipeadata.gov.br/api/odata4/Metadados"
resp_tipo = requests.get(url_meta, timeout=60)
df_carros   = pd.DataFrame(resp_carros.json()["value"])

mask_tipo   = df_carros["MODELO"].str.upper().str.contains("FIPE",          na=False)
mask_vendas = df_carros["BRASIL"].str.lower().str.contains("BYD", na=False)
df_fipe_BYD = df_carros[mask_tipo & mask_vendas].copy()

print(f"Séries FIPE 'vendas - Brasil' encontradas: {df_fipe_BYD.shape[0]}")
print(df_fipe_BYD[["MODELO", "BRASIL", "FNTSIGLA"]].to_string(index=False), "\n")



# 7 - (1,0) O Banco Mundial disponibiliza uma API pública com diversos indicadores econômicos. 
# O código do indicador NY.GDP.PCAP.CD corresponde ao PIB per capita (em dólares correntes).
# Usando Python e a biblioteca requests para acessar a API e pandas para manipulação dos dados:
# Acesse o indicador "NY.GDP.PCAP.CD" e o pais "BRA".

import pandas as pd
import requests

df_BM = pd.DataFrame
df_pais = pd.DataFrame
df_indicador = pd.DataFrame

url = f"https://api.worldbank.org/v2/country/{pais}/indicator/{indicador}?format=json"
# Construa um DataFrame atraves do segundo elemento da lista do retorno
#segundo elemento é o [1]
# Selecione apenas as colunas anos (date) e os valores de PIB per capita (value).
# Identifique em qual ano o Brasil apresentou o menor PIB per capita e mostre o respectivo valor.

df.groupby("country")["score"].min().sort_values(ascending=False).head(1)

# 8 - (1,0) - Faça um ranking das 30 melhores empresas baseado nos indicadores Return on Equity (roe) e Dividend Yield (dividend_yield) no dia 2024-04-01.
# Faça uma média entre o ranking das empresas com maior ROE e o ranking das empresas com maior dividend_yield
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )

import os
import requests
import pandas as pd
import yfinance as yf

BASE_URL  = "https://laboratoriodefinancas.com/api/v2"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc4MTUxNzUyLCJpYXQiOjE3NzU1NTk3NTIsImp0aSI6IjgzYjg2ZDc0NTQzMDQzNWRhOThmMmMwODlhYmNlOWFjIiwidXNlcl9pZCI6IjEwMCJ9.ztG3Gcv5p5CYyU2MTYZcVvW0XqcOdPN9Oi1hODzaUxk"
HEADERS   = {"Authorization": f"Bearer {TOKEN}"}

DATA_BASE   = "2024-04-01"              
DATA_INI    = "2021-03-21"              
DATA_FIM    = "2026-03-23"              
DATA_FIM_YF = "2026-03-24"             

print("Buscando dados do planilhão...")

resp = requests.get(
    f"{BASE_URL}/bolsa/planilhao",
    headers=HEADERS,
    params={"data_base": DATA_BASE},
)
resp.raise_for_status()

df  = pd.DataFrame(resp.json())
df2 = df[["ticker", "roic", "earning_yield"]].dropna().copy()

df2["rank_roic"]  = df2["roic"].rank(ascending=False)
df2["rank_ey"]    = df2["earning_yield"].rank(ascending=False)
df2["rank_final"] = (df2["rank_roic"] + df2["rank_ey"]) / 2

top30 = (
    df2.sort_values("rank_final", ascending=True)["ticker"]
    .head(30)
    .tolist()
)

print(f"\nTop 30 Magic Formula ({DATA_BASE}):")
for i, ticker in enumerate(top30, 1):
    print(f"  {i:2}. {ticker}")

print(f"\nBuscando histórico de preços ({DATA_INI} → {DATA_FIM})...")

resultados = []

for acao in top20:
    print(f"  Buscando {acao}...")
    resp = requests.get(
        f"{BASE_URL}/preco/corrigido",
        headers=HEADERS,
        params={"ticker": acao, "data_ini": DATA_INI, "data_fim": DATA_FIM},
    )

    if resp.status_code != 200:
        print(f"  Aviso: {acao} retornou status {resp.status_code} — pulando.")
        continue

    dados = resp.json()
    if not dados:
        print(f"  Aviso: {acao} sem dados — pulando.")
        continue

    df_preco = pd.DataFrame(dados)

    if "fechamento" not in df_preco.columns:
        print(f"  Aviso: {acao} sem coluna 'fechamento' — pulando.")
        continue

    filtro_ini = df_preco["data"] == DATA_INI
    filtro_fim = df_preco["data"] == DATA_FIM
    df_sorted  = df_preco.sort_values("data")

    preco_ini = float(df_preco.loc[filtro_ini, "fechamento"].iloc[0]) if filtro_ini.any() else float(df_sorted["fechamento"].iloc[0])
    preco_fim = float(df_preco.loc[filtro_fim, "fechamento"].iloc[0]) if filtro_fim.any() else float(df_sorted["fechamento"].iloc[-1])

    retorno = (preco_fim / preco_ini - 1) * 100

    resultados.append({
        "ticker":      acao,
        "preco_ini":   round(preco_ini, 2),
        "preco_fim":   round(preco_fim, 2),
        "retorno_pct": round(retorno, 2),
    })
    filtro_ini = df_preco["data"] == DATA_INI
    filtro_fim = df_preco["data"] == DATA_FIM
    df_sorted  = df_preco.sort_values("data")

    preco_ini = float(df_preco.loc[filtro_ini, "fechamento"].iloc[0]) if filtro_ini.any() else float(df_sorted["fechamento"].iloc[0])
    preco_fim = float(df_preco.loc[filtro_fim, "fechamento"].iloc[0]) if filtro_fim.any() else float(df_sorted["fechamento"].iloc[-1])

    retorno = (preco_fim / preco_ini - 1) * 100

    resultados.append({
        "ticker":      acao,
        "preco_ini":   round(preco_ini, 2),
        "preco_fim":   round(preco_fim, 2),
        "retorno_pct": round(retorno, 2),
    })

    filtro_ini = df_preco["data"] == DATA_INI
    filtro_fim = df_preco["data"] == DATA_FIM
    df_sorted  = df_preco.sort_values("data")

    preco_ini = float(df_preco.loc[filtro_ini, "fechamento"].iloc[0]) if filtro_ini.any() else float(df_sorted["fechamento"].iloc[0])
    preco_fim = float(df_preco.loc[filtro_fim, "fechamento"].iloc[0]) if filtro_fim.any() else float(df_sorted["fechamento"].iloc[-1])

    retorno = (preco_fim / preco_ini - 1) * 100

    resultados.append({
        "ticker":      acao,
        "preco_ini":   round(preco_ini, 2),
        "preco_fim":   round(preco_fim, 2),
        "retorno_pct": round(retorno, 2),
    })

df_resultado = pd.DataFrame(resultados).sort_values("retorno_pct", ascending=False)

dados= resp.json()
df = pd.DataFrame(dados)

maximo = df["roe"].max()
filtro = df["roe"] == maximo
df[filtro]

# 9 - (1,0) Quantos setores ("setor") tem essa carteira formada por 30 ações?


# 10 - (1,0) 11 - Você tem acesso à API do Laboratório de Finanças, que fornece dados do Planilhão em formato JSON. 
# Selecione a empresa do setor de "varejo" que apresenta o maior endividamento na data base 2024-04-01.
# Exiba APENAS AS COLUNAS "ticker", "setor", "preco", "endividamento"
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )


base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc4MTUxNzUyLCJpYXQiOjE3NzU1NTk3NTIsImp0aSI6IjgzYjg2ZDc0NTQzMDQzNWRhOThmMmMwODlhYmNlOWFjIiwidXNlcl9pZCI6IjEwMCJ9.ztG3Gcv5p5CYyU2MTYZcVvW0XqcOdPN9Oi1hODzaUxk"
response = requests.get(
     f"{base_url}/bolsa/planilhao",
     headers={"Authorization": f"Bearer {token}"},
     params={"data_base": "2026-04-01"},
 )

info = pd.DataFrame
info[["institution", "country", "score"]]


dados_varejo = {
    "valor": ["ticker"],
    "local": ["setor"],
    "dinheiro": ["preco1"],
    "indice": ["endividamento"],
}

# 11 - (1,0) O IPEA disponibiliza uma API pública com diversas séries econômicas.
# Para localizar uma série de interesse, é necessário acessar primeiro o endpoint de metadados.
# Acesse o endpoint de metadados:
# "http://www.ipeadata.gov.br/api/odata4/Metadados"
# Transforme o retorno em um DataFrame.
# Filtre para encontrar as séries do IBGE relacionadas à taxa de desemprego no Brasil.
# Dica:
# - Utilize a coluna FNTSIGLA para encontrar as séries do "IBGE";
# - Utilize a coluna SERNOME para encontrar as séries relacionadas a "Taxa de desemprego - cor negra"

url4 = "http://www.ipeadata.gov.br/api/odata4/Metadados/"
response4 = requests.get(url4)
response4.status_code
dados = response4.json()["value"]
df = pd.json_normalize(dados)
df = df.loc[:, ["SERCODIGO", "SERNOME", "SERCOMENTARIO"]]

df.columns
df.loc[:, ("desemprego", "brasil") ]. sort_values("IBGE")

url_meta = "http://www.ipeadata.gov.br/api/odata4/Metadados"
resp_meta = requests.get(url_meta, timeout=60)
df_meta = pd.DataFrame(resp_meta.json()["value"])

print(f"Shape do DataFrame de metadados: {df_meta.shape}")

mask_brasil   = df_meta["FNTSIGLA"].str.upper().str.contains("IBGE", na=False)
mask_desemprego = df_meta["SERNOME"].str.lower().str.contains("desemprego - brasil", na=False)
df_brasil_desemprego = df_meta[mask_brasil & mask_desemprego].copy()

print(f"Séries encontradas: {df_brasil_desemprego.shape[0]}")
print(df_brasil_desemprego[["SERCODIGO", "SERNOME", "FNTSIGLA"]].to_string(index=False), "\n")


# 12 - (1,0) Descubra qual é o código da série correspondente (coluna: SERCODIGO).
# CODIGO_ENCONTRADO = ''
# Usando o código encontrado, acesse a API de valores:
# f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
# Construa um DataFrame a partir da chave 'value' do retorno da API.
# Selecione apenas as colunas de data (VALDATA) e valor (VALVALOR).
# Exiba a Data e o Valor em que a taxa de desemprego atingiu o maior valor da série.

CODIGO_ENCONTRADO = df_brasil_desemprego.iloc[0]["SERCODIGO"]
print(f"Código da série: {CODIGO_ENCONTRADO}")

url_valores = f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
resp_vals = requests.get(url_valores, timeout=60)
df_vals = pd.DataFrame(resp_vals.json()["value"])[["VALDATA", "VALVALOR"]].copy()

df_vals["VALDATA"]  = pd.to_datetime(df_vals["VALDATA"])
df_vals["VALVALOR"] = pd.to_numeric(df_vals["VALVALOR"], errors="coerce")
df_vals.dropna(subset=["VALVALOR"], inplace=True)

row_max = df_vals.loc[df_vals["VALVALOR"].idxmax()]
print(f"Data com valor MÁXIMO : {row_max['VALDATA'].strftime('%Y-%m-%d')}")
print(f"Valor máximo          : {row_max['VALVALOR']:,.2f}\n")