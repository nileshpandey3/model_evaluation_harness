from conversation.llm_client import get_llm_response

def build_prompt(scenario:dict, transcript:list[dict])->str:
    """
    Include the scenario budget and conversation history in the model prompt
    """
    budget = scenario["constraint"]["value"]
    currency = scenario["constraint"]["currency"]
    history = []

    for message in transcript:
        history.append(
            f"{message['role']}:{message['content']}"
        )

    conversation = "\n".join(history)
    return (
        f"Keep the total trip cost within {budget} {currency}.\n"
        "Follow the latest user's requested trip duration while retaining "
        "the original budget.\n"
        "Return ONLY valid JSON, without Markdown or extra text.\n"
        'Include "answer", numeric "trip_days", "currency", and a nonempty '
        '"cost_items" list in every response.\n'
        'Each cost item must have "item" and numeric "amount".\n'
        "Choose one travel mode and include every selected expense for both travelers.\n"
        "Do not put alternative prices or ranges in cost_items.\n"
        "If a required expense cannot be estimated, say so in answer "
        "and do not invent a price.\n"
        'Include "answer", numeric "trip_days", "currency", '
        'and a nonempty "cost_items" list.\n'
        f"Conversation:\n{conversation}\n"
        "assistant:"
    )

def run_scenario(scenario,model_call=get_llm_response):
    """
    Execute the scenario and return a transcript.
    """
    transcript = []

    for turn in scenario['turns']:
        transcript.append(turn)

        prompt = build_prompt(scenario, transcript)

        if turn['role'] == 'user':
            llm_response = model_call(prompt)

            transcript.append(
                {
                    'role': 'assistant',
                    'content': llm_response,
                }
            )

    return transcript
