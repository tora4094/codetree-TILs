n = int(input())
arr = list(map(int, input().split()))

max_positions = []

current_index = n

while current_index > 0:
    current_max = max(arr[:current_index])
    max_index = arr[:current_index].index(current_max)
    max_positions.append(max_index + 1)
    current_index = max_index

for max_position in max_positions:
    print(max_position,end=" ")