# Publication quality figure settings
import matplotlib.pyplot as plt
# rcParams for matplotlib
plt.rcParams.update(
    {
        # Math text
        "mathtext.default": "regular",
        # Figure
        "figure.figsize": [4, 4],  # or [4, 6.4]
        "figure.dpi": 300,
        # Plot (lines and markers)
        "lines.linewidth": 3,
        "lines.markersize": 8,
        # Axes
        "axes.titlesize" : 16,
        "axes.titleweight": "bold",
        "axes.labelsize": 16,
        "axes.labelweight": "bold",
        "xtick.labelsize": 15,
        "ytick.labelsize": 15,
        "xtick.direction": "in",
        "ytick.direction": "in",
    }
)
