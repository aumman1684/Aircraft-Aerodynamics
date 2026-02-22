import matplotlib.pyplot as plt
import numpy as np
import os

def read_airfoil_txt(filename):
    """
    Read multi-element airfoil coordinates from txt file.
    Splits main element and flap using 999.9 separator.
    """
    main_coords = []
    flap_coords = []

    section = "main"

    with open(filename, 'r') as f:
        lines = f.readlines()

    # Skip header if present
    if "x" in lines[0].lower():
        lines = lines[1:]

    for line in lines:
        parts = line.strip().split()
        if len(parts) < 2:
            continue

        x = float(parts[0])
        y = float(parts[1])

        # Separator between elements
        if abs(x - 999.9) < 1e-3:
            section = "flap"
            continue

        if section == "main":
            main_coords.append((x, y))
        else:
            flap_coords.append((x, y))

    return main_coords, flap_coords


def split_upper_lower(coords):
    """
    Split into upper and lower surfaces.
    Detect leading edge as minimum x.
    """
    xs = np.array([p[0] for p in coords])
    le_index = np.argmin(xs)

    upper = coords[:le_index+1]
    lower = coords[le_index+1:]

    return upper, lower


def plot_airfoil_txt(filename):

    main_coords, flap_coords = read_airfoil_txt(filename)

    main_upper, main_lower = split_upper_lower(main_coords)
    flap_upper, flap_lower = split_upper_lower(flap_coords)

    fig, ax = plt.subplots(figsize=(14, 6))

    # Main element
    ax.plot(*zip(*main_upper), 'k-', linewidth=2.5)
    ax.plot(*zip(*main_lower), 'k-', linewidth=2.5)

    # Flap element
    ax.plot(*zip(*flap_upper), 'r-', linewidth=2.5)
    ax.plot(*zip(*flap_lower), 'r-', linewidth=2.5)

    ax.set_xlabel('Chord (x/c)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Thickness y/c', fontsize=13, fontweight='bold')
    ax.set_title('NLR 7301 Airfoil with Flap', fontsize=15, fontweight='bold')

    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.4)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    script_dir = os.path.dirname(os.path.abspath(__file__))
    txt_file = os.path.join(script_dir, "7301_withflap.txt")

    plot_airfoil_txt(txt_file)