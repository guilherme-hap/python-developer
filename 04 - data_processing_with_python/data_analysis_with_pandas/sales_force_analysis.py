"""
    Programa que utiliza das bibliotecas 'pandas' e 'matplotlib' para fazer uma análise exploratória
    dos dados de uma base de dados externa e mostra, visualmente, os resultados da análise.
"""
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-dark')

df = pd.read_excel("dataset.xlsx")

# print(df.columns)  # Verificando as colunas da base de dados

# print(df.shape) # Verificando a quantidade de linhas e colunas

# print(df.dtypes)  # Verificando os tipos de dados

# print(df.isnull().sum())  # Verificando se há dados nulos na base de dados

# print(df.describe())  # Verificando dados estatísticos da base de dados

# print(df.groupby("City")["Qty"].sum().sort_values(ascending=False))  # Verificando a quantidade de vendas por cidade

# print(df.groupby("Region")["Qty"].sum().sort_values(ascending=False))  # Verificando a quantidade de vendas por região

# print(df.groupby("Category")["Qty"].sum().sort_values(ascending=False))  # Verificando a qtde de vendas por categoria

# print(df.groupby("Product")["Qty"].sum().sort_values(ascending=False))  # Verificando a qtde de vendas por produto

# print(df.groupby("City")["TotalPrice"].sum().sort_values(ascending=False))  # Verificando a receita de cada cidade

# print(df.groupby("Region")["TotalPrice"].sum().sort_values(ascending=False))  # Verificando a receita de cada região

# print(df.groupby([df["Date"].dt.year, "Product"])["TotalPrice"].sum())  # Receita total por ano dos produtos

df_2022 = df[df["Date"].dt.year == 2022]  # Criando variável com os dados apenas de 2022

# print(df.groupby(df["Date"].dt.month)["TotalPrice"].sum())  # Verificando receita total por mês

# Plotando os gráficos dos dados
df.groupby("Product")["Qty"].sum().sort_values(ascending=False).plot.barh(title="Total product sales")
plt.xlabel("Total")
plt.ylabel("Product")
plt.show()

df.groupby(df["Date"].dt.year)["TotalPrice"].sum().plot.bar(title="Receipt x Year")
plt.xlabel("Year")
plt.ylabel("Receipt")
plt.xticks(rotation='horizontal')
plt.show()

df_2022.groupby(df_2022["Date"].dt.month)["TotalPrice"].sum().plot(title="[2022] Total receipt x Month")
plt.xlabel("Month")
plt.ylabel("Receipt")
plt.show()
