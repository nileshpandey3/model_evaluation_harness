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

all: install classification conversation report
conversation-all: conversation conversation-report