import numpy as np
import matplotlib.pyplot as plt

############################
# GRID
############################

x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)
X, Y = np.meshgrid(x, y)

phi = np.zeros_like(X)
psi = np.zeros_like(X)
u = np.zeros_like(X)
v = np.zeros_like(X)

U_ref = None
doublet_strength = None
doublet_center = (0.0, 0.0)

############################
# FLOW TYPES
############################

def uniform(U, alpha):
    global phi, psi, u, v, U_ref
    U_ref = U
    phi += U*(X*np.cos(alpha) + Y*np.sin(alpha))
    psi += U*(Y*np.cos(alpha) - X*np.sin(alpha))
    u += U*np.cos(alpha)
    v += U*np.sin(alpha)

def source(strength, x0, y0):
    global phi, psi, u, v
    dx = X - x0
    dy = Y - y0
    r2 = dx**2 + dy**2
    r2[r2 == 0] = 1e-16
    r = np.sqrt(r2)

    phi += strength/(2*np.pi)*np.log(r)
    psi += strength/(2*np.pi)*np.arctan2(dy, dx)

    u += strength/(2*np.pi)*(dx/r2)
    v += strength/(2*np.pi)*(dy/r2)

def vortex(strength, x0, y0):
    global phi, psi, u, v
    dx = X - x0
    dy = Y - y0
    r2 = dx**2 + dy**2
    r2[r2 == 0] = 1e-16

    phi -= strength/(2*np.pi)*np.arctan2(dy, dx)
    psi += strength/(2*np.pi)*np.log(np.sqrt(r2))

    u -= strength/(2*np.pi)*(dy/r2)
    v += strength/(2*np.pi)*(dx/r2)

def doublet(strength, x0, y0):
    global phi, psi, u, v, doublet_strength, doublet_center
    doublet_strength = strength
    doublet_center = (x0, y0)

    dx = X - x0
    dy = Y - y0
    r2 = dx**2 + dy**2
    r2[r2 == 0] = 1e-16
    r = np.sqrt(r2)
    theta = np.arctan2(dy, dx)

    phi += strength/(2*np.pi)*(np.cos(theta)/r)
    psi -= strength/(2*np.pi)*(np.sin(theta)/r)

    r4 = r2**2
    u -= strength/(2*np.pi)*((dx**2 - dy**2)/r4)
    v -= strength/(2*np.pi)*(2*dx*dy/r4)

############################
# USER INPUT
############################

print("Enter canonical flows:")
print("1: uniform")
print("2: source/sink")
print("3: vortex")
print("4: doublet")
print("Type 'done' to finish.\n")

while True:
    flow_type = input("Enter flow type: ")

    if flow_type.lower() == "done":
        break

    if flow_type in ["1", "uniform"]:
        U = float(input("Uniform speed [m/s]: "))
        alpha_deg = float(input("Angle [deg]: "))
        uniform(U, np.radians(alpha_deg))

    elif flow_type in ["2", "source/sink"]:
        x0 = float(input("x-location: "))
        y0 = float(input("y-location: "))
        strength = float(input("Strength: "))
        source(strength, x0, y0)

    elif flow_type in ["3", "vortex"]:
        x0 = float(input("x-location: "))
        y0 = float(input("y-location: "))
        strength = float(input("Strength: "))
        vortex(strength, x0, y0)

    elif flow_type in ["4", "doublet"]:
        x0 = float(input("x-location: "))
        y0 = float(input("y-location: "))
        strength = float(input("Strength: "))
        doublet(strength, x0, y0)

############################
# CYLINDER RADIUS + MASK
############################

R = None

if U_ref is not None and doublet_strength is not None:
    R = np.sqrt(doublet_strength / (2*np.pi*U_ref))

    dx = X - doublet_center[0]
    dy = Y - doublet_center[1]
    mask = dx**2 + dy**2 <= R**2

    u[mask] = 0.0
    v[mask] = 0.0

############################
# PRESSURE COEFFICIENT
############################

Vi2 = u**2 + v**2

if U_ref is not None and U_ref > 1e-12:
    Cp = 1 - Vi2 / (U_ref**2)
else:
    Cp = np.zeros_like(Vi2)

############################
# PLOTS
############################

# Streamlines
plt.figure()
plt.contourf(X, Y, psi, 60)
plt.colorbar(label="Stream Function")
if R is not None:
    circle = plt.Circle(doublet_center, R, color='k', fill=False)
    plt.gca().add_patch(circle)
plt.axis("equal")
plt.title("Streamlines")
plt.show()

# Potential
plt.figure()
plt.contourf(X, Y, phi, 60)
plt.colorbar(label="Potential Function")
if R is not None:
    circle = plt.Circle(doublet_center, R, color='k', fill=False)
    plt.gca().add_patch(circle)
plt.axis("equal")
plt.title("Potential Field")
plt.show()

# Pressure coefficient
plt.figure()
cp_min = np.min(Cp)
cp_max = np.max(Cp)
levels = np.linspace(cp_min, cp_max, 120)
plt.contourf(X, Y, Cp, levels=levels)
plt.colorbar(label="Pressure Coefficient")
plt.text(0.02, 0.98, f'Max Cp: {cp_max:.2f}', transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
plt.text(0.02, 0.90, f'Min Cp: {cp_min:.2f}', transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
if R is not None:
    circle = plt.Circle(doublet_center, R, color='k', fill=False)
    plt.gca().add_patch(circle)
plt.axis("equal")
plt.title("Pressure Coefficient Field")
plt.show()

# Velocity field
plt.figure()
plt.quiver(X[::25, ::25], Y[::25, ::25],
           u[::25, ::25], v[::25, ::25])
if R is not None:
    circle = plt.Circle(doublet_center, R, color='k', fill=False)
    plt.gca().add_patch(circle)
plt.axis("equal")
plt.title("Velocity Field")
plt.show()

print(f"R is qual to: {R:.3f} m")

############################
# LIFT COEFFICIENT VS ANGULAR VELOCITY
############################

rho = 1.225  # kg/m^3 (air, not actually needed since it cancels)

if R is not None and U_ref is not None and U_ref > 1e-12:

    omega_vals = np.linspace(-200, 200, 200)  # rad/s
    Gamma_vals = 2*np.pi * R**2 * omega_vals
    Cl_vals = Gamma_vals / (U_ref * R)

    plt.figure()
    plt.plot(omega_vals, Cl_vals)
    plt.xlabel("Angular velocity ω [rad/s]")
    plt.ylabel("Lift coefficient C_L")
    plt.title("Lift Coefficient vs Angular Velocity")
    plt.grid(True)
    plt.show()

