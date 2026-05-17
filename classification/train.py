from classification.model import build_model
from classification.utils import load_dataset


def train_model():
    """
    Train classification model
    :return:
    """
    x_train, x_test, y_train, y_test = load_dataset()
    model = build_model()

    model.fit(x_train, y_train)

    return model, x_test, y_test
