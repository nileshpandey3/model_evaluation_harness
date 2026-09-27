"""
Deterministic integration test of the evaluation pipeline
"""

import json

import pytest

from conversation.evaluators import evaluate_conversation
from conversation.runner import run_scenario
from conversation.scenarios import get_travel_planning_scenario

@pytest.mark.multi_turn_conversation_end_to_end
def test_multi_turn_conversation_end_to_end():
    scenario = get_travel_planning_scenario()

    # add a user turn between the scenario’s existing turns to test more than 2 turns
    scenario["turns"].insert(
        1,
        {
            "role": "user",
            "content": "Make it a two-day trip, keeping the same budget.",
        },
    )

    responses = iter([
        {
            "answer": "A three-day plan",
            "trip_days": 3,
            "currency": "USD",
            "cost_items": [{"item": "trip", "amount": 450}],
        },
        {
            "answer": "A revised two-day plan",
            "trip_days": 2,
            "currency": "USD",
            "cost_items": [{"item": "trip", "amount": 350}],
        },
        {
            "answer": "Another revised one-day plan",
            "trip_days": 1,
            "currency": "USD",
            "cost_items": [{"item": "trip", "amount": 300}],
        },
    ])

    def fake_model(_prompt):
        """
        This gives the evaluator predictable responses,
        so a test failure points to the eval pipeline rather than a change in actual LLM's wording
        """
        return json.dumps(next(responses))

    transcript = run_scenario(scenario, model_call=fake_model)
    result = evaluate_conversation(scenario, transcript)

    scores = result["scores"]
    evidence = result["evidence"]

    assert len(transcript) == 6
    assert scores["constraint_consistency"] is True
    assert scores["multi_turn_consistency"] is True

    assert evidence["final_total_cost"] == 300
    assert evidence["actual_trip_days"] == 1

    assert not result["failure_types"]
