from conversation.evaluators import evaluate_conversation
from conversation.runner import run_scenario
from conversation.scenarios import travel_planning_scenario
from shared.output_writer import write_json


def main():
    scenario = travel_planning_scenario()

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