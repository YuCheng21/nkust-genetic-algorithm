"""
Curry 要寄一封 email 出去給隊友，但不想花錢卻只發給一個人。
他查出了誰會把信轉給誰
他想知道：他的信要寄給誰才能讓最多的勇士隊球員看到？

4 (個人)
1>2, 2>1, 4>3, 3>2
5 (個人)
1>2, 2>1, 5>3, 3>4, 4>5
"""


def best_starting_point(data):
    # ========== Data Pre-processing
    # Mapping test_data start from 0
    one_dimension = [j for i in data for j in i]
    category = dict([(i, one_dimension.count(i)) for i in one_dimension])
    key = list(category.keys())
    value = list(range(len(category)))
    maps = dict(zip(key, value))
    map_data = [[maps[e] for e in data[idx]] for idx in range(len(data))]
    # Make a Floyd-Warshall template
    length = len(maps)
    array = []
    for i in range(length):
        buffer = []
        for j in range(length):
            if i == j:
                buffer.append(0)
            else:
                buffer.append(float("-inf"))
        array.append(buffer)
    # Insert value in template
    for i in map_data:
        array[i[0]][i[1]] = 1

    # ========== Start Algorithm - Floyd-Warshall (DP)
    for k in range(length):
        for i in range(length):
            if i == k:
                continue
            for j in range(length):
                if j == k:
                    continue
                if array[i][k] + array[k][j] > array[i][j]:
                    array[i][j] = array[i][k] + array[k][j]

    # ========== End Algorithm
    # Get the maximum of each row
    row_max = [max(i) for i in array]
    # Get the index of the maximum value of all rows
    best_idx = [idx for idx, val in enumerate(row_max) if val == max(row_max)]
    # Get the best result and print
    best_value = [idx for idx, val in maps.items() if val in best_idx]
    return best_value


# test_data = [
#     [1, 2],
#     [2, 1],
#     [4, 3],
#     [3, 2],
# ]
# test_data = [
#     [1, 2],
#     [2, 1],
#     [5, 3],
#     [3, 4],
#     [4, 5],
# ]
# test_data = [
#     [1, 2],
#     [2, 1],
#     [2, 3],
#     [3, 4],
#     [4, 5],
# ]
# test_data = [
#     [1, 2],
#     [2, 1],
#     [4, 3],
#     [3, 4],
#     [4, 5],
# ]
# test_data = [
#     [5, 11],
#     [2, 3],
#     [2, 5],
#     [2, 1],
#     [3, 2]
# ]
test_data = [
    [2, 3],
    [2, 5],
    [2, 1],
    # [1, 2],
    [3, 4],
    [10, 9],
    [9, 8],
    [8, 7],
    [7, 6],
]


result = best_starting_point(test_data)
print("the best node: ", result)
