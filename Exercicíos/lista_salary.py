import pandas as pd
arquivo = "salary.xslsx"
df = pd.read_excel(arquivo)

#1.	Quantas linhas e quantas colunas tem o dataset?

#2.	Qual a média salarial? Qual é o maior salário? O menor salário?
print(f"media: {df['salary'].mean()}")
print(f"maior: {df['salary'].max()}")
print(f"menor: {df['salary'].min()}")

#3.	Crie um df com apenas as colunas job_title, salary, company_location, company_size, remote_ratio?

ds = df[df['job_title'] == 'Data Scientist']
maior_ds = ds.loc[ds['salary'].idxmax(), ['salary', 'company_location']]
menor_ds = ds.loc[ds['salary'].idxmin(), ['salary', 'company_location']]
print(f"Maior: {maior_ds}\Menor: {menor_ds}")

#4.	Qual é o maior e menor salário de um “Data Scientist”? Onde fica essas empresas?

medias_profissao = df.groupby('job_title')['salary'].mean()
print(f"Maior media: {medias_profissao.idxmax()}")
print(f"Menor media: {medias_profissao.idxmin()}")

#5.	Qual a profissão com a maior média salarial? E a menor?

medias_profissao = df.groupby('job_title')['salary'].mean()
print(f"Maior media: {medias_profissao.idxmax()}")
print(f"Menor media: {medias_profissao.idxmin()}")

#6.	Quais as profissões com a média salarial maior que a média geral?

media_geral = df['salary'].mean()
medias_profissao[medias_profissao > media_geral]

#7.	Qual a localização com maior média salarial?

df.groupby('company_location')['salary'].mean().idxmax()

#8.	Quais as profissões que existem no Brasil (BR)?

df[df['company_location'] == 'BR']['job_title'].unique()

#9.	Qual a média salarial no Brasil?

df[df['company_location'] == 'BR']['salary'].mean()

#10.Quantas profissões existem no Brasil?

df[df['company_location'] == 'BR']['job_title'].nunique()

#11.Qual a profissão que mais ganha no Brasil?

df_br = df[df['company_location'] == 'BR']
df_br.loc[df_br['salary'].idxmax(), 'job_title']

#12.Quantas profissões tem nos US e que trabalham em empresas grandes (L)?

df[(df['company_location'] == 'US') & (df['company_size'] == 'L')]['job_title'].nunique()

#13.Qual é a média salarial das empresas médias (M) na Canada (CA)?

df[(df['company_location'] == 'CA') & (df['company_size'] == 'M')]['salary'].mean()

#14.Qual é o país com mais profissões? E qual é o mais com menos?

diversidade = df.groupby('company_location')['job_title'].nunique()
print(f"Mais profissões: {diversidade.idxmax()}, Menos: {diversidade.idxmin()}")

#15.Quem ganha mais que trabalha remoto, presencial ou híbrido?

df.groupby('remote_ratio')['salary'].mean().idxmax()

#16.Qual o país com maior numero de profissões trabalhando 100% remoto?

df[df['remote_ratio'] == 100]['company_location'].value_counts().idxmax()
