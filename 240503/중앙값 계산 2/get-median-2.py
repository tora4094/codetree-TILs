n = int(input())
arr = list(map(int,input().split()))

new_arr = []
for i in range(0,n):
    new_arr.append(arr[i])
    if (i + 1) % 2 == 1:
        index = i // 2        
        new_arr.sort()        
        print(new_arr[index],end=" ")