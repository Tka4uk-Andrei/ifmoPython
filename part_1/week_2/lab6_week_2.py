perim = lambda a,b: (2 * (a + b))
square = lambda a,b: (a * b)

a = int(input())
b = int(input())

print(0, square (a, b))
print(1, perim (a, b))
print([square (a, b), perim (a, b)])
print(square (a, b), perim (a, b))