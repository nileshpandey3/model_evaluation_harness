import json


def write_json(path, data):
    """
    Persist evaluation results to JSON.
    """
    with open(path, "w") as file:
        json.dump(data, file, indent=2)
