import numpy as np

B = np.array([
    [0.24, 0.21, 0.06, -0.34],
    [0.05, 0.32, 0.12, -0.57,],
    [0.35, -0.27, -0.05, 0.68],
    [0.12, -.28, -0.14, 0.94]
])

c = np.array([1.42, -0.57, 0.68, -2.14])

eps = 0.0001

x = np.array([0.0, 0.0, 0.0, 0.0])
k = 0
max_iter = 1000
for k in range(1, max_iter + 1):
    x_new = B @ x + c
    diff = np.abs(x_new-x)
    print(f"{k:>3} | {x_new[0]:>10.6f} | {x_new[1]:>10.6f} | {x_new[2]:>10.6f} | {x_new[3]:>10.6f} | "
          f"{diff[0]:>8.6f} | {diff[1]:>8.6f} | {diff[2]:>8.6f} | {diff[3]:>8.6f}")
    x = x_new.copy()
    if np.all(diff < eps):
        print(f"Сошлось на {k}")
        break
print(f"\nРешение (простые итерации): x1={x[0]:.6f}, x2={x[1]:.6f}, x3={x[2]:.6f}, x4={x[3]:.6f}")


x = np.array([0.0, 0.0, 0.0, 0.0])
k = 0

for k in range(1, max_iter +1):
    x_old = x.copy()
    x[0] = 0.24*x_old[0] + 0.21*x_old[1] + 0.06*x_old[2] - 0.34*x_old[3] + 1.42
    x[1] = 0.05*x[0]      + 0.00*x_old[1] + 0.32*x_old[2] + 0.12*x_old[3] - 0.57
    x[2] = 0.35*x[0]      - 0.27*x[1]     + 0.00*x_old[2] - 0.05*x_old[3] + 0.68
    x[3] = 0.12*x[0]      - 0.43*x[1]     + 0.34*x[2]     - 0.21*x_old[3] - 2.14
    diff = np.abs(x-x_old)
    print(f"{k:>3} | {x[0]:>10.6f} | {x[1]:>10.6f} | {x[2]:>10.6f} | {x[3]:>10.6f} | "
          f"{diff[0]:>8.6f} | {diff[1]:>8.6f} | {diff[2]:>8.6f} | {diff[3]:>8.6f}")
    if np.all(diff < eps):
        print(f"Сошлось на {k}")
        break
print(f"\nРешение (Зейгель): x1={x[0]:.6f}, x2={x[1]:.6f}, x3={x[2]:.6f}, x4={x[3]:.6f}")
    