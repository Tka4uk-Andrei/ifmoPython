class Book:
    def __init__(self, name, count):
        self.name__ = name
        self.count__ = count

    def getName(self):
        return self.name__

    def getCount(self):
        return self.count__
    
    def giveBook(self):
        if (self.count__ > 0):
            self.count__ = self.count__ - 1
        return self.count__
    
    def getBook(self):
        self.count__ = self.count__ + 1
        return self.count__

sin = str.split(input())

for i in range (sin.__len__() // 2 - 1):
    book = Book(sin[i*2], int(sin[i*2+1]))
    print (book.getName(), book.getCount(), book.giveBook(), book.getBook(), end=' ')

i = sin.__len__() // 2 - 1
book = Book(sin[i*2], int(sin[i*2+1]))
print (book.getName(), book.getCount(), book.giveBook(), book.getBook())
