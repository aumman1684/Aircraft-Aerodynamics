import os
import matplotlib.pyplot as plt


def read_7301_withflap(filename):
    """Read the 7301_withflap.txt format: header then pairs; 999.9 sentinel separates sections."""
    sections = []
    current = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            if i == 0:
                # skip header like 'x y'
                continue
            s = line.strip()
            if not s:
                continue
            parts = s.split()
            if len(parts) < 2:
                continue
            try:
                x = float(parts[0])
                y = float(parts[1])
            except ValueError:
                continue
            # sentinel
            if abs(x - 999.9) < 1e-6 and abs(y - 999.9) < 1e-6:
                if current:
                    sections.append(current)
                current = []
                continue
            current.append((x, y))
    if current:
        sections.append(current)
    return sections


def plot_and_print(filename):
    sections = read_7301_withflap(filename)
    name = os.path.basename(filename)

    fig, ax = plt.subplots(figsize=(8, 6))
    for sec in sections:
        xs = [p[0] for p in sec]
        ys = [p[1] for p in sec]
        ax.plot(xs, ys, 'k-', linewidth=1.8)

    ax.set_title(name)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(alpha=0.3)
    ax.set_aspect('equal')
    plt.tight_layout()

    plt.show()

    # print geometry summary
    total = sum(len(s) for s in sections)
    print('='*70)
    print(f'FILE: {name}')
    for i, sec in enumerate(sections, 1):
        print(f'  section {i}: {len(sec)} points')
    print(f'  Total points: {total}')
    print('='*70)

    # print coordinates (first and last 10 of each section to avoid flooding)
    for i, sec in enumerate(sections, 1):
        print(f'\nSECTION {i} (showing first/last 10 of {len(sec)}):')
        print(f"Index    x{' '*6} y")
        for j, (x, y) in enumerate(sec[:10]):
            print(f"{j:<6} {x:12.8f} {y:12.8f}")
        if len(sec) > 20:
            print('   ...')
            for j, (x, y) in enumerate(sec[-10:], start=len(sec)-10):
                print(f"{j:<6} {x:12.8f} {y:12.8f}")

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    infile = os.path.join(script_dir, 'NLR 7301 with flap')
    plot_and_print(infile)
