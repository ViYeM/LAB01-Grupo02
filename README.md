cat <<EOL > README.md
# **Análise de Repositórios Populares do GitHub**

Este projeto tem como objetivo analisar os 1.000 repositórios mais populares do GitHub, utilizando a API GraphQL para coletar dados e técnicas de análise para responder a questões de pesquisa sobre suas características. O projeto inclui coleta automatizada de dados, processamento e visualização dos resultados.

---

## **Questões de Pesquisa**

1. **RQ 01: Sistemas populares são maduros/antigos?**  
   - *Métrica:* Idade do repositório (calculada a partir da data de criação).

2. **RQ 02: Sistemas populares recebem muita contribuição externa?**  
   - *Métrica:* Total de pull requests aceitas.

3. **RQ 03: Sistemas populares lançam releases com frequência?**  
   - *Métrica:* Total de releases.

4. **RQ 04: Sistemas populares são atualizados com frequência?**  
   - *Métrica:* Tempo até a última atualização.

5. **RQ 05: Sistemas populares são escritos nas linguagens mais populares?**  
   - *Métrica:* Linguagem primária de cada repositório.

6. **RQ 06: Sistemas populares possuem um alto percentual de issues fechadas?**  
   - *Métrica:* Razão entre o número de issues fechadas e o total de issues.

7. **RQ 07 (Bônus):** Sistemas escritos em linguagens populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência?  
   - *Métrica:* Análise segmentada das RQs 02, 03 e 04 por linguagem.

---

## **Estrutura do Projeto**

📂 **src**  
　┣ 📜 \`query_github.py\` → Script responsável pela consulta à API GraphQL do GitHub para coletar dados dos repositórios.  
　┣ 📜 \`analysis.py\` → Script para processar, analisar e visualizar os dados coletados.  

📂 **data**  
　┣ 📜 \`github_repositories.csv\` → Arquivo contendo os dados brutos coletados da API do GitHub.  

📜 **README.md** → Este arquivo, contendo a documentação do projeto.  

---

## **Dependências**

Este projeto foi desenvolvido utilizando **Python 3** e as seguintes bibliotecas:

- \`requests\` → Para requisições à API do GitHub.
- \`pandas\` → Para manipulação e análise dos dados coletados.
- \`matplotlib\` e \`seaborn\` → Para criação de gráficos e visualizações.

Para instalar todas as dependências de uma vez, execute:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

Caso o arquivo \`requirements.txt\` não esteja disponível, instale manualmente:

\`\`\`bash
pip install requests pandas matplotlib seaborn
\`\`\`

---

## **Configuração do Token do GitHub**

Para acessar a API GraphQL do GitHub, você precisa gerar um **Personal Access Token**:

1. **Acesse o GitHub** e vá em **Settings > Developer settings > Personal access tokens**.
2. Clique em **Generate new token**.
3. Selecione as permissões necessárias (*repo* e *read:org* são suficientes).
4. Copie o token gerado.
5. No arquivo \`query_github.py\`, substitua \`"SEU_TOKEN_AQUI"\` pelo seu token real:

\`\`\`python
token = "SEU_TOKEN_AQUI"
headers = {"Authorization": f"Bearer {token}"}
\`\`\`

---

## **Como Configurar o Ambiente**

### **1. Instalar o Python 3**
Se você estiver no **macOS**, pode instalar o Python via [Homebrew](https://brew.sh/):

\`\`\`bash
brew install python
\`\`\`

### **2. Criar um Ambiente Virtual**
Para evitar conflitos com outras instalações, crie e ative um ambiente virtual:

\`\`\`bash
python3 -m venv env
source env/bin/activate  # Para macOS/Linux
\`\`\`

### **3. Instalar Dependências**
Com o ambiente virtual ativado, instale as bibliotecas necessárias:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### **4. Executar a Coleta de Dados**
Após configurar seu token do GitHub, execute o script de coleta:

\`\`\`bash
python src/query_github.py
\`\`\`

O script **consulta a API do GitHub via GraphQL**, coletando informações de até **1.000 repositórios mais populares** e armazenando no arquivo \`github_repositories.csv\`.

### **5. Executar a Análise dos Dados**
Com os dados coletados, você pode executar a análise estatística e visualizações:

\`\`\`bash
python src/analysis.py
\`\`\`

Esse script processa os dados e gera **estatísticas descritivas** e **gráficos** para responder às perguntas da pesquisa.

---

## **Contribuição**
Se quiser contribuir com melhorias no código ou na análise dos dados, siga os passos:

1. Faça um **fork** do repositório.
2. Crie uma **branch** para a sua alteração:
   \`\`\`bash
   git checkout -b minha-contribuicao
   \`\`\`
3. Commit suas mudanças:
   \`\`\`bash
   git commit -m "Melhoria na análise de dados"
   \`\`\`
4. Envie as mudanças para o seu fork:
   \`\`\`bash
   git push origin minha-contribuicao
   \`\`\`
5. Abra um **Pull Request** para revisão.

---

## **Licença**
Este projeto está licenciado sob a **MIT License**, permitindo seu uso, modificação e distribuição.

---

## **Contato**
Caso tenha dúvidas ou sugestões, entre em contato via GitHub Issues ou envie um e-mail. 🚀
EOL
