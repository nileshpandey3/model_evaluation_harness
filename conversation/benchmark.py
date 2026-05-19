from conversation.evaluators import evaluate_conversation
from conversation.runner import run_scenario



def run_benchmark(scenarios: list[dict]) -> dict:
    """
    Run all scenarios and aggregate results.
    """
    scenario_results = []

    for scenario in scenarios:
        transcript = run_scenario(scenario)
        result = evaluate_conversation(
            scenario,
            transcript,
        )

        # Keep transcript with each result for debugging/reporting.
        result["transcript"] = transcript

        scenario_results.append(result)

    total_scenarios = len(scenario_results)

    passed = sum(
        1
        for result in scenario_results
        if not result["failure_types"]
    )

    pass_rate = (
        passed / total_scenarios
        if total_scenarios > 0
        else 0.0
    )

    return {
        "summary": {
            "total_scenarios": total_scenarios,
            "passed": passed,
            "failed": total_scenarios - passed,
            "pass_rate": round(pass_rate, 3),
        },
        "scenario_results": scenario_results,
    }
