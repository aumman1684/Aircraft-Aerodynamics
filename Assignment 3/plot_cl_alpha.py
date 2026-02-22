import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.ticker import MultipleLocator

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

file_clean = os.path.join(script_dir, "NLR7301_cl_alpha")
file_flap  = os.path.join(script_dir, "NLR7301_with_flap_10degrees_cl_alpha")

def load_alpha_cl(filepath):
    data = []
    with open(filepath, "r") as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 2:
                try:
                    data.append([float(parts[0]), float(parts[1])])
                except ValueError:
                    pass
    return np.array(data)

data_clean = load_alpha_cl(file_clean)
data_flap  = load_alpha_cl(file_flap)

alpha_clean = data_clean[:, 0]
cl_clean    = data_clean[:, 1]

alpha_flap  = data_flap[:, 0]
cl_flap     = data_flap[:, 1]

# Plot: Cl vs Alpha (line graphs)
fig, ax = plt.subplots(figsize=(9, 8))

ax.set_xlabel("Alpha (degrees)", fontsize=14, fontweight="bold")
ax.set_ylabel("Cl", fontsize=14, fontweight="bold")

ax.plot(alpha_clean, cl_clean, "b-",
        linewidth=2.5, label="Airfoil with no flap")

ax.plot(alpha_flap, cl_flap, "r-",
        linewidth=2.5, label="Airfoil with flap, 10 degrees")

# Axis increments = 2
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(0.2))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))

# Grid styling
ax.grid(True, which="major", alpha=0.5, linewidth=0.8)
ax.grid(True, which="minor", alpha=0.2, linewidth=0.4)

ax.legend(fontsize=13, loc="best")
ax.tick_params(axis="both", which="major", labelsize=11)
ax.set_aspect("auto", adjustable="box")

ax.set_title("Cl vs Alpha – NLR7301",
             fontsize=14, fontweight="bold")

fig.tight_layout()
plt.show()