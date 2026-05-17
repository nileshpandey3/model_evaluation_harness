from classification.evaluator import evaluate
from shared.output_writer import write_json


def main():
    results = evaluate()
    print("Classification Results: ", results)
    write_json(
        "outputs/classification_results.json",
        results
    )
    print("Classification evaluation complete.")
    print("Artifacts written to outputs/")

if __name__ == "__main__":
    main()