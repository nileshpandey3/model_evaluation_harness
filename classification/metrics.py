from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, classification_report, balanced_accuracy_score, log_loss,
    top_k_accuracy_score)



def calculate_metrics(y_true, y_pred, y_proba):
    """
    Compute Evaluation metrics
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
        ),
        "balanced_accuracy": round(
            balanced_accuracy_score(y_true, y_pred), 3
        ),
        "log_loss": round(
            log_loss(y_true, y_proba), 3
        ),
        "top_3_accuracy": round(
            top_k_accuracy_score(y_true, y_proba, k=3), 3
        ),
    }
