import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib.ticker import MultipleLocator
import numpy as np

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Excel file path
file_path = os.path.join(script_dir, "cdi_cant_angle2.xlsx")

# Read Excel (no header)
df = pd.read_excel(file_path, header=None)

# Rows 4–14 -> indices 3–13
# Column B -> index 1 (phi angle), Column K -> index 10 (CDi)
phi = df.iloc[3:14, 1].to_numpy()
cdi = df.iloc[3:14, 10].to_numpy()

# Plot
fig, ax = plt.subplots(figsize=(9, 8))

ax.set_xlabel("Phi [deg]", fontsize=14, fontweight="bold")
ax.set_ylabel("CDi", fontsize=14, fontweight="bold")

ax.plot(phi, cdi, "b-", linewidth=2.5, marker="o")

# X-axis ticks every 10 units
ax.xaxis.set_major_locator(MultipleLocator(10))

# Ensure only the maximum CDi (first value) is added, remove 0.003350 if present
max_cdi = cdi[0]
yticks = ax.get_yticks()
yticks = yticks[np.abs(yticks - 0.003350) > 1e-9]
yticks = np.unique(np.append(yticks, max_cdi))
ax.set_yticks(yticks)

ax.grid(True, alpha=0.5)
ax.tick_params(axis="both", labelsize=11)
ax.set_aspect("auto", adjustable="box")

ax.set_title(
    "Induced Drag Coefficient (CDi) vs Cant Angle (phi)",
    fontsize=14,
    fontweight="bold"
)

fig.tight_layout()
plt.show()