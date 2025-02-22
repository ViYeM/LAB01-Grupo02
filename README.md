# Laboratório de Experimentação de Software
# 📊 Análise de Características de Repositórios Populares no GitHub  

Este projeto tem como objetivo estudar as principais características de sistemas open-source populares no GitHub. Para isso, analisamos os 1.000 repositórios com maior número de estrelas, coletando dados como idade, contribuições externas, número de releases, frequência de atualização, linguagens utilizadas e taxa de issues fechadas.  

## 🔍 Questões de Pesquisa  
O estudo busca responder às seguintes questões:  

1️⃣ **Sistemas populares são maduros/antigos?**  
📏 *Métrica:* Idade do repositório (data de criação).  

2️⃣ **Sistemas populares recebem muita contribuição externa?**  
📏 *Métrica:* Total de pull requests aceitas.  

3️⃣ **Sistemas populares lançam releases com frequência?**  
📏 *Métrica:* Total de releases.  

4️⃣ **Sistemas populares são atualizados com frequência?**  
📏 *Métrica:* Tempo até a última atualização.  

5️⃣ **Sistemas populares são escritos nas linguagens mais populares?**  
📏 *Métrica:* Linguagem primária do repositório.  

6️⃣ **Sistemas populares possuem um alto percentual de issues fechadas?**  
📏 *Métrica:* Razão entre o número de issues fechadas e o total de issues.  

📌 **Bônus:**  
7️⃣ **Sistemas escritos em linguagens populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência?**  
📏 *Métrica:* Comparação dos valores das RQs 02, 03 e 04 entre linguagens populares e outras linguagens.  

## 🛠️ Metodologia  
O projeto foi desenvolvido em três etapas principais:  

- **Lab01S01:** Consulta inicial via GraphQL para coletar dados de 100 repositórios.  
- **Lab01S02:** Implementação de paginação para obter 1.000 repositórios, armazenamento em CSV e definição das hipóteses.  
- **Lab01S03:** Análise e visualização dos dados, elaboração do relatório final.  

## 📈 Resultados  
Os dados foram analisados por meio de estatísticas descritivas, incluindo valores medianos para cada métrica. Além disso, realizamos uma segmentação por linguagem para entender padrões específicos.  

## 📄 Relatório  
O relatório completo apresenta:  
- Introdução e hipóteses iniciais  
- Metodologia adotada  
- Resultados obtidos para cada métrica  
- Discussão e análise comparativa  

## 🚀 Tecnologias Utilizadas  
- GitHub GraphQL API  
- Python (para coleta e análise de dados)  
- Pandas e Matplotlib (para manipulação e visualização de dados)  
- Jupyter Notebook (para documentação e experimentação)  
