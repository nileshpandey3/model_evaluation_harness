.PHONY: classification report all

install:
	pip install --upgrade pip
	pip install -r requirements.txt

classification:
	python run_classification.py

conversation:
	python run_conversation.py

conversation-report:
	quarto render reports/conversation_report.qmd

report:
	quarto render reports/classification_report.qmd

benchmark:
	python run_benchmark.py

benchmark-report:
	quarto render reports/benchmark_report.qmd

benchmark-all: benchmark benchmark-report


conversation-all: conversation conversation-report
classification-all: install classification report