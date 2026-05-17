from pathlib import Path

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix


def save_confusion_matrix(y_true, y_pred):
    """
    Generate and save confusion matrix image.
    """
    matrix = confusion_matrix(y_true, y_pred)
    display = ConfusionMatrixDisplay(confusion_matrix=matrix)
    display.plot()

    output_path = Path("outputs/confusion_matrix.png")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(output_path, bbox_inches="tight")
    plt.close()

    return str(output_path)

