from agents.planner import create_plan

if __name__ == "__main__":
    task = "Find top AI GitHub repositories"
    plan = create_plan(task)
    print(plan)
