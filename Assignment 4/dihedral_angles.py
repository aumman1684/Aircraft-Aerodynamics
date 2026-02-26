import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

# Data
theta = np.array([10, 20, 30, 40, 50, 80])
cdi = np.array([0.0034595, 0.0034449, 0.0033961, 0.0033161, 0.0032149, 0.0061542])

# Plot
fig, ax = plt.subplots(figsize=(9, 8))

ax.set_xlabel("Theta [deg]", fontsize=14, fontweight="bold")
ax.set_ylabel("CDi", fontsize=14, fontweight="bold")

ax.plot(theta, cdi, "b-", linewidth=2.5, marker="o")

# X-axis ticks every 10 degrees
ax.xaxis.set_major_locator(MultipleLocator(10))

# Y-ticks: ensure only the first (maximum reference) value is explicitly included
max_cdi = cdi[0]
yticks = ax.get_yticks()
yticks = np.unique(np.append(yticks, max_cdi))
ax.set_yticks(yticks)

ax.grid(True, alpha=0.5)
ax.tick_params(axis="both", labelsize=11)
ax.set_aspect("auto", adjustable="box")

ax.set_title(
    "Induced Drag Coefficient (CDi) vs Dihedral Angle (Theta)",
    fontsize=14,
    fontweight="bold"
)

fig.tight_layout()
plt.show()