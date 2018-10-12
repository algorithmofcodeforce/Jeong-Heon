# 경우의수: 36
import random

l = []
for i in range(9):
    a = int(input())
    l.append(a)

while True:

    answerList = []
    randomList = []
    sum = 0

    for i in range(7):

        while True:
            b = random.randint(0, 8)
            if b in randomList:
                pass
            else:
                randomList.append(b)
                break

        answerList.append(l[b])
        sum += l[b]
    # print(answerList, "<< ", sum, ">>")
    if sum == 100:
        break

for i in range(7):
    answerList.sort()
    print(answerList[i])
