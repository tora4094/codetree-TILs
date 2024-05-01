n = int(input())
arr = list(map(long,input().split()))
for i in range(0,n):
    for j in range(n - i - 1):        
        if arr[i] < arr[i+j]:
            arr[i], arr[i+j] = arr[i+j], arr[i]
print(f"{arr[0]} {arr[1]}")