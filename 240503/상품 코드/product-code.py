class Product:
    def __init__(self,name="",code=50):
        self.name = name
        self.code = code
    def print(self):
        print(f"product {self.code} is {self.name}")

    
p1 = Product()
p2 = Product()

p1.name = "codetree"

name, code = tuple(input().split())
p2.name = name
p2.code = code

p1.print()
p2.print()