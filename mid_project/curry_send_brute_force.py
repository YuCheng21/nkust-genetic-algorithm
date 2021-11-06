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
    length = len(data)
    distance = []
    for i in range(length):
        start, end = data[i]
        count = [i]
        record = 0
        while True:
            try:
                target_index = list(zip(*data))[0].index(end, record)
            except ValueError:
                distance.append(len(count))
                break
            if target_index in count:
                record = target_index + 1
                continue
            record = 0
            start, end = data[target_index]
            count.append(target_index)

    best_value = [data[idx][0] for idx, value in enumerate(distance) if value == max(distance)]
    # print("start list: ", list(zip(*data))[0])
    # print("distance list: ", distance)
    return best_value


# test_data = [
#     [1, 2],
#     [2, 1],
#     [5, 3],
#     [3, 4],
#     [4, 5],
# ]
#
# test_data = [
#     [1, 2],
#     [2, 1],
#     [4, 3],
#     [3, 2],
# ]
#
# test_data = [
#     [1, 2],
#     [2, 1],
#     [2, 3],
#     [3, 4],
#     [4, 5],
# ]
#
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
#     [3, 2],
# ]
# Wrong, may have [2, 10]
test_data = [
    # 2 have 5 node
    [2, 3],
    [2, 5],
    [2, 1],
    # [1, 2],
    [3, 4],

    # 10 have 5 node
    [10, 9],
    [9, 8],
    [8, 7],
    [7, 6],
]


result = best_starting_point(test_data)
print("the best node: ", result)
