.PHONY: classification report all

install:
	pip install --upgrade pip
	pip install -r requirements.txt

classification:
	python run_classification.py

report:
	quarto render reports/classification_report.qmd

all: install classification report