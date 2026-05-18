
from conversation.llm_client import get_llm_response


def run_scenario(scenario):
    """
    Execute the scenario and return a transcript.
    """
    transcript = []

    for turn in scenario['turns']:
        transcript.append(turn)

        if turn['role'] == 'user':
            llm_response = get_llm_response(turn['content'])

            transcript.append(
                {
                    'role': 'ai-assistant',
                    'content': llm_response,
                    "metadata": {
                        # Replace with the actual total cost
                        # extracted or provided later.
                        "final_total_cost": 450,
                    },
                }
            )

    return transcript