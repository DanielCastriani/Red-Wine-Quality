import mlflow


def create_experiment(name: str):
    exp = mlflow.get_experiment_by_name(name)

    if exp is None:
        mlflow.create_experiment(name)

    exp = mlflow.get_experiment_by_name(name)

    return exp
