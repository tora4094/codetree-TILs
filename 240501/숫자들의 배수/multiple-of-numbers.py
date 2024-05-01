from itertools import count
n = int(input())
arr = [n]

count_val = 0

for i in count(2):
    if count_val == 2:
        break
    current_val = n * i
    arr.append(current_val)
    if current_val % 5 == 0:
        count_val += 1
    
    

    
    

for elem in arr:
    print(elem, end=" ")