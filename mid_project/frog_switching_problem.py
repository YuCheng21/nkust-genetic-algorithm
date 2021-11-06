"""
Frog switching problem
Ex: XXXX YYYY -> YYYY XXXX

Algorithm:
能跳就先跳，不能跳就走，走過一次就換邊
不能走也不能跳也換邊
連換兩次沒有走或跳，就結束(左右都走不動、也跳不動)
"""

data = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
print(data)

# direction: low(left)=1, high(right)=2
direction_total = 1 + 2
direction = 2
# target_data: {1: [-4, -3, -2, -1], 2: [1, 2, 3, 4]}
target_data = {
    1: [],
    2: []
}
for i in data:
    if i < 0:
        target_data[1] += [i]
    elif i > 0:
        target_data[2] += [i]

# If direction_counter = 2, then finish (low and high directions finished)
direction_counter = 0
while direction_counter < 2:
    zero = None
    # Traverse from high to low
    if direction == 1:
        start = len(data) - 1
        end = 0 - 1
        step = -1
    # Traverse from low to high
    elif direction == 2:
        start = 0
        end = len(data)
        step = 1
    # Start traversal
    for i in range(start, end, step):
        if data[i] == 0:
            zero = i
        if data[i] in target_data[direction] and zero is not None:
            # Switch position
            data[zero], data[i] = data[i], data[zero]
            # Print current list
            print(data)
            # Update zero index
            zero = i
            # Reset counter
            direction_counter = 0
            # Length: walk=1, jump=2
            length = abs(zero - i)
            if length == 2:
                continue
            if length == 1:
                # Switch direction
                direction = direction_total - direction
                break
    else:
        direction = direction_total - direction
        direction_counter += 1

print(data)
