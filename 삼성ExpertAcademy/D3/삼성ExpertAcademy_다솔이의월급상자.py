def soltion():
    T = int(input())

    for test_case in range(1, T + 1):
        n= int(input())
        answer = 0
        for i in range(n):
            aArr = input().split()
            answer = float(answer) + float(aArr[0])*float(aArr[1])

        print("#"+str(test_case),'%.6f' % answer)
soltion()





