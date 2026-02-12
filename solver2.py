import numpy as np
import matplotlib.pyplot as plt

###### GRID ###########

x = np.linspace(-5, 5, 300)
y = np.linspace(-5, 5, 300)
X, Y = np.meshgrid(x, y)

phi = np.zeros_like(X)
psi = np.zeros_like(X)
u = np.zeros_like(X)
v = np.zeros_like(X)

U_inf = 5   # m/s
alpha = 0.0   # angle of attack (rad)


##### FLOW TYPES ######

def uniform(U, alpha):
    global phi, psi, u, v
    phi += U*(X*np.cos(alpha) + Y*np.sin(alpha))
    psi += U*(Y*np.cos(alpha) - X*np.sin(alpha))
    u += U*np.cos(alpha)
    v += U*np.sin(alpha)

def source(strength, x0, y0):
    global phi, psi, u, v
    delta_x = X - x0
    delta_y = Y - y0
    r = np.sqrt( delta_x**2 + delta_y**2 )
    r[r == 0] = 1e-12
    theta = np.arctan2(delta_y,delta_x)

    phi += strength/(2*np.pi)*np.log(r)
    psi += strength/(2*np.pi)*np.arctan2(delta_y, delta_x)
    u += strength/(2*np.pi)*(delta_x/r)
    v += strength/(2*np.pi)*(delta_y/r)

def vortex(strength, x0, y0):
    global phi, psi, u, v
    delta_x = X - x0
    delta_y = Y - y0
    r = np.sqrt( delta_x**2 + delta_y**2)
    theta = np.arctan2(delta_y,delta_x)

    r[r == 0] = 1e-12

    phi -= strength/(2*np.pi)*theta
    psi += strength/(2*np.pi)*np.log(r)
    u -= strength/(2*np.pi)*(delta_y/r)
    v += strength/(2*np.pi)*(delta_x/r)

def doublet(strength, x0, y0):
    global phi, psi, u, v
    delta_x = X - x0
    delta_y = Y - y0
    r = np.sqrt(delta_x**2 + delta_y**2)
    r2 = r**2
    r[r == 0] = 1e-12
    r2[r2 == 0] = 1e-12
    theta = np.arctan2(delta_y,delta_x)

    phi += strength/(2*np.pi)*(np.cos(theta)/r)
    psi -= strength/(2*np.pi)*(np.sin(theta)/r)

    u -= strength/(2*np.pi)*((delta_x**2 - delta_y**2)/r2)
    v -= strength/(2*np.pi)*(2*delta_x*delta_y/r2)

### USER INTERFACE ##### 

print("Enter canonical flows:")
print("1: uniform")
print("2: source/sink")
print("3: vortex")
print("4: doublet")
print("Type 'done' to finish adding flows. \n")

while True:
    flow_type = input("Enter flow type: ")

    if flow_type.lower() == "done":
        break

    if flow_type == "1" or flow_type == "uniform":
        U = float(input("Enter uniform flow speed: "))
        alpha_deg = float(input("Enter flow angle (deg): "))
        uniform(U, np.radians(alpha_deg))

    elif flow_type in ["2", "3", "4", "source/sink", "vortex", "doublet"]:
        x0 = float(input("Enter x-location: "))
        y0 = float(input("Enter y-location: "))
        strength = float(input("Enter strength: "))

        if flow_type == "2" or flow_type == "source/sink":
            source(strength, x0, y0)
        elif flow_type == "3" or flow_type == "vortex":
            vortex(strength, x0, y0)
        elif flow_type == "4" or flow_type == "doublet":
            doublet(strength, x0, y0)

    else:
        print("Invalid selection.")

# ------------------------------------------------------------
# Compute Pressure Coefficient
# ------------------------------------------------------------

V2 = u**2 + v**2

Cp = 1 - V2/(U_inf**2)

# ------------------------------------------------------------
# Plot Results
# ------------------------------------------------------------

print('cp: ' , Cp)

plt.figure()
plt.contourf(X, Y, psi, levels=50)
plt.colorbar(label="Stream Function")
plt.title("Streamlines")
plt.axis("equal")
plt.show()

plt.figure()
plt.contourf(X, Y, phi, levels=50)
plt.colorbar(label="Potential Function")
plt.title("Potential Field")
plt.axis("equal")
plt.show()

plt.figure()
plt.contourf(X, Y, Cp, levels=50)
plt.colorbar(label="Pressure Coefficient")
plt.title("Pressure Coefficient Field")
plt.axis("equal")
plt.show()

plt.figure()
plt.quiver(X[::20, ::20], Y[::20, ::20],
           u[::20, ::20], v[::20, ::20])
plt.title("Velocity Field")
plt.axis("equal")
plt.show()
