input_arr = list(map(int, input().split()))
arr1 = []
arr2 = []
for elem in input_arr:
    if elem < 500:
        arr1.append(elem)
    elif elem > 500:
        arr2.append(elem)

max_val = arr1[0]
for elem in arr1[1:]:
    if elem > max_val:
        max_val = elem

min_val = arr2[0]
for elem in arr2[1:]:
    if min_val > elem:
        min_val = elem
        
print(f"{max_val} {min_val}")