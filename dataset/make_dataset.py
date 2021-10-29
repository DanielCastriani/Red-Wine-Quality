import pandas as pd


def make_dataset():
    red_wine_df = pd.read_csv('data/winequality-red.csv')

    red_wine_df.columns = [c.replace(' ', '_') for c in red_wine_df.columns]

    return red_wine_df
