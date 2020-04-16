from collections import OrderedDict
import hashlib

class Libriary:
    def __init__(self, init_str):
        self.lib = dict()
        for i in range (init_str.__len__() // 2):
            if (not init_str[i * 2] in self.lib):
                self.lib.update({init_str[i*2]: int(init_str[i*2+1])})
            else:
                self.lib.pop(init_str[i * 2])


class Book:
    def __init__(self, name, count):
        self.name__ = name
        self.count__ = count

    def getName(self):
        return self.name__

    def getCount(self):
        return self.count__

    def getHash(self, type):
        if (type == 'md5'):
            return hashlib.md5(self.name__.encode()).hexdigest()
        if (type == 'sha1'):
            return hashlib.sha1(self.name__.encode()).hexdigest()
        if (type == 'sha224'):
            return hashlib.sha224(self.name__.encode()).hexdigest()
        if (type == 'sha256'):
            return hashlib.sha256(self.name__.encode()).hexdigest()
        if (type == 'sha384'):
            return hashlib.sha384(self.name__.encode()).hexdigest()
        if (type == 'sha512'):
            return hashlib.sha512(self.name__.encode()).hexdigest()

    def print(self, type):
        print(type, self.getHash(type), end='')


sin = str.split(input())
hashType = input()

lib = Libriary(sin)

orderedLib = OrderedDict(sorted(lib.lib.items()))

for key in orderedLib.keys():
    print(key, lib.lib[key])

i = 0
for key in orderedLib.keys():
    Book(key, lib.lib[key]).print(hashType)
    if (i < lib.lib.keys().__len__() - 1):
        print(end=' ')
    i += 1
