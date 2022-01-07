import numpy as np
import random
import matplotlib.pyplot as plt


w = 0.8
c1 = 2
c2 = 2
r1 = 0.6
r2 = 0.3
pN = 30  # 粒子數量
dim = 5  # 搜尋維度
max_iter = 100  # 迭代次數
X = np.zeros((pN, dim))  # 所有粒子的位置和速度
V = np.zeros((pN, dim))
pbest = np.zeros((pN, dim))  # 個體經歷的最佳位置
gbest = np.zeros((1, dim))  # 全域性最佳位置
p_fit = np.zeros(pN)  # 每個個體的歷史最佳適應值
fit = 1e10  # 全域性最佳適應值


def sphere_function(x):
    result = 0
    length = len(x)
    x = x ** 2
    for index in range(length):
        result += x[index]
    return result


for i in range(pN):
    for j in range(dim):
        X[i][j] = random.uniform(0, 1)
        V[i][j] = random.uniform(0, 1)
    pbest[i] = X[i]
    tmp = sphere_function(X[i])
    p_fit[i] = tmp
    if tmp < fit:
        fit = tmp
        gbest = X[i]


fitness = []
for t in range(max_iter):
    for i in range(pN):  # 更新gbest\pbest
        temp = sphere_function(X[i])
        if temp < p_fit[i]:  # 更新個體最優
            p_fit[i] = temp
            pbest[i] = X[i]
            if p_fit[i] < fit:  # 更新全域性最優
                gbest = X[i]
                fit = p_fit[i]
    for i in range(pN):
        V[i] = w * V[i] + c1 * r1 * (pbest[i] - X[i]) + c2 * r2 * (gbest - X[i])
        X[i] = X[i] + V[i]
    fitness.append(fit)
    print(fit)  # 輸出最優值


t = np.array([t for t in range(0, max_iter)])
fitness = np.array(fitness)

plt.title("PSO")
plt.xlabel("iterators")
plt.ylabel("fitness")
plt.plot(t, fitness)
plt.show()
