# Считать несколько имен людей одной строкой, записанных латиницей, через пробел, например:
# «Anna Maria Peter».
# Вывести их одной строкой в порядке возрастания «Anna Maria Peter».
# Вывести их одной строкой в порядке убывания «Peter Maria Anna».

s = input()
s1 = s.split()

s1.sort()
strr = " ".join(str(x) for x in s1)
print(strr)

s1.reverse()
strr = " ".join(str(x) for x in s1)
print(strr)
