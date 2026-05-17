from classification import model
from classification.metrics import calculate_metrics
from classification.train import train_model


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