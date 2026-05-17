from pathlib import Path

import pandas as pd
from evidently import Report
from evidently.presets import ClassificationPreset

def generate_evidently_report(x_test, y_test, predictions):
    """
    Generate an interactive classification report using Evidently.
    """

    # Build a tabular dataset for Evidently
    report_data = pd.DataFrame(x_test)
    report_data['target'] = y_test
    report_data['prediction'] = predictions

    report = Report(
        metrics=[ClassificationPreset()]
    )

    report.run(
        current_data=report_data,
        reference_data=None
    )

    # Save the report
    output_path = "outputs/evidently_classification_report.html"
    report.save(output_path)

    return output_path



