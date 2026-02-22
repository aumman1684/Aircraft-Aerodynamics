import os

# -------------------------------------------------------
# Locate files
# -------------------------------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))

input_file = os.path.join(script_dir, '7301_withflap.txt')
output_file = os.path.join(script_dir, 'NLR-7301_with_flap.dat')

# -------------------------------------------------------
# Read and clean geometry
# -------------------------------------------------------
clean_coords = []

with open(input_file, 'r') as file:
    lines = file.readlines()

for line in lines:

    if line.strip() == "":
        continue

    # Skip header
    if "x" in line.lower():
        continue

    values = line.split()

    if len(values) >= 2:
        try:
            x = float(values[0])
            y = float(values[1])

            # Skip separator line
            if abs(x - 999.9) < 1e-3:
                continue

            clean_coords.append((x, y))

        except:
            continue

# -------------------------------------------------------
# Write .dat file
# -------------------------------------------------------
with open(output_file, 'w') as f:
    f.write("NLR-7301 with 20deg Flap\n")
    for x, y in clean_coords:
        f.write(f"{x:.8f} {y:.8f}\n")

print(f"Saved file to: {output_file}")
print(f"Total points written: {len(clean_coords)}")