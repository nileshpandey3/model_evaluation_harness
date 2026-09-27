from conversation.runner import run_scenario
from conversation.scenarios import get_travel_planning_scenario


def test_second_turn_receives_history():
    scenario = get_travel_planning_scenario()
    received_inputs = []
    responses = iter(["first_response", "second_response"])

    def fake_model(model_input):
        received_inputs.append(model_input)
        response = next(responses)
        return response

    transcript = run_scenario(scenario, model_call=fake_model)

    assert transcript[1]["content"] == "first_response"
    assert transcript[3]["content"] == "second_response"

    # Verify that the second prompt contains the first user request
    assert scenario["turns"][0]["content"] in received_inputs[1]

    assert len(received_inputs) == 2
    assert "first_response" in received_inputs[1]

    # Verify that transcript has no invented cost
    assert all("metadat" not in message for message in transcript)
