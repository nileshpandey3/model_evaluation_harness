.PHONY: install conversation conversation-report benchmark benchmark-report benchmark-all conversation-all

install:
	pip install --upgrade pip
	pip install -r requirements.txt

conversation:
	python run_conversation.py

conversation-report:
	quarto render reports/conversation_report.qmd

conversation-all: conversation conversation-report
