import re
text = input()

parser = re.findall(r'<p>\sadress\s\d+:\s*(\w+\s\d+)\s*</p>', text)

for i in range(parser.__len__() - 1):
    print(parser[i], ', ', sep='', end='')
print(parser[parser.__len__() - 1])

for i in range(parser.__len__() - 1):
    str1 = parser[i].split(' ')[0]
    str2 = parser[i].split(' ')[1]
    print(str1, ' str.' , str2, ', ', sep='', end='')

print(parser[parser.__len__() - 1].split(' ')[0], ' str.' , parser[parser.__len__() - 1].split(' ')[1], sep='')
