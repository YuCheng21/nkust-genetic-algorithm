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
    def recursive(item):
        next_val = []
        found = False
        for i in data:
            if i[0] == item[-1] and i[1] not in item:
                found = True
                next_val = [*next_val, [*item, *[i[1]]]]
        if found is False:
            return item
        maximum = []
        for i in next_val:
            res = recursive(i)
            maximum = list(set(maximum) | set(res))
        return maximum

    ravel = [j for i in data for j in i]
    classification = list(dict([(i, ravel.count(i)) for i in ravel]))
    depth = []
    for i in classification:
        depth = [*depth, len(recursive([i]))]
    print("Each node(key) can traverse(value): ", dict(zip(classification, depth)), sep='\n', end='\n\n')
    max_val = max(depth)
    max_item = [idx for idx, val in zip(classification, depth) if val == max_val]
    return max_item


# test_data = [
#     [1, 2],
#     [2, 1],
#     [4, 3],
#     [3, 2],
# ]
# test_data = [
#     [1, 2],
#     [2, 1],
#     [4, 3],
#     [3, 2],
#     [1, 3],
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
    [1, 2],
    [3, 4],
    [10, 9],
    [9, 8],
    [8, 7],
    [7, 6],
]

result = best_starting_point(test_data)
print("These nodes can traverse the most node: ", result, sep='\n')
