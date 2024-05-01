arr = list(map(int,input().split()))
for i in range(2, 10):
    a = (2 * arr[i-2]) + arr[i-1]
    arr.append(a)
for elem in arr:
    print(elem,end=" ")