class Student:
    def __init__(self,h,w,number):
        self.h = h
        self.w = w
        self.number = number

n = int(input())

arr = []

for i in range(1, n+1):
    h, w = tuple(map(int,input().split()))
    arr.append(Student(h,w,i))

arr.sort(key=lambda s : (s.h,-s.w))

for s in arr:
    print(s.h,s.w,s.number)