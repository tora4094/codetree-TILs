arr = list(map(int,input().split()))
print(f"{arr[0]} {arr[1]}",end=" ")
for i in range (2, 10):
    elem = (arr[i-2] + arr[i-1]) % 10
    arr.append(elem)
    print(f"{elem}",end=" ")