import json
import math


def extract_trip_days(content: str) -> int:
    try:
        days = json.loads(content)["trip_days"]
    except (TypeError, KeyError, ValueError) as exc:
        raise ValueError("unverifiable_duration") from exc

    if not isinstance(days,int) or days < 1:
        raise ValueError("unverifiable_duration")

    return days

def extract_total_cost(content:str, expected_currency:str):
    """
    Return the model's stated total, or raise ValueError
    """

    try:
        response = json.loads(content)
        if response['currency'] != expected_currency:
            raise ValueError()

        items = response["cost_items"]
        if not isinstance(items, list) or not items:
            raise ValueError()

        total = 0

        for item in items:
            amount = item["amount"]

            if type(amount) not in (int, float):
                raise ValueError("unverifiable_cost")

            if not math.isfinite(amount) or amount < 0:
                raise ValueError("unverifiable_cost")

            total += amount

        return round(total, 2)

    except (TypeError, KeyError, ValueError, IndexError) as e:
        raise ValueError('unverifiable_cost') from e



def evaluate_conversation(scenario: dict, transcript: list[dict]) -> dict:
    """Check the final response's stated cost and requested duration."""
    budget_limit = scenario["constraint"]["value"]
    currency = scenario["constraint"]["currency"]
    expected_days = scenario["expectations"]["final_trip_days"]

    total = None
    within_budget = None
    actual_days = None
    correct_duration = None
    failure_types = []

    if not transcript or transcript[-1].get("role") != "assistant":
        failure_types.append("missing_assistant_response")
    else:
        content = transcript[-1]["content"]

        try:
            total = extract_total_cost(content, currency)
            within_budget = total <= budget_limit
            if not within_budget:
                failure_types.append("constraint_violation")

        except ValueError:
            failure_types.append("unverifiable_cost")

        try:
            actual_days = extract_trip_days(content)
            correct_duration = actual_days == expected_days
            if not correct_duration:
                failure_types.append("duration_mismatch")

        except ValueError:
            failure_types.append("unverifiable_duration")


    return {
        "scenario": scenario["name"],
        "scores": {
            "constraint_consistency": within_budget,
            "multi_turn_consistency": correct_duration,
        },
        "failure_types": failure_types,
        "evidence": {
            "budget_limit": budget_limit,
            "final_total_cost": total,
            "expected_trip_days": expected_days,
            "actual_trip_days": actual_days,
        },
    }
