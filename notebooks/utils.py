import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def value_counts(series):
    """Make a series of values and the number of times they appear.

    Returns a DataFrame because they get rendered better in Jupyter.

    series: Pandas Series

    returns: Pandas DataFrame
    """
    series = series.value_counts(dropna=False).sort_index()
    series.index.name = "values"
    series.name = "counts"
    return pd.DataFrame(series)


def underride(d, **options):
    """Add key-value pairs to d only if key is not in d.

    d: dictionary
    options: keyword args to add to d
    """
    for key, val in options.items():
        d.setdefault(key, val)

    return d


class SuppressWarning:
    def __enter__(self):
        warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")

    def __exit__(self, exc_type, exc_value, traceback):
        warnings.filterwarnings("default", category=UserWarning, module="matplotlib")


def decorate(**options):
    """Decorate the current axes.

    Call decorate with keyword arguments like
    decorate(title='Title',
             xlabel='x',
             ylabel='y')

    The keyword arguments can be any of the axis properties
    https://matplotlib.org/api/axes_api.html
    """
    ax = plt.gca()
    ax.set(**options)

    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(handles, labels)

    with SuppressWarning():
        plt.tight_layout()
