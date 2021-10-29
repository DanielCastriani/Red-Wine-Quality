from typing import Tuple, Union
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def ecdf_values(values: Union[np.ndarray, pd.Series]) -> Tuple[np.ndarray, np.ndarray]:

    x = np.sort(values)
    y = np.arange(1, len(x) + 1)/len(x)

    return x, y


def ecdf_plot(values: Union[np.ndarray, pd.Series], normal: bool = True, percentiles: bool = True, show: bool = True, ax: plt.Axes = None):

    if not ax:
        _, ax = plt.subplots(figsize=(10, 5))

    x, y = ecdf_values(values)

    if normal:
        mean = np.mean(x)
        std = np.std(x)
        samples = np.random.normal(mean, std, size=10000)
        tx, ty = ecdf_values(samples)
        ax.plot(tx, ty, color='red', label='Normal')

    if percentiles:
        ax.axvline(np.percentile(values, 1), color='#AAA', label='1 %', linestyle='--')
        ax.axvline(np.percentile(values, 25), color='#777', label='25 %', linestyle='--')
        ax.axvline(np.percentile(values, 50), color='#333', label='50 %', linestyle='--')
        ax.axvline(np.percentile(values, 75), color='#777', label='75 %', linestyle='--')
        ax.axvline(np.percentile(values, 99), color='#AAA', label='99 %', linestyle='--')

    ax.plot(x, y, marker='.', linestyle='none', color='blue', label='ECDF')

    ax.legend()

    if show:
        plt.show()
