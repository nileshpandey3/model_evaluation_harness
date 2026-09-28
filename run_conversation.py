from conversation.evaluators import evaluate_conversation
from conversation.runner import run_scenario
from conversation.scenarios import get_travel_planning_scenario
from shared.output_writer import write_json


def main():
    """
    Entry point for the live LLM evaluation:
    it runs the scenario, scores the model’s response,
    and writes the two JSON files that the Quarto report reads
    """
    scenario = get_travel_planning_scenario()

    transcript = run_scenario(scenario)

    results = evaluate_conversation(
        scenario,
        transcript,
    )

    write_json(
        "outputs/conversation_transcript.json",
        transcript,
    )

    write_json(
        "outputs/conversation_results.json",
        results,
    )

    print(results)


if __name__ == "__main__":
    main()
