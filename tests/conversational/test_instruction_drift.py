import json

import pytest

from conversation.evaluators import evaluate_conversation
from conversation.scenarios import get_travel_planning_scenario

@pytest.mark.instruction_drift
class TestInstructionDrift:

    def test_multi_turn_consistency(self):
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
        expected_trip_days = result['evidence']['expected_trip_days']
        actual_trip_days = result['evidence']['actual_trip_days']

        assert 'multi_turn_consistency' in result['scores']
        assert expected_trip_days == actual_trip_days

    def test_multi_turn_consistency_fail(self):
        scenario = get_travel_planning_scenario()
        response = {
            "answer": "Here is your trip",
            "currency": "USD",
            "trip_days": 5
        }
        transcript = [
            {"role": "user", "content": "Plan me a trip under $500"},
            {"role": "assistant", "content": json.dumps(response)},
        ]

        result = evaluate_conversation(scenario, transcript)

        assert not result['scores']['multi_turn_consistency']
        assert 'duration_mismatch' in result['failure_types']

    def test_multi_turn_consistency_invalid_duration(self):
        scenario = get_travel_planning_scenario()
        response = {
            "answer": "Here is your trip",
            "currency": "USD",
            "trip_days": "invalid"
        }
        transcript = [
            {"role": "user", "content": "Plan me a trip under $500"},
            {"role": "assistant", "content": json.dumps(response)},
        ]

        result = evaluate_conversation(scenario, transcript)

        assert result["scores"]["multi_turn_consistency"] is None
        assert 'unverifiable_duration' in result['failure_types']
