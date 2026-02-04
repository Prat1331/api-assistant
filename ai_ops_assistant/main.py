from agents.planner import create_plan
from agents.executor import execute_plan

if __name__ == "__main__":
    task = "Find top AI GitHub repositories"

    plan = create_plan(task)
    print("PLAN:")
    print(plan)

    output = execute_plan(plan)
    print("\nRESULT:")
    print(output)
