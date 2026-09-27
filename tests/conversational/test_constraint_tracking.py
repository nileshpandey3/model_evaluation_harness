"""
Verify failures classification from the evaluator
"""
import json

import pytest

from conversation.evaluators import evaluate_conversation
from conversation.scenarios import get_travel_planning_scenario

@pytest.mark.constraint_tracking
class TestConstraintTracking:
    def test_missing_cost_is_unverified_not_budget_violation(self):
        scenario = get_travel_planning_scenario()
        response = {
            "answer": "Here is your trip",
            "currency": "USD",
            "trip_days": 1
        }
        transcript = [
            {"role": "user", "content": "Plan me a trip under $500"},
            {"role": "assistant", "content": json.dumps(response)},
        ]

        result = evaluate_conversation(scenario, transcript)

        assert "unverifiable_cost" in result["failure_types"]
        assert "constraint_violation" not in result["failure_types"]

    def test_cost_above_scenario_budget_is_a_violation(self):
        response = {
          "answer": "A one-day trip for two",
          "currency": "USD",
          "cost_items": [
            {"item": "transportation", "amount": 400},
            {"item": "food", "amount": 250}
          ],
          "trip_days": 1
        }

        scenario = get_travel_planning_scenario()

        transcript = [
            {"role": "user", "content":"Plan me a one-day trip for two under $500"},
            {"role": "assistant",
             "content": json.dumps(response)
            }
        ]

        result = evaluate_conversation(scenario, transcript)
        failure_types = result['failure_types']


        # The get_travel_planning_scenario's binding budget is $500,
        # so the evaluator should record the
        # $650 total as evidence and classify the result as a constraint violation

        assert 'constraint_violation' in failure_types
        assert result["evidence"]["final_total_cost"] == 650
        assert result["scores"]["constraint_consistency"] is False

    def test_cost_below_scenario_budget_passes(self):
        response = {
          "answer": "A one-day trip for two",
          "currency": "USD",
          "cost_items": [
            {"item": "transportation", "amount": 100},
            {"item": "food", "amount": 250}
          ],
          "trip_days": 1
        }

        scenario = get_travel_planning_scenario()

        transcript = [
            {"role": "user", "content":"Plan me a one-day trip for two under $500"},
            {"role": "assistant",
             "content": json.dumps(response)
            }
        ]

        result = evaluate_conversation(scenario, transcript)
        failure_types = result['failure_types']


        # The get_travel_planning_scenario's binding budget is $500,
        # so the evaluator should record the
        # $350 total as evidence and raise no failure types

        assert failure_types == []
        assert result["evidence"]["final_total_cost"] == 350
        assert result["scores"]["constraint_consistency"]
