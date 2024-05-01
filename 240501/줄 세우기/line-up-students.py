class Student:
    def __init__(self,h,w,number):
        self.h = h
        self.w = w
        self.number = number

n = int(input())

students = []

for i in range(1, n + 1):
    h,w = tuple(map(int,input().split()))
    students.append(Student(h,w,i))

students.sort(key=lambda s : (-s.h, -s.w, s.number))

for st in students:
    print(st.h, st.w, st.number)