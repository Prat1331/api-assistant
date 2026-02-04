def verify_results(results: dict) -> dict:
    final_output = {}

    # Verify GitHub results
    github_results = results.get("github_results")

    if not github_results:
        final_output["github_results"] = "No repositories found."
    else:
        final_output["github_results"] = github_results

    final_output["status"] = "success"

    return final_output
