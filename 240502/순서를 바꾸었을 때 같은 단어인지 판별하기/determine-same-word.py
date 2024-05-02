arr1 = list(input())
arr2 = list(input())

arr1.sort()
arr2.sort()

result = "Yes"
for i in range (len(arr1)):
    if arr1[i] != arr2[i]:
        result = "No"
        break
print(result)