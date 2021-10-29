import matplotlib.pyplot as plt
import pandas as pd
import shap
from sklearn.ensemble._forest import BaseForest

from utils.file_utils import make_path


def feature_importance(model: BaseForest, x: pd.DataFrame):
    fi = pd.DataFrame([x.columns, model.feature_importances_]).T
    fi.columns = ['Feature', 'Importance']
    fi = fi.sort_values('Importance', ascending=False)

    fi_path = make_path('results/', file_name='fi.csv')
    fi.to_csv(fi_path, index=False)

    return fi_path


def shap_report(model: BaseForest, x: pd.DataFrame, show: bool = True):
    explainer = shap.Explainer(model)
    shap_values = explainer(x)
    
    plt.plot()

    shap.plots.beeswarm(shap_values, show=False)

    shap_path = make_path('result/', file_name='shap.png')

    plt.savefig(shap_path)

    if show:
        plt.show()

    return shap_path
