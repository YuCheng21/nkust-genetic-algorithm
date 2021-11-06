"""
給定一組陣列資料，陣列中每個元素代表你在該位置的最大跳躍長度。寫一個程式來確定否能夠從第一個點跳到最後一個點

Input: [2, 3, 1, 1, 4]  : Output: Y
// Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: [3, 2, 1, 0, 4]  : Output: N
// Impossible

"""


def quiz_3(array):
    length = len(array)
    if length == 0:
        return False
    # 紀錄可以走最大步數
    maximum = 0
    # 遞迴陣列長度
    for i in range(length):
        # 可以走的最大步數 < 當前的位置 = 無法走到最後
        if maximum < i:
            return False
        # 可以走的最大步數 > 最後一個位置 = 可以走到最後
        if maximum > length:
            return True
        # 比較[可以走的最大步數]與[當前 Index 可以走的步數 + index]的最大的數字，即為可以走的最大步數
        maximum = max(maximum, array[i] + i)
    # 如果走到最後沒有回傳 False，代表這個陣列可以走到最後
    return True


test_data = [2, 2, 0, 3, 4]
results = quiz_3(test_data)
print(results)
