from itertools import count
n = int(input())
arr = []

count_val = 0

for i in count(1):    
    current_val = n * i
    arr.append(current_val)
    if current_val % 5 == 0:
        count_val += 1
        if count_val == 2:
            break
    
for elem in arr:
    print(elem, end=" ")