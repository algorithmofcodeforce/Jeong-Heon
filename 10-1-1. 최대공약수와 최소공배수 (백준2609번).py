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
    answer = int(answer)
    return answer


a, b = map(int, input().strip().split(' '))

if a > b:
    print(GCD(a, b))
    print(LCM(a, b))
else:
    print(GCD(b, a))
    print(LCM(b, a))

