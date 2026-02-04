from agents.planner import create_plan
from agents.executor import execute_plan
from agents.verifier import verify_results

if __name__ == "__main__":
    task = "Find top AI GitHub repositories and weather in London"

    plan = create_plan(task)
    print("PLAN:")
    print(plan)

    raw_results = execute_plan(plan)
    print("\nRAW RESULTS:")
    print(raw_results)

    final_output = verify_results(raw_results)
    print("\nFINAL OUTPUT:")
    print(final_output)
