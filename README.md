# A multi-turn AI evaluation framework for adversarial robustness and conversational quality assessment

A production-style ML and AI evaluation framework for assessing both traditional machine learning models and multi-turn conversational AI systems.

This project demonstrates:

- Classical ML evaluation (classification metrics and diagnostics)
- Multi-turn conversational AI evaluation
- Adversarial and prompt injection testing
- Constraint consistency and instruction-following analysis
- Aggregate benchmark scoring
- Automated HTML/PDF reporting
- Local open-source LLM evaluation using Ollama

---

## Architecture Overview

```text
model_evaluation_harness/
├── classification/      # Traditional ML evaluation pipeline
├── conversation/        # Multi-turn conversational AI evaluation
├── data/                # Datasets and scenario definitions
├── docs/                # Architecture and methodology notes
├── outputs/             # Generated JSON artifacts
├── reports/             # Quarto reports (HTML/PDF)
├── shared/              # Common utilities and configuration
├── tests/               # Automated tests(TODO)
├── run_classification.py
├── run_conversation.py
├── run_benchmark.py
└── Makefile

