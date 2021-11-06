"""
Find a the maximum of a set S of n numbers
"""


def func(array):
    if len(array) > 2:
        half = len(array) // 2
        left = array[:half]
        right = array[half:]
        left_max = func(left)
        right_max = func(right)
        return max(left_max, right_max)
    else:
        return max(array)


test_data = [29, 14, 15, 1, 6, 10, 32, 12]
results = func(test_data)
print(results)


"""
Binary Search
"""


def func(array, target):
    middle = len(array) // 2

    if target == array[middle]:
        return middle
    elif target < array[middle]:
        return func(array[:middle], target)
    elif target > array[middle]:
        return func(array[middle:], target) + middle
    else:
        return None


test_data = [1, 2, 3, 4, 5, 6, 7, 8]
results = func(test_data, 2)
print(results)


"""
N!
"""


def func(n):
    if n > 1:
        return func(n - 1) * n
    else:
        return 1


test_data = 5
results = func(test_data)
print(results)


"""
Quick sort
"""


def func(array):
    if len(array) > 1:
        # Move pivot to the middle
        left = 0
        right = len(array) - 1
        pivot_value = array[0]
        while left < right:
            while array[right] >= pivot_value and left < right:
                right -= 1
            while array[left] <= pivot_value and left < right:
                left += 1
            array[left], array[right] = array[right], array[left]
        # Set balance to left or right
        balance = left
        # Switch pivot and balance
        array[0], array[balance] = array[balance], array[0]
        # Recursive both sides
        left_array = func(array[:balance])
        right_array = func(array[balance + 1:])
        # Merge both sides and balance
        return left_array + [array[balance]] + right_array
    elif len(array) == 1:
        return [array[0]]
    elif len(array) < 1:
        return []


test_data = [4, 3, 5, 2, 7, 1, 6]
results = func(test_data)
print(results)
