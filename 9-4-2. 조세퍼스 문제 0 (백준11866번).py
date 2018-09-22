n, m = map(int, input().split())

list = []

for i in range(1, n + 1):
    list.append(i)

answer = []

for k in range(n):
    for j in range(m - 1):
        list.append(list[0])
        list.remove(list[0])
    answer.append(list[0])
    list.remove(list[0])

answerString = ""

print("<", end="")

for l in range(len(answer)):
    answerString += str(answer[l])
    if not ((l+1) == len(answer)):
        answerString += ", "
    else:
        answerString += ">"
print(answerString)
