.PHONY: install conversation conversation-report benchmark benchmark-report benchmark-all conversation-all

install:
	pip install --upgrade pip
	pip install -r requirements.txt

conversation:
	python run_conversation.py

conversation-report:
	quarto render reports/conversation_report.qmd

benchmark:
	python run_benchmark.py

benchmark-report:
	quarto render reports/benchmark_report.qmd

benchmark-all: benchmark benchmark-report

conversation-all: conversation conversation-report
