rList = []
answerList = []

for i in range(10):
    a = int(input())
    r = a % 42
    if r not in answerList:
        answerList.append(r)
print(len(answerList))
