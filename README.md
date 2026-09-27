# An AI evaluation framework for assessing multi-turn conversational AI systems


This project demonstrates:

- Multi-turn conversational AI evaluation
- Constraint consistency and instruction-following analysis
- Automated HTML reporting
- Local open-source LLM evaluation using Ollama

---

## Architecture Overview

```text
model_evaluation_harness/
├── conversation/        # Multi-turn conversational AI evaluation
├── outputs/             # Generated JSON artifacts
├── reports/             # Quarto reports (HTML)
├── tests/               # Automated tests
├── run_conversation.py
└── Makefile
