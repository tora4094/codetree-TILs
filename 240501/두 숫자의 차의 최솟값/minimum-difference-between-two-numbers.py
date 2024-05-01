n = int(input())
arr = list(map(int, input().split()))

min_diff = arr[1] - arr[0]

for i in range(2, n):
    diff = arr[i] - arr[i - 1]
    if diff < min_diff:
        min_diff = diff

print(min_diff)