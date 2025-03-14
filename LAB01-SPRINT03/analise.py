import pandas as pd
import matplotlib.pyplot as plt

# Carrega o arquivo CSV
df = pd.read_csv("github_repositories.csv")

# Converte as colunas de data para datetime (elas já vêm com timezone)
df['createdAt'] = pd.to_datetime(df['createdAt'])
df['updatedAt'] = pd.to_datetime(df['updatedAt'])

# Data atual como tz-aware (UTC)
hoje = pd.Timestamp.now(tz='UTC')

# Calcula a idade do repositório (em dias) e os dias desde a última atualização
df['idade_dias'] = (hoje - df['createdAt']).dt.days
df['dias_desde_atualizacao'] = (hoje - df['updatedAt']).dt.days

# Exibe estatísticas
print("Mediana da idade (dias):", df['idade_dias'].median())
print("Mediana dos dias desde a última atualização:", df['dias_desde_atualizacao'].median())

# Análise da Linguagem Primária
linguagens = df['primaryLanguage'].value_counts()
print("\nDistribuição de Linguagens:")
print(linguagens)

# Visualização: Gráfico de Barras para Linguagens
plt.figure(figsize=(10,6))
linguagens.plot(kind='bar')
plt.xlabel("Linguagem")
plt.ylabel("Número de Repositórios")
plt.title("Distribuição de Repositórios por Linguagem Primária")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualização: Histograma da Idade dos Repositórios
plt.figure(figsize=(10,6))
plt.hist(df['idade_dias'], bins=20)
plt.xlabel("Idade do Repositório (dias)")
plt.ylabel("Frequência")
plt.title("Distribuição da Idade dos Repositórios")
plt.tight_layout()
plt.show()

# Visualização: Histograma de Dias desde a Última Atualização
plt.figure(figsize=(10,6))
plt.hist(df['dias_desde_atualizacao'], bins=20)
plt.xlabel("Dias desde a Última Atualização")
plt.ylabel("Frequência")
plt.title("Distribuição do Tempo desde a Última Atualização")
plt.tight_layout()
plt.show()
