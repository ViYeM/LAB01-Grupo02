# Laboratório de Experimentação de Software
# Análise de Repositórios Populares no GitHub

Este projeto tem como objetivo analisar as principais características dos **1.000 repositórios mais populares** no GitHub (com base no número de estrelas). A análise inclui métricas como **idade dos repositórios, contribuição externa, frequência de releases, frequência de atualizações, linguagens de programação utilizadas e percentual de issues fechadas**.

---

## Questões de Pesquisa

O estudo busca responder às seguintes perguntas:

🔹 **RQ 01**: Sistemas populares são maduros/antigos?
   - *Métrica*: Idade do repositório (calculado a partir da data de sua criação).

🔹 **RQ 02**: Sistemas populares recebem muita contribuição externa?
   - *Métrica*: Total de pull requests aceitas.

🔹 **RQ 03**: Sistemas populares lançam releases com frequência?
   - *Métrica*: Total de releases.

🔹 **RQ 04**: Sistemas populares são atualizados com frequência?
   - *Métrica*: Tempo até a última atualização (calculado a partir da data de última atualização).

🔹 **RQ 05**: Sistemas populares são escritos nas linguagens mais populares?
   - *Métrica*: Linguagem primária de cada um desses repositórios.

🔹 **RQ 06**: Sistemas populares possuem um alto percentual de issues fechadas?
   - *Métrica*: Razão entre número de issues fechadas pelo total de issues.

🔹 **RQ 07 (Bônus)**: Sistemas escritos em linguagens mais populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência?
   - *Métrica*: Comparação das métricas das RQs 02, 03 e 04 entre as linguagens de programação mais populares e outras linguagens.

---

## Estrutura do Projeto

📌 **Lab01S01**: Consulta GraphQL para os primeiros 100 repositórios e obtenção de todas as métricas necessárias para responder às RQs.

📌 **Lab01S02**: Paginação para consultar 1.000 repositórios, armazenamento dos dados em um arquivo CSV e elaboração da primeira versão do relatório com as hipóteses informais.

📌 **Lab01S03**: Análise e visualização de dados, elaboração do relatório final com os resultados e discussões.

---

## Dependências

Para executar este projeto, instale as seguintes dependências:

```sh
pip install -r requirements.txt
```

Dependências utilizadas:
- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- Requests

---

## Como Configurar o Ambiente

### 1️⃣ Clone este repositório:
```sh
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2️⃣ Crie e ative um ambiente virtual (opcional, mas recomendado):
```sh
python -m venv venv  # Criação do ambiente virtual
source venv/bin/activate  # Ativação no macOS/Linux
venv\Scripts\activate  # Ativação no Windows
```

### 3️⃣ Instale as dependências:
```sh
pip install -r requirements.txt
```

### 4️⃣ Execute o script de coleta de dados:
```sh
python coletar_dados.py
```

### 5️⃣ Analise os dados e gere as visualizações:
```sh
python analisar_dados.py
```
