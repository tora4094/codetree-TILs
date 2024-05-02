n = int(input())
arr = list(map(int, input().split()))
arr.sort()
max_sum = 0
for i in range(n):
    sum_val = arr[i] + arr[2 * n - 1 - i]
    if sum_val > max_sum:
        max_sum = sum_val
print(max_sum)