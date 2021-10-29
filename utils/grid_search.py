import pandas as pd

from itertools import product

from typing import Any, Dict, List


def generate_combination(grid_parameters: Dict[str, List[Any]]):
    combinations = product(*grid_parameters.values())

    configs = [dict(zip(grid_parameters, v)) for v in combinations]

    return configs

