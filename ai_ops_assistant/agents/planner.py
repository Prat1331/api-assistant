import json
from llm.openai_client import call_llm

def create_plan(user_input: str) -> dict:
    prompt = f"""
You are a planner agent.
Convert the user request into a JSON plan.

Allowed actions:
- search_github(query, limit)
- get_weather(city)

User request:
"{user_input}"

Return ONLY valid JSON.
"""

    response = call_llm(prompt)
    return json.loads(response)
