def printMultiplication(dan):
    for item in range(1, 10):
        result = "{} * {} = {}".format(dan, item, item * dan)
        print(result)

for item in range(2, 10):
    printMultiplication(item)
    print("-------------")


