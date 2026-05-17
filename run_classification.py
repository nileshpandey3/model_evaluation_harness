from classification.evaluator import evaluate
from shared.output_writer import write_json


def main():
    results = evaluate()
    print(results)
    write_json(
        "outputs/classification_results.json",
        results
    )

if __name__ == "__main__":
    main()