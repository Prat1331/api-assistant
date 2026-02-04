import requests

def get_sample_posts(limit: int = 5):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()[:limit]
