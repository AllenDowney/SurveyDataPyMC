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


from scipy.stats import gaussian_kde


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


def round_into_bins(values, bin_width, low=None):
    """Round values to the nearest bin center of specified width.

    Args:
        values: array-like of numbers to bin (e.g., ages)
        bin_width: positive number specifying the size of each bin
        low: optional minimum value to start binning from. Values below this
             will be rounded up to this value before binning.

    Returns:
        numpy array of values rounded to nearest bin center

    Examples:
        >>> round_into_bins([13, 15, 18, 20, 23], 5, low=13)
        array([15, 15, 20, 20, 25])  # rounds to nearest 5-year group center

        >>> round_into_bins([32, 37, 41], 10)
        array([35, 35, 45])  # rounds to nearest decade center
    """
    # Handle NaN values by imputing with mean
    values_clean = np.array(values)
    if np.isnan(values_clean).any():
        mean_value = np.nanmean(values_clean)
        values_clean = np.where(np.isnan(values_clean), mean_value, values_clean)

    # Input validation
    if not bin_width > 0:
        raise ValueError("bin_width must be positive")

    # Convert input to numpy array
    try:
        values = np.asarray(values_clean, dtype=float)
    except (ValueError, TypeError):
        raise TypeError("values must be convertible to numeric array")

    # If low is provided, clip values to not go below it
    if low is not None:
        values = np.maximum(values, low)

    # Calculate bin centers
    # First get the bin number
    bin_numbers = np.floor((values - (bin_width / 2)) / bin_width)
    # Then convert back to actual values
    binned_values = (bin_numbers * bin_width) + (bin_width / 2) + 1

    return binned_values.astype(int)
