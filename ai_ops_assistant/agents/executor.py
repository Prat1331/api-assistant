from tools.github_tool import search_repositories
from tools.weather_tool import get_weather

def execute_plan(plan: dict) -> dict:
    results = {}

    for step in plan.get("steps", []):
        action = step.get("action")

        if action == "search_github":
            repos = search_repositories(
                step.get("query"),
                step.get("limit", 5)
            )
            results["github_results"] = repos

        elif action == "get_weather":
            weather = get_weather(step.get("city"))
            results["weather"] = weather

        else:
            results[action] = "Unsupported action"

    return results
