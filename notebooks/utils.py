import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

import arviz as az
import pymc as pm


# def value_counts(series):
#     """Make a series of values and the number of times they appear.

#     Returns a DataFrame because they get rendered better in Jupyter.

#     series: Pandas Series

#     returns: Pandas DataFrame
#     """
#     series = series.value_counts(dropna=False).sort_index()
#     series.index.name = "values"
#     series.name = "counts"
#     return pd.DataFrame(series)


def value_counts(series, normalize=False):
    """Make a series of values and the number (or proportion) of times they appear.

    Returns a DataFrame because they get rendered better in Jupyter.

    series: Pandas Series
    normalize: If True, return proportions instead of counts

    returns: Pandas DataFrame
    """
    series_counts = series.value_counts(dropna=False, normalize=normalize).sort_index()
    series_counts.index.name = "values"
    series_counts.name = "proportion" if normalize else "counts"
    return pd.DataFrame(series_counts)


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


def joint_contour(x, y):
    """Plot a joint KDE contour plot.

    Args:
        x: sequence
        y: sequence
    """
    data = np.vstack([x, y])
    kde = gaussian_kde(data)

    xs = np.linspace(x.min(), x.max(), 101)
    ys = np.linspace(y.min(), y.max(), 101)
    X, Y = np.meshgrid(xs, ys, indexing="ij")

    positions = np.vstack([X.ravel(), Y.ravel()])
    kde_values = kde(positions).reshape(X.shape)
    plt.contour(X, Y, kde_values, cmap="Blues")


def load_idata_or_sample(
    model: pm.Model, filename: str, force_run: bool = False, **sample_options
) -> az.InferenceData:
    """
    Runs PyMC sampling and saves the results to a NetCDF file, or loads existing results from the file.

    Load existing idata if the file exists and force_run is False.
    Runs the sampler and saves the idata if the file doesn't exist or force_run is True.

    Args:
        model (pm.Model):
            The PyMC model object to sample from.
        filename (str):
            Path to the NetCDF file to save to or load from.
        force_run (bool):
            If true, run the sampler even if the file exists.
        **sample_options:
            Additional keyword arguments passed directly to `pm.sample()`.

    Returns:
        az.InferenceData:
            The idata (posterior samples) as an ArviZ InferenceData object.

    """
    if os.path.exists(filename) and not force_run:
        idata = az.from_netcdf(filename)
        print(f"Loaded idata from {filename}")
    else:
        with model:
            idata = pm.sample(**sample_options)

        az.to_netcdf(idata, filename)
        print(f"Saved new idata to {filename}")

    return idata


def round_into_bins(series, bin_width, low=0, high=None):
    """Rounds values down to the bin they belong in.

    series: pd.Series
    bin_width: number, width of the bins

    returns: array of bin values
    """
    if high is None:
        high = series.max()

    bins = np.arange(low, high + bin_width, bin_width)
    indices = np.digitize(series, bins)
    return bins[indices - 1]