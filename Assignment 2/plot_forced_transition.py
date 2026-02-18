import numpy as np
import matplotlib.pyplot as plt

cd = [0.01326, 0.01201 , 0.01090, 0.00998, 0.00923, 0.00918, 0.00918 , 0.00918 , 0.00918 ,0.00918  ] 
xtr= [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

# Create the plot
from matplotlib.ticker import MultipleLocator

fig, ax = plt.subplots(figsize=(9, 8))

ax.plot(xtr, cd, 'b-o', linewidth=2.5, markersize=8)

ax.set_xlabel('Transition Location (xtr/c)', fontsize=14, fontweight='bold')
ax.set_ylabel('CD', fontsize=14, fontweight='bold')

# Set axis limits and locators
ax.set_xlim(0, 1.1)
ax.set_ylim(0.008, 0.015)
ax.xaxis.set_major_locator(MultipleLocator(0.1))
ax.xaxis.set_minor_locator(MultipleLocator(0.02))
ax.yaxis.set_major_locator(MultipleLocator(0.001))
ax.yaxis.set_minor_locator(MultipleLocator(0.0002))

ax.grid(True, which='major', alpha=0.5, linewidth=0.8)
ax.grid(True, which='minor', alpha=0.2, linewidth=0.4)
ax.tick_params(axis='both', which='major', labelsize=11)
ax.set_title('Cd vs Transition Location at Cl = 0.4 - NACA 2623', fontsize=14, fontweight='bold')

fig.tight_layout()
plt.show()

