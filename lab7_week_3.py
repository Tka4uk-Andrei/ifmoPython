import hashlib

s = input()

arr = []

print('md5', hashlib.md5(s.encode()).hexdigest())
print('sha1', hashlib.sha1(s.encode()).hexdigest())
print('sha224', hashlib.sha224(s.encode()).hexdigest())
print('sha256', hashlib.sha256(s.encode()).hexdigest())
print('sha384', hashlib.sha384(s.encode()).hexdigest())
print('sha512', hashlib.sha512(s.encode()).hexdigest())
