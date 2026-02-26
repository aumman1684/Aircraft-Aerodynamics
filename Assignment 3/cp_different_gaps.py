import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.ticker import MultipleLocator

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# File paths
file_original = os.path.join(
    script_dir,
    "NLR7301_with_flap_10degrees_cp_dist.txt"
)

file_gap2 = os.path.join(
    script_dir,
    "NLR7301_with_flap_10degrees_2pgap_cp_dist"
)

print("Original exists:", os.path.exists(file_original))
print("2% gap exists:", os.path.exists(file_gap2))


def read_cp_distribution(file_path):
    data = []
    with open(file_path, "r") as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 3:
                try:
                    x_c = float(parts[0])
                    cp  = float(parts[-1])
                    data.append([x_c, cp])
                except ValueError:
                    pass
    return np.array(data)


# Read data
data_orig = read_cp_distribution(file_original)
data_gap2 = read_cp_distribution(file_gap2)

x_orig = data_orig[:, 0]
cp_orig = data_orig[:, 1]

x_gap2 = data_gap2[:, 0]
cp_gap2 = data_gap2[:, 1]


# Plot
fig, ax = plt.subplots(figsize=(9, 8))

ax.set_xlabel("x / c", fontsize=14, fontweight="bold")
ax.set_ylabel("Pressure coefficient Cp", fontsize=14, fontweight="bold")

ax.plot(x_orig, cp_orig, "r-", linewidth=2.5, label="Original gap")
ax.plot(x_gap2, cp_gap2, "b-", linewidth=2.5, label="+2% flap gap")

ax.invert_yaxis()

ax.xaxis.set_major_locator(MultipleLocator(0.1))
ax.xaxis.set_minor_locator(MultipleLocator(0.02))
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(MultipleLocator(0.2))

ax.grid(True, which="major", alpha=0.5, linewidth=0.8)
ax.grid(True, which="minor", alpha=0.2, linewidth=0.4)

ax.tick_params(axis="both", which="major", labelsize=11)
ax.set_aspect("auto", adjustable="box")

ax.set_title(
    "Cp vs x/c – NLR7301 with flap at 10 degrees (Original vs +2% Gap)",
    fontsize=14,
    fontweight="bold"
)

ax.legend(fontsize=12)

fig.tight_layout()
plt.show()