# A multi-turn AI evaluation framework for adversarial robustness and conversational quality assessment


## Overview
Evaluation-focused ML/AI project exploring:
- classification metrics tradeoffs
- qualitative failure analysis
- adversarial testing
- multi-turn conversational AI evaluation

---

## Features

### Classification Evaluation
- Accuracy
- Precision
- Recall
- F1
- Confusion Matrix

### Conversational AI Evaluation
- Multi-turn session evaluation
- Prompt injection testing
- Constraint consistency checking
- Adversarial resistance scoring

---

## Tech Stack
- Python
- scikit-learn
- Streamlit
- Ollama/OpenAI

---

## Example Insights
- High accuracy masked poor minority-class detection
- Prompt injection caused instruction drift in multi-turn sessions

---

## Running The Project

### Install
pip install -r requirements.txt

### Run classification evaluation
python classification/evaluate.py

### Run conversational evaluation
python conversational/runner.py

### Launch dashboard
streamlit run dashboard/app.py