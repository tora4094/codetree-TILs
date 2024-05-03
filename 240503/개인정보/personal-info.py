class People:
    def __init__(self,name,h,w):
        self.name = name
        self.h = h
        self.w = w
n = 5
arr = []
for _ in range(n):
    name, h, w = tuple(input().split())
    arr.append(People(name,int(h),float(w)))

arr.sort(key=lambda p : p.name)
print("name")
for p in arr:
    print(p.name,p.h,p.w)

print()

print("height")
arr.sort(key=lambda p : -p.h)
for p in arr:
    print(p.name,p.h,p.w)