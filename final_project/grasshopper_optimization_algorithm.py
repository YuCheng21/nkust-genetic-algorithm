import math
import random
import matplotlib.pyplot as plt

"""
Reference: https://doi.org/10.1016/j.advengsoft.2017.01.004
Dataset: https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html
"""


class GrasshopperOptimizationAlgorithm:
    """
    Grasshopper Optimization Algorithm for 01 Knapsack Problem
    """

    def __init__(self, max_iter, c_max, c_min, upper_bound, lower_bound, dimension, f_arg, l_arg):
        # GOA arguments
        self.max_iter = max_iter
        self.c_max = c_max
        self.c_min = c_min
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        self.dimension = dimension
        self.f_arg = f_arg
        self.l_arg = l_arg
        # Custom dataset
        self.__name = None
        self.__capacity = None
        self.__optimal = None
        self.things_information = []
        # Generate random data
        self.bags = []
        # Calculate fitness value
        self.punish_fitness_value = 5
        self.best_fitness = None
        self.current_iteration = None
        # Plot figure
        self.history_fitness_value = []

    def add_things_information(self, weight, profits):
        self.things_information.append({'weight': weight, 'profits': profits})

    def reset_things_information(self):
        self.things_information = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = value

    @property
    def optimal(self):
        return self.__optimal

    @optimal.setter
    def optimal(self, value):
        self.__optimal = value

    def generate_random_data(self, quantity):
        self.bags = []
        for i in range(0, quantity):
            self.bags.append({'things': random.choices([0, 1], k=len(self.things_information))})

    def calculate_fitness_value(self, things: list) -> [int, int]:
        weight = 0
        profits = 0
        for thing_index, thing_value in enumerate(things):
            if thing_value is 1:
                weight += self.things_information[thing_index]['weight']
                profits += self.things_information[thing_index]['profits']
        return weight, profits

    def get_fitness(self):
        self.best_fitness = {'profits': 0}
        for bag_index, bag_value in enumerate(self.bags):
            weight, profits = self.calculate_fitness_value(bag_value['things'])
            self.bags[bag_index]['weight'] = weight
            if weight > self.capacity:
                self.bags[bag_index]['profits'] = self.punish_fitness_value
            else:
                self.bags[bag_index]['profits'] = profits
            if self.bags[bag_index]['profits'] > self.best_fitness['profits']:
                self.best_fitness = self.bags[bag_index]

    def record_fitness_value(self):
        buffer = []
        for bag in self.bags:
            buffer.append(bag['profits'])
        self.history_fitness_value.append(buffer)

    def reset_history_fitness(self):
        self.history_fitness_value = []

    def plot_fitness_trend(self):
        mean = list(map((lambda x: sum(x) / len(x)), self.history_fitness_value))
        stddev = list(map((lambda x: math.sqrt(sum((i - sum(x) / len(x)) ** 2 for i in x) / len(x))),
                          self.history_fitness_value))
        optimal_weight_value, optimal_profits_value = self.calculate_fitness_value(self.optimal)

        plt.plot(range(1, len(mean) + 1), mean, marker='o', label='mean', linestyle='solid', color='steelblue')
        plt.plot(range(1, len(stddev) + 1), stddev, marker='o', label='stddev', linestyle='dashed', color='orange')
        plt.axhline(optimal_profits_value, linestyle='dotted', color='lightcoral')
        plt.xlabel('Iteration')
        plt.ylabel('Fitness value')
        plt.title(f'GOA, Dataset={self.name}, Optimal fitness={optimal_profits_value}')
        plt.legend(loc='upper left')
        plt.show()
        print('===================================================')
        print('Optimal fitness: ')
        print(f'thing: {GOA.optimal}, weight: {optimal_weight_value}, profits: {optimal_profits_value}')
        print('\n\n\n\n')

    def print_current_state(self):
        print('===================================================')
        print(f'Iteration: {self.current_iteration}')
        print(*self.bags, sep='\n')
        print(f'Best fitness:\n {self.best_fitness}')

    def iterator(self):
        print(f'[{self.name}]')
        space = (self.upper_bound - self.lower_bound) / 2
        self.reset_history_fitness()
        for current_iteration in range(self.max_iter):
            self.current_iteration = current_iteration
            self.get_fitness()
            self.record_fitness_value()
            self.print_current_state()
            c_value = self.c_max - (self.c_max - self.c_min) * (current_iteration / self.max_iter)
            next_iter_bags = []
            for i_bag_index, i_bag_value in enumerate(self.bags):
                sub_summation = []
                for j_bag_index, j_bag_value in enumerate(self.bags):
                    if i_bag_index == j_bag_index:
                        continue
                    buffer = []
                    for index in range(len(i_bag_value['things'])):
                        vector = j_bag_value['things'][index] - i_bag_value['things'][index]
                        distance = abs(vector)
                        social_interaction = self.f_arg * math.exp(-distance / self.l_arg) - math.exp(-distance)
                        try:
                            buffer.append(c_value * space * social_interaction * vector / distance)
                        except ZeroDivisionError:
                            buffer.append(0)
                    sub_summation.append(buffer)
                sub_summation_transpose = [list(row) for row in zip(*sub_summation)]
                result = []
                for row_index, row_value in enumerate(sub_summation_transpose):
                    summation = 0
                    for col in row_value:
                        summation += col
                    equation = summation * c_value + self.best_fitness['things'][row_index]
                    activation = (lambda data: 1 if data > 0.5 else 0)(equation)
                    result.append(activation)
                next_iter_bags.append(result)
            for i in range(len(self.bags)):
                self.bags[i] = {'things': next_iter_bags[i]}


# Setting GOA
kwargs = {
    'max_iter': 10,
    'c_max': 1,
    'c_min': 4e-5,
    'upper_bound': 1,
    'lower_bound': 0,
    'dimension': None,
    'f_arg': 0.5,
    'l_arg': 1
}
GOA = GrasshopperOptimizationAlgorithm(**kwargs)
GOA.punish_fitness_value = 5
print(GOA.__doc__)

# ============= Use P01 Dataset =============
GOA.name = 'P01'
GOA.capacity = 165
GOA.reset_things_information()
GOA.add_things_information(23, 92)
GOA.add_things_information(31, 57)
GOA.add_things_information(29, 49)
GOA.add_things_information(44, 68)
GOA.add_things_information(53, 60)
GOA.add_things_information(38, 43)
GOA.add_things_information(63, 67)
GOA.add_things_information(85, 84)
GOA.add_things_information(89, 87)
GOA.add_things_information(82, 72)
GOA.dimension = len(GOA.things_information)
GOA.optimal = [1, 1, 1, 1, 0, 1, 0, 0, 0, 0]

# Generate random data
GOA.generate_random_data(30)

# Start GOA
GOA.iterator()
GOA.plot_fitness_trend()

# ============= Use P02 Dataset =============
GOA.name = 'P02'
GOA.capacity = 26
GOA.reset_things_information()
GOA.add_things_information(12, 24)
GOA.add_things_information(7, 13)
GOA.add_things_information(11, 23)
GOA.add_things_information(8, 15)
GOA.add_things_information(9, 16)
GOA.dimension = len(GOA.things_information)
GOA.optimal = [0, 1, 1, 1, 0]

# Generate random data
GOA.generate_random_data(30)

# Start GOA
GOA.iterator()
GOA.plot_fitness_trend()
