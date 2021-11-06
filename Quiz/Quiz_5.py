"""
0198. House Robber (Easy)
一個小偷要偷東西找到了一排房子。每個房子裡的有不ㄧ樣的財物價值可以偷，但因為防盜系統不能偷相鄰兩間房子的物品
請找出最大你能偷的財物價值。

Input: [1, 2, 3, 1]  : Output: 4
// 1+3 = 4.

Input: [2, 7, 9, 3, 1]  : Output: 12
// 2+9+1=12
"""


def quiz_5(array):
    length = len(array)
    if length == 1:
        return array[0]
    if length == 2:
        return max(array[0], array[1])

    dist = [array[0], array[1]]
    count = 2
    while count < length:
        dist.append(array[count] + max(dist[:-1]))
        count += 1

    return max(dist)


test_data = [1, 2, 3, 1]
# test_data = [2, 7, 9, 3, 1]
result = quiz_5(test_data)
print(result)
