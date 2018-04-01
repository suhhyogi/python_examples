def myRange(n):
    i = 0
    while i < n:
        yield i

print(myRange(10))

