def GCD(a, b):
    while True:
        r = a % b
        if r == 0:
            return b
        else:
            a = b
            b = r


def LCM(a, b):
    answer = (a * b) / GCD(a, b)
    return answer


repeat = int(input())
i = 0
while i < repeat:
    a, b = map(int, input().strip().split(' '))

    if a > b:
        answer = LCM(a, b)
    else:
        answer = LCM(b, a)
    answer = int(answer)
    print(answer)
    i += 1
