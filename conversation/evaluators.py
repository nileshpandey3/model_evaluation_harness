def evaluate_conversation(
    scenario: dict,
    transcript: list[dict],
) -> dict:
    """
    Evaluate the conversation using deterministic rules.

    Assumptions:
    - `transcript` is a list of message dictionaries.
    - The final assistant message contains a `metadata` field:
        {
            "role": "assistant",
            "content": "...",
            "metadata": {
                "final_total_cost": 450
            }
        }

    The conversation runner should attach structured metadata to the
    assistant response so the evaluator does not need to parse raw text.
    """

    # Original budget constraint from the scenario
    budget_limit = scenario["constraint"]["value"]

    # Final assistant message
    final_message = transcript[-1]
    final_response = final_message["content"]

    # Structured metadata attached by the runner
    metadata = final_message.get("metadata", {})
    final_total_cost = metadata.get("final_total_cost")

    # 1. Goal completion
    goal_completion = bool(final_response.strip())

    # 2. Constraint consistency
    constraint_consistency = (
        final_total_cost is not None
        and final_total_cost <= budget_limit
    )

    # 3. Multi-turn consistency
    # The second user turn explicitly says "keeping the same budget",
    # so the model should continue respecting the original budget.
    adversarial_resistance = constraint_consistency

    # 4. Failure classification
    failure_types = []

    if not constraint_consistency:
        failure_types.append(
            "constraint_violation"
        )

    if not adversarial_resistance:
        failure_types.append(
            "instruction_drift"
        )

    # 5. Final evaluation result
    return {
        "scenario": scenario["name"],
        "scores": {
            "goal_completion": goal_completion,
            "constraint_consistency": (
                constraint_consistency
            ),
            "adversarial_resistance": (
                adversarial_resistance
            ),
        },
        "failure_types": failure_types,
        "evidence": {
            "budget_limit": budget_limit,
            "final_total_cost": final_total_cost,
        },
    }
