def create_plan(user_input: str) -> dict:
    steps = []
    text = user_input.lower()

    if "github" in text or "repo" in text:
        steps.append({
            "action": "search_github",
            "query": "AI",
            "limit": 5
        })

    if "weather" in text:
        steps.append({
            "action": "get_weather",
            "city": "London"
        })
        
    if "posts" in text:
        steps.append({
            "action": "get_posts",
            "limit": 5
        })    

    return {"steps": steps}
