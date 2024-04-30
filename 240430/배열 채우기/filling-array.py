arr = list(map(int,input().split()))
new_arr = []
for elem in arr:
    if (elem != 0):
        new_arr.append(elem)
    else:
        break
for i in range(len(new_arr) - 1, -1, -1):
    print(new_arr[i],end=" ")