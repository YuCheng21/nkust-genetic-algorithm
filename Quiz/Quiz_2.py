"""
有一個12個整數的陣列 (15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14)
請寫出程式將數字中偶數的數字加以排序，但不能更動奇數數字的位置
-> (15, 4, 19, 10, 25, 1, 3, 14, 5, 7, 16, 20)

Algorithm:
使用選擇排序法排序，並且在 Value 為奇數時跳過排序。
"""


def odd_sort(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] % 2 == 1:
            # This round value is odd
            continue

        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] % 2 == 1:
                # The minimum value was found is odd.
                continue
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers


data = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
results = odd_sort(data)
print(results)
