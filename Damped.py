import numpy as np
import matplotlib.pyplot as plt

b = 1
k = 1
m = 1

def G(t, f):
    return np.array([f[1], -b/m*f[1] - k/m*f[0]])

def rk4_meth(f, t, h):
    k1 = h * G(t, f)
    k2 = h * G(t + 0.5*h, f + 0.5*k1)
    k3 = h * G(t + 0.5*h, f + 0.5*k2)
    k4 = h * G(t + h, f + k3)
    return f + 1/6 * (k1 + 2*k2 + 2*k3 + k4)

# Initial Conditions
f = np.array([0, 1])
t = 0
n = 1000
h = 0.1

x = []
time = []
x.append(f[0])
time.append(t)
cur = f

for i in range(n):
    cur = rk4_meth(cur, t, h)
    x.append(cur[0])
    t += h  # Update time
    time.append(t)  # Append updated time

plt.plot(time, x)  # Plot time on x-axis and x on y-axis
plt.xlabel('Time')
plt.ylabel('Displacement (x)')
plt.title('Displacement vs Time')
plt.grid(True)
plt.show()