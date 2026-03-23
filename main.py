# ⚠️ This Files uses Jupyter in File Cells instead of a real Notebook

# %% Imports
import random

import numpy as np

# import numpy as np
from matplotlib import pyplot as plt

# %% Equations


# random Value
def true_random(min=0, max=100, step=1):
    return random.SystemRandom().choice(range(min, max, step))


# Gaussion Normal Distribution


# %% Plot
##### True Random Histogram
result_true_random = []
true_random_x = range(0, 10000)
for x in true_random_x:
    result_true_random.append(true_random())

fig, ax = plt.subplots()

ax.hist(result_true_random, bins=8, linewidth=0.5, edgecolor="white")

plt.show()
