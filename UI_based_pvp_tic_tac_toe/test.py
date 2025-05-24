import random
import matplotlib.pyplot as plt

total_points = 10000
inside_circle = 0

x_in, y_in = [], []     # 圆内的点
x_out, y_out = [] , []  # 圆外的点

for _ in range(total_points):
    x = random.random()
    y = random.random()
    
    distance = ((x - 0.5) ** 2 + (y - 0.5) ** 2) ** 0.5
    if distance <= 0.5:
        inside_circle += 1
        x_in.append(x)
        y_in.append(y)
    else:
        x_out.append(x)
        y_out.append(y)

# 估算 π
pi_estimate = 4 * inside_circle / total_points
print("Estimated π:", pi_estimate)

# 可视化
plt.figure(figsize=(6,6))
plt.scatter(x_in, y_in, color='blue', s=1, label='Inside Circle')
plt.scatter(x_out, y_out, color='red', s=1, label='Outside Circle')
plt.gca().set_aspect('equal')  # 保持比例
plt.title("Monte Carlo Simulation of π")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()