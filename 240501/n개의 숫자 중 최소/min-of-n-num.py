n = int(input())
arr = list(map(int,input().split()))
min_val = arr[0]
cnt = 0
for elem in arr[1:]:
    if (min_val > elem):
        min_val = elem
for i in range(0, n):
    if (arr[i] == min_val):
        cnt += 1
print(f"{min_val} {cnt}")