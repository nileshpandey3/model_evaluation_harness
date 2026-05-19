from conversation.benchmark import run_benchmark
from conversation.scenarios import get_all_scenarios
from shared.output_writer import write_json



def main() -> None:
    scenarios = get_all_scenarios()

    benchmark_results = run_benchmark(scenarios)

    write_json(
        "outputs/benchmark_results.json",
        benchmark_results,
    )

    print(benchmark_results["summary"])


if __name__ == "__main__":
    main()
