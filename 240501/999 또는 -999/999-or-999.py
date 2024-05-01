arr = list(map(int, input().split()))
min_value = arr[0]
max_value = arr[0]
for elem in arr[1:]:
    if elem == 999:
        break
    elif elem == -999:
        break
    if min_value > elem:
        min_value = elem
    if elem > max_value:
        max_value = elem
            
print(f"{max_value} {min_value}")