class Product:
    def __init__(self, c_name, c_code):
        self.c_name = c_name
        self.c_code = c_code


p1 = Product("codetree", 50)

name, code = input().split()
p2 = Product(name, int(code))

print(f"product {p1.c_code} is {p1.c_name}")
print(f"product {p2.c_code} is {p2.c_name}")