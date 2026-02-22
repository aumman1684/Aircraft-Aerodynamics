import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.ticker import MultipleLocator

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# File paths
file_10deg = os.path.join(
    script_dir,
    "NLR7301_with_flap_10degrees_cp_dist.txt"
)

file_15deg = os.path.join(
    script_dir,
    "NLR7301_with_flap_15degrees_cp_dist.txt"
)

print("Looking for:", file_10deg)
print("Exists:", os.path.exists(file_10deg))
print("Looking for:", file_15deg)
print("Exists:", os.path.exists(file_15deg))


def read_cp_distribution(file_path):
    data = []
    with open(file_path, "r") as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 3:
                try:
                    x_c = float(parts[0])     # first column
                    cp  = float(parts[-1])    # last column (Cp)
                    data.append([x_c, cp])
                except ValueError:
                    pass
    return np.array(data)


# Read both datasets
data_10 = read_cp_distribution(file_10deg)
data_15 = read_cp_distribution(file_15deg)

x10 = data_10[:, 0]
cp10 = data_10[:, 1]

x15 = data_15[:, 0]
cp15 = data_15[:, 1]


# Plot
fig, ax = plt.subplots(figsize=(9, 8))

ax.set_xlabel("x / c", fontsize=14, fontweight="bold")
ax.set_ylabel("Pressure coefficient Cp", fontsize=14, fontweight="bold")

# Red = 10°, Blue = 15°
ax.plot(x10, cp10, "r-", linewidth=2.5, label="Flap 10 degrees")
ax.plot(x15, cp15, "b-", linewidth=2.5, label="Flap 15 degrees")

# Cp convention
ax.invert_yaxis()

# Axis ticks and grid
ax.xaxis.set_major_locator(MultipleLocator(0.1))
ax.xaxis.set_minor_locator(MultipleLocator(0.02))
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(MultipleLocator(0.2))

ax.grid(True, which="major", alpha=0.5, linewidth=0.8)
ax.grid(True, which="minor", alpha=0.2, linewidth=0.4)

ax.tick_params(axis="both", which="major", labelsize=11)
ax.set_aspect("auto", adjustable="box")

ax.set_title(
    "Cp vs x/c – NLR7301 with flap at 10 and 15 degrees",
    fontsize=14,
    fontweight="bold"
)

ax.legend(fontsize=12)

fig.tight_layout()
plt.show()