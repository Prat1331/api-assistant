from tools.github_tool import search_repositories

def execute_plan(plan: dict) -> dict:
    results = {}

    for step in plan.get("steps", []):
        action = step.get("action")

        if action == "search_github":
            query = step.get("query")
            limit = step.get("limit", 5)

            repos = search_repositories(query, limit)
            results["github_results"] = repos

        else:
            results[action] = "Unsupported action"

    return results
