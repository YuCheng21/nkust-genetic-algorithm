"""
一串沒有排序的陣列
從中找到一個連續陣列，其元素總和是最大值

Input: [-2, 1, -3,  4, -1, 2, 1, -5, 4 ]
Output: 6    (4-1+2+1 = 6)
"""


def quiz_4(array):
    current = 0
    result = array[0]
    for i in array:
        current += i
        result = max(result, current)
        current = max(0, current)
    return result


test_data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
results = quiz_4(test_data)
print(results)
