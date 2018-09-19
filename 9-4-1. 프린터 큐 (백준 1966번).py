printOrder=0
testCaseNum = int(input())


for i in range(testCaseNum):
    N, M = input().split()
    N = int(N)
    M = int(M)
    importance=[]
    importance = input().split()
    print("*********")
    print(importance)
    # importance[M] = int(importance[M]) + 0.5
    # importance[M] = str(importance[M])

    for j in range(N):


        for k in range(1, len(importance)):
            if importance[0] < importance [k]:
                temp = importance[0]
                importance.remove(temp)
                importance.append(temp)
                print(importance)
        print("--뒤로 넘기기 완료--")
        print(importance)
        printOrder += 1
        print(importance[0],"출력 완료   ","출력 순서(printOrder):", printOrder)
        importance.remove(importance[0])
        print(importance)
        print("------출력 완료------")
