from sklearn.metrics import (
    accuracy_score,precision_score, recall_score, f1_score, classification_report)



def calculate_metrics(y_true, y_pred):
    """
    Compute Evaluation metrics
    :param y_true:
    :param y_pred:
    :return:
    """

    return {
        "accuracy": round(
            accuracy_score(y_true, y_pred),
            3
        ),
        "precision": round(
            precision_score(y_true, y_pred, average="weighted", zero_division=0),
            3
        ),
        "recall": round(
            recall_score(y_true, y_pred, average="weighted", zero_division=0),
            3
        ),
        "f1": round(
            f1_score(y_true, y_pred, average="weighted", zero_division=0),
            3
        ),
        "per_class_report": classification_report(
            y_true, y_pred, zero_division=0, output_dict=True
        )
    }
