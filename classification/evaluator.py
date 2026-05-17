from sklearn.metrics import confusion_matrix

from classification import model
from classification.metrics import calculate_metrics
from classification.train import train_model
from classification.visualization import save_confusion_matrix


def evaluate():
    """
    Run classification evaluation pipeline.
    :return:
    """

    model, x_test, y_test = train_model()

    prediction = model.predict(x_test)

    results = calculate_metrics(
        y_test,
        prediction
    )

    confusion_matrix_path = save_confusion_matrix(
        y_test, prediction
    )
    results['artifacts'] = {
        "confusion_matrix": confusion_matrix_path
    }

    if results["precision"] == 0:
        print(
            "WARNING: One or more classes "
            "were never predicted."
        )

    if results["precision"] < 0.70:
        print(
            "WARNING: Low precision indicates "
            "high false positive rates."
        )

    return results
