import os


def make_path(path: str, *args, file_name: str = None):
    path = os.path.join(path, *args)

    if not os.path.exists(path):
        os.makedirs(path)

    if file_name is not None:
        path = os.path.join(path, file_name)

    return path
