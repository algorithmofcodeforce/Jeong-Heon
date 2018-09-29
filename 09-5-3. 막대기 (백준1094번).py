goalLen = int(input())
answer = 0

while goalLen > 0:
    if (goalLen % 2) == 1:
        answer += 1
    goalLen /= 2
    goalLen = int(goalLen)
print(answer)
