import sys
n = int(input())
arr = list(map(int, input().split()))

min_total_distance = sys.maxsize

for i in range(n):
    total_distance = 0
    for j in range(n):
        distance = abs(i - j)
        total_distance += arr[j] * distance
    
    if total_distance < min_total_distance:
        min_total_distance = total_distance

print(min_total_distance)

        
    #1= 1-1 
    #2= abs(1-2) = 1
    #3= abs(1-3) = 2

# import sys
# INT_MAX = sys.maxsize
# INT_MIN = -sys.maxsize
# print(INT_MAX,INT_MIN)

# n = 5
# arr = [-6, -5, -2, -10, -15]
# max_val = arr[0]
# for i in range(n):
#     if arr[i] > max_val:
#         max_val = arr[i]
# print(max_val)


# A = [1, 5, 2 ,6, 8]

# answer = 0

# for i in range(5):
#     A[i] *= 2
#     S = 0
#     for j in range(4):
#         S += abs(A[j] - A[j+1])    
#     answer = max(answer, S)
#     A[i] //= 2
# print(answer)