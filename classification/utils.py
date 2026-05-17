from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split


def load_dataset():
    """

    :return:
    """
    dataset = load_digits()

    x_train, x_test, y_train, y_test = train_test_split(
        dataset.data,
        dataset.target,
        test_size=0.2,
        random_state=42
    )

    return x_train, x_test, y_train, y_test