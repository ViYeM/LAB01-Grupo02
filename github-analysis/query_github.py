import requests
import pandas as pd

GITHUB_TOKEN = "Github Token"
GITHUB_API_URL = "https://api.github.com/graphql"
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Content-Type": "application/json"
}

def fetch_repositories():
    all_repos = []
    cursor = None

    for _ in range(10):  
        query = f"""
        {{
          search(query: "stars:>10000", type: REPOSITORY, first: 100, after: {cursor if cursor else "null"}) {{
            nodes {{
              ... on Repository {{
                nameWithOwner
                createdAt
                primaryLanguage {{ name }}
                updatedAt
              }}
            }}
            pageInfo {{ endCursor hasNextPage }}
          }}
        }}
        """
        response = requests.post(GITHUB_API_URL, json={"query": query}, headers=headers).json()
        repos = response["data"]["search"]["nodes"]
        all_repos.extend(repos)

        if not response["data"]["search"]["pageInfo"]["hasNextPage"]:
            break
        cursor = f'"{response["data"]["search"]["pageInfo"]["endCursor"]}"'

    return all_repos

repos = fetch_repositories()

df = pd.DataFrame(repos)

df.to_csv("github_repositories.csv", index=False)
print("Dados salvos em github_repositories.csv")