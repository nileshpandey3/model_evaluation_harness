import pandas as pd
from evidently import Report
from evidently.presets import DataSummaryPreset


def generate_evidently_report(transcript: list[dict]) -> str:
    """
    Generate a simple Evidently report summarizing a conversation.
    """
    data = pd.DataFrame(transcript)

    report = Report(
        metrics=[DataSummaryPreset()]
    )

    report.run(
        current_data=data,
        reference_data=None,
    )

    output_path = (
        "outputs/evidently_conversation_report.html"
    )

    report.save(output_path)  # type: ignore[attr-defined]

    return output_path