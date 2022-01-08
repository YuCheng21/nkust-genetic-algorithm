import math
import random


class GrasshopperOptimisationAlgorithm:
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
        self.__capacity = None
        self.__optimal = None
        self.things_information = []
        # Generate random data
        self.bags = []
        # Calculate fitness value
        self.punish_fitness_value = 5
        self.best_fitness = None

    def add_things_information(self, weight, profits):
        self.things_information.append({'weight': weight, 'profits': profits})

    def reset_things_information(self):
        self.things_information = []

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

    def calculate_fitness_value(self):
        self.best_fitness = {'profits': 0}
        for bag_index, bag_value in enumerate(self.bags):
            weight = 0
            profits = 0
            for thing_index, thing_value in enumerate(bag_value['things']):
                if thing_value is 1:
                    weight += self.things_information[thing_index]['weight']
                    profits += self.things_information[thing_index]['profits']
            self.bags[bag_index]['weight'] = weight
            if weight > self.capacity:
                self.bags[bag_index]['profits'] = self.punish_fitness_value
            else:
                self.bags[bag_index]['profits'] = profits
            if self.bags[bag_index]['profits'] > self.best_fitness['profits']:
                self.best_fitness = self.bags[bag_index]

    def iterator(self):
        space = (self.upper_bound - self.lower_bound) / 2
        for current_iter in range(self.max_iter):
            self.calculate_fitness_value()
            print('====================')
            # print(*self.bags, sep='\n')
            print(self.best_fitness)
            c_value = self.c_max - (self.c_max - self.c_min) * (current_iter / self.max_iter)
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
                        if distance == 0:
                            buffer.append(0)
                        else:
                            buffer.append(c_value * space * social_interaction * vector / distance)
                    sub_summation.append(buffer)
                sub_summation_t = [list(row) for row in zip(*sub_summation)]
                result = []
                for row_index, row_value in enumerate(sub_summation_t):
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
    'max_iter': 9,
    'c_max': 1,
    'c_min': 1e-5,
    'upper_bound': 1,
    'lower_bound': 0,
    'dimension': 1,
    'f_arg': 1,
    'l_arg': 2
}
GOA = GrasshopperOptimisationAlgorithm(**kwargs)

# # ============= Use P01 Dataset =============
GOA.capacity = 165
GOA.optimal = [1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
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

# Generate random data
GOA.generate_random_data(30)

# Start GOA
GOA.iterator()
print('\noptimal: ', GOA.optimal, sep='\n')

# ============= Use P02 Dataset =============
# GOA.capacity = 26
# GOA.optimal = [0, 1, 1, 1, 0]
# GOA.reset_things_information()
# GOA.add_things_information(12, 24)
# GOA.add_things_information(7, 13)
# GOA.add_things_information(11, 23)
# GOA.add_things_information(8, 15)
# GOA.add_things_information(9, 16)
#
# # Generate random data
# GOA.generate_random_data(50)
#
# # Start GOA
# GOA.iterator()
# print('\noptimal: ', GOA.optimal, sep='\n')
