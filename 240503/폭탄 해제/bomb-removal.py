class Bomb:
    def __init__(self,code,color,second=1):
        self.code = code
        self.color = color
        self.second = second

code, color, second = tuple(input().split())
b1 = Bomb(code,color,int(second))
print(f"code : {b1.code}")
print(f"color : {b1.color}")
print(f"second : {b1.second}")