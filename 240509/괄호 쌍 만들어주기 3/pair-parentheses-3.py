a = list(input())

open_cnt = 0
pairs_cnt = 0
for elem in a:
    if elem == '(':
        open_cnt += 1
    elif elem == ')' and open_cnt > 0:
        pairs_cnt += open_cnt
print(pairs_cnt)


# n = 4
# a = [1, 5, 2, 6]

# result = 0
# for i in range(n):
#     for j in range(i+1, n):
#         s = 0
#         a[i] *= 2
#         a[j] *= 2
#         for k in range(n-1):
#             s += abs(a[k] - a[k+1])
#         result = max(result, s)
#         a[i] //= 2
#         a[j] //= 2
# print(result)