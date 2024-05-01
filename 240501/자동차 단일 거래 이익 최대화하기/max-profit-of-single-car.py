n = int(input())
arr = list(map(int, input().split()))

min_val = arr[0]
result = 0

for elem in arr[1:]:
    sum_val = elem - min_val
    if sum_val > result:
        result = sum_val
    if elem < min_val:
        min_val = elem

print(result)