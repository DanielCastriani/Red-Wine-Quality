import os
from typing import Any
import pickle


def make_path(path: str, *args, file_name: str = None):
    path = os.path.join(path, *args)

    if not os.path.exists(path):
        os.makedirs(path)

    if file_name is not None:
        path = os.path.join(path, file_name)

    return path


def save_model(model: Any, path: str, file_name: str = 'model.pickle'):
    path = make_path(path, file_name=file_name)

    with open(path, 'wb') as f:
        pickle.dump(model, f)


def load_model(model: Any, path: str, file_name: str = 'model.pickle'):
    path = make_path(path, file_name=file_name)

    with open(path, 'rb') as f:
        return pickle.load(model, f)
