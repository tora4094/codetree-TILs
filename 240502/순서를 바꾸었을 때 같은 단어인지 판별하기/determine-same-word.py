arr1 = list(input())
arr2 = list(input())

arr1.sort()
arr2.sort()

result = "Yes"

if len(arr1) == len(arr2):
    for i in range (len(arr1)):
        if arr1[i] != arr2[i]:
            result = "No"
            break
            
print(result)