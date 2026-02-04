import requests

def search_repositories(query, limit=5):
    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": limit
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    items = response.json()["items"]

    results = []
    for repo in items:
        results.append({
            "name": repo["full_name"],
            "stars": repo["stargazers_count"],
            "url": repo["html_url"]
        })

    return results
