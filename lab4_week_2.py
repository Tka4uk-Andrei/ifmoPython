def f (a, b, name):
    def perim(a, b):
        return (2 * (a + b))
    def square(a, b):
        return (a * b)
    
    if name == 'perim':
        return perim(a, b)
    elif name == 'square':
        return square(a, b)

a = int(input())
b = int(input())

print(f(a, b, name="square"), f(a, b, name="perim"))
