import requests
import pandas as pd

# Defina o token diretamente (apenas para testes)
GITHUB_TOKEN = ""  # Substitua pelo seu token, se necessário.
GITHUB_API_URL = "https://api.github.com/graphql"
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Content-Type": "application/json"
}

query = """
query ($cursor: String) {
  search(query: "stars:>10000", type: REPOSITORY, first: 100, after: $cursor) {
    nodes {
      ... on Repository {
        nameWithOwner
        createdAt
        primaryLanguage { name }
        updatedAt
      }
    }
    pageInfo { endCursor hasNextPage }
  }
}
"""

def fetch_repositories():
    all_repos = []
    cursor = None

    for _ in range(10):  # Tenta até 10 iterações para coletar repositórios
        variables = {"cursor": cursor}
        response = requests.post(GITHUB_API_URL, json={"query": query, "variables": variables}, headers=headers).json()
        
        if "errors" in response:
            raise Exception(f"Erro na consulta: {response['errors']}")
        
        repos = response["data"]["search"]["nodes"]
        all_repos.extend(repos)
        
        page_info = response["data"]["search"]["pageInfo"]
        if not page_info["hasNextPage"]:
            break
        
        cursor = page_info["endCursor"]
    
    return all_repos

# Coleta os repositórios e salva em um CSV
repos = fetch_repositories()
df = pd.DataFrame(repos)
df.to_csv("github_repositories.csv", index=False)
print("Dados salvos em github_repositories.csv")
