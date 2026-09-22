# A multi-turn AI evaluation framework for adversarial robustness and conversational quality assessment

A production-style ML and AI evaluation framework for assessing multi-turn conversational AI systems.

This project demonstrates:

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
├── conversation/        # Multi-turn conversational AI evaluation
├── data/                # Datasets and scenario definitions
├── outputs/             # Generated JSON artifacts
├── reports/             # Quarto reports (HTML/PDF)
├── shared/              # Common utilities and configuration
├── tests/               # Automated tests
├── run_conversation.py
├── run_benchmark.py
└── Makefile
