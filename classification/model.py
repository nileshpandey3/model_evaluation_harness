from sklearn.ensemble import RandomForestClassifier


def build_model():
    """
    Build an interpretable classifier
    """
    return RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

