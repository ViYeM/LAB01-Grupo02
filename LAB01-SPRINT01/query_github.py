import requests

GITHUB_TOKEN = "github token"

GITHUB_API_URL = "https://api.github.com/graphql"

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Content-Type": "application/json"
}

query = """
{
  search(query: "stars:>10000", type: REPOSITORY, first: 100) {
    nodes {
      ... on Repository {
        nameWithOwner
        createdAt
        primaryLanguage { name }
        updatedAt
      }
    }
  }
}
"""

response = requests.post(GITHUB_API_URL, json={"query": query}, headers=headers)

print(response.json())
