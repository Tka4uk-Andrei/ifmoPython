a = input()

b = tuple()
for i in range(10):
    if (a.find(str(i)) != -1):
        b+=(i,)

print (b)
b = b[::-1]
print (b)
