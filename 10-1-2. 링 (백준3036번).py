def simpleFraction(b, a):
    if b > a:
        k =a
    else:
        k =b
    i=2
    while i <=k:
        if (b % i == 0) and (a%i ==0):
            b = int(b/i)
            a = int(a / i)
            i = 2
        else:
            i +=1
    print("%d/%d" %(b, a))

num = int(input())
r = input()

l = r.split()
j = 0
for i in l:
    i = int(i)
    l[j] = i
    j +=1


for j in range(num-1):
    simpleFraction(l[0],l[j+1])