import numpy as np
import matplotlib.pyplot as plt
import random

# 初始值
x = [100, 50]

# 初始溫度
t0 = 100
temp_for_plot = t0

# 跑幾回合
run = 100

# 一次找到幾個鄰居
iter = 10

# 降溫係數
alpha = 0.95

t_temp = []
ans = []

accept_count = 0
for i in range(run):
    for j in range(iter):
        random_x = []
        new_x = []
        for k in range(len(x)):
            random_x.append(random.uniform(-0.5, 0.5))
            new_x.append(x[k] + random_x[k])

        new_obj_sigma = 0
        new_obj_pi = 1
        curr_obj_sigma = 0
        curr_obj_pi = 1
        for k in range(len(x)):
            new_obj_sigma += abs(new_x[k])
            new_obj_pi *= abs(new_x[k])

            curr_obj_sigma += abs(x[k])
            curr_obj_pi *= abs(x[k])

        new_obj = new_obj_sigma + new_obj_pi
        curr_obj = curr_obj_sigma + curr_obj_pi

        if new_obj <= curr_obj:
            x = new_x
        else:
            r = np.random.rand()
            if r <= 1 / (np.exp((new_obj - curr_obj) / t0)):
                accept_count += 1
                x = new_x
    t_temp.append(t0)
    ans.append(curr_obj)

    t0 = alpha * t0

print("總共接受較差狀態次數: ", accept_count)
plt.plot(t_temp, ans)
plt.xlabel("Temperature")
plt.ylabel("Objective value")
plt.xlim(temp_for_plot, 0)
plt.show()
