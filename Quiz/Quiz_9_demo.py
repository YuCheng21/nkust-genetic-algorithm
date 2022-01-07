# https://blog.csdn.net/kunshanyuz/article/details/63683145

import numpy as np
import random
import matplotlib.pyplot as plt


# ----------------------PSO參數設定---------------------------------
class PSO:
    def __init__(self, pn, dim, max_iter):
        self.w = 0.8
        self.c1 = 2
        self.c2 = 2
        self.r1 = 0.6
        self.r2 = 0.3
        self.pN = pn  # 粒子數量
        self.dim = dim  # 搜尋維度
        self.max_iter = max_iter  # 迭代次數
        self.X = np.zeros((self.pN, self.dim))  # 所有粒子的位置和速度
        self.V = np.zeros((self.pN, self.dim))
        self.pbest = np.zeros((self.pN, self.dim))  # 個體經歷的最佳位置
        self.gbest = np.zeros((1, self.dim))  # 全域性最佳位置
        self.p_fit = np.zeros(self.pN)  # 每個個體的歷史最佳適應值
        self.fit = 1e10  # 全域性最佳適應值

    # ---------------------目標函式Sphere函式-----------------------------
    def sphere_function(self, x):
        result = 0
        length = len(x)
        x = x ** 2
        for i in range(length):
            result += x[i]
        return result

    # ---------------------初始化種群----------------------------------
    def init_population(self):
        for i in range(self.pN):
            for j in range(self.dim):
                self.X[i][j] = random.uniform(0, 1)
                self.V[i][j] = random.uniform(0, 1)
            self.pbest[i] = self.X[i]
            tmp = self.sphere_function(self.X[i])
            self.p_fit[i] = tmp
            if tmp < self.fit:
                self.fit = tmp
                self.gbest = self.X[i]

    # ----------------------更新粒子位置----------------------------------
    def iterator(self):
        fitness = []
        for t in range(self.max_iter):
            for i in range(self.pN):  # 更新gbest\pbest
                temp = self.sphere_function(self.X[i])
                if temp < self.p_fit[i]:  # 更新個體最優
                    self.p_fit[i] = temp
                    self.pbest[i] = self.X[i]
                    if self.p_fit[i] < self.fit:  # 更新全域性最優
                        self.gbest = self.X[i]
                        self.fit = self.p_fit[i]
            for i in range(self.pN):
                self.V[i] = self.w * self.V[i] + self.c1 * self.r1 * (self.pbest[i] - self.X[i]) + self.c2 * self.r2 * (
                            self.gbest - self.X[i])
                self.X[i] = self.X[i] + self.V[i]
            fitness.append(self.fit)
            print(self.fit)  # 輸出最優值
        return fitness


# ----------------------程式執行-----------------------
iteration = 100
dimension = 5
particle_number = 30

my_pso = PSO(pn=particle_number, dim=dimension, max_iter=iteration)
my_pso.init_population()
fitness = my_pso.iterator()
# -------------------畫圖--------------------
t = np.array([t for t in range(0, iteration)])
fitness = np.array(fitness)

plt.title("PSO")
plt.xlabel("iterators")
plt.ylabel("fitness")
plt.plot(t, fitness)
plt.show()
