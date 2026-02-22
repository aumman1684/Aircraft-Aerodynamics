import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.ticker import MultipleLocator

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Exact filename
file_path = os.path.join(
    script_dir,
    "NLR7301_with_flap_10degrees_cp_dist.txt"
)

print("Looking for:", file_path)
print("Exists:", os.path.exists(file_path))

# Read Cp distribution (handles headers, multiple elements)
data = []
with open(file_path, "r") as f:
    for line in f:
        parts = line.split()
        if len(parts) >= 3:
            try:
                x_c = float(parts[0])     # leftmost column
                cp  = float(parts[-1])    # rightmost column
                data.append([x_c, cp])
            except ValueError:
                pass

data = np.array(data)

x_c = data[:, 0]
cp  = data[:, 1]

# Plot: Cp vs x/c
fig, ax = plt.subplots(figsize=(9, 8))

ax.set_xlabel("x / c", fontsize=14, fontweight="bold")
ax.set_ylabel("Pressure coefficient Cp", fontsize=14, fontweight="bold")

ax.plot(x_c, cp, "r-", linewidth=2.5)

# Cp convention
ax.invert_yaxis()

# Axis ticks and grid (matched style)
ax.xaxis.set_major_locator(MultipleLocator(0.1))
ax.xaxis.set_minor_locator(MultipleLocator(0.02))
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(MultipleLocator(0.2))

ax.grid(True, which="major", alpha=0.5, linewidth=0.8)
ax.grid(True, which="minor", alpha=0.2, linewidth=0.4)

ax.tick_params(axis="both", which="major", labelsize=11)
ax.set_aspect("auto", adjustable="box")

ax.set_title("Cp vs x/c – NLR7301 with flap at 10 degrees",
             fontsize=14, fontweight="bold")

fig.tight_layout()
plt.show()