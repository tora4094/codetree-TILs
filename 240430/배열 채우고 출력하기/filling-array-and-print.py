arr = list(input().split())
arr_len = len(arr)
for i in range(arr_len - 1, -1, -1):
    print(arr[i], end="")