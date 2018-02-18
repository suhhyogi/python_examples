# parameter가 2개인 function으로 'message 00님'나오게 하기
# hello 경록님 bye 경록님 message, name
def printMessageWho(message, name):
    result = "{} {}님".format(message, name)
    print(result)

printMessageWho("hello", "kyeongrok")
