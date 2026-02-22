import matplotlib.pyplot as plt
import numpy as np
import os

def read_airfoil_dat(filename):
    """Read airfoil coordinates from a DAT file."""
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # Skip header lines
    name = lines[0].strip()
    params = lines[1].strip()
    
    # Parse coordinates
    data = []
    for i in range(2, len(lines)):
        line = lines[i].strip()
        if line:  # Skip empty lines
            parts = line.split()
            if len(parts) >= 2:
                try:
                    x = float(parts[0])
                    y = float(parts[1])
                    data.append((x, y))
                except ValueError:
                    continue
    
    # Separate upper and lower surfaces
    # Assuming first half is upper surface, second half is lower surface
    n_coords = len(data) // 2
    upper = data[:n_coords]
    lower = data[n_coords:]
    
    return name, upper, lower

def plot_airfoil(filename, save_filename=None):
    """Plot the airfoil shape and optionally save it."""
    name, upper, lower = read_airfoil_dat(filename)
    
    # Extract x and y coordinates
    upper_x, upper_y = zip(*upper) if upper else ([], [])
    lower_x, lower_y = zip(*lower) if lower else ([], [])
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Plot upper surface
    ax.plot(upper_x, upper_y, 'k-', linewidth=2.5)
    
    # Plot lower surface
    ax.plot(lower_x, lower_y, 'k-', linewidth=2.5)
    
    # Plot settings
    ax.set_xlabel('Chord (x/c)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Thickness (y/c)', fontsize=13, fontweight='bold')
    ax.set_title('NLR 7301 Airfoil', fontsize=15, fontweight='bold')
    ax.grid(True, alpha=0.4, linestyle='--')
    ax.set_aspect('equal')
    
    plt.tight_layout()
    
    # Save if filename provided
    if save_filename:
        plt.savefig(save_filename, dpi=150, bbox_inches='tight')
        print(f"✓ Plot saved to {save_filename}\n")
    
    # Display the plot
    plt.show()
    
    return name, upper, lower

def print_airfoil_geometry(name, upper, lower):
    """Print the airfoil geometry coordinates."""
    print("=" * 80)
    print(f"AIRFOIL GEOMETRY: {name}")
    print("=" * 80)
    
    print(f"\nUPPER SURFACE ({len(upper)} points):")
    print(f"{'Index':<8} {'x/c':<15} {'y/c':<15}")
    print("-" * 40)
    for i, (x, y) in enumerate(upper):
        print(f"{i:<8} {x:<15.6f} {y:<15.6f}")
    
    print(f"\n\nLOWER SURFACE ({len(lower)} points):")
    print(f"{'Index':<8} {'x/c':<15} {'y/c':<15}")
    print("-" * 40)
    for i, (x, y) in enumerate(lower):
        print(f"{i:<8} {x:<15.6f} {y:<15.6f}")
    
    print("\n" + "=" * 80)
    print(f"Total points: {len(upper) + len(lower)}")
    print("=" * 80)

if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dat_file = os.path.join(script_dir, "NLR-7301 AIRFOIL.dat")
    save_file = os.path.join(script_dir, "NLR7301_Airfoil.png")
    
    # Plot the airfoil
    name, upper, lower = plot_airfoil(dat_file, save_filename=save_file)
    
    # Print the airfoil geometry
    print_airfoil_geometry(name, upper, lower)

