def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        printString ="#"+ str(test_case)
        n,k = map(int, input().split())
        tArr = map(int,input().split())
        tArr = list(tArr)
        mArr = []
        for i in range(1,n+1,1):
            mArr.append(i)
        for i in range(len(tArr)):
            for j in range(len(mArr)):
                if tArr[i] == mArr[j] :
                    mArr.pop(j)
                    break
        answer = ""
        for i in mArr:
            answer = answer +" "+str(i)
        print(printString+answer)
soltion()