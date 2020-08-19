def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        printString ="#"+ str(test_case)
        n,q = map(int,input().split())
        mArr = [0]*n
        for i in range(1,q+1,1):
            first,second = map(int,input().split())
            for j in range(first-1, second,1):
                mArr[j] = i
        answer = ""
        for i in mArr:
            answer = answer+" "+str(i)
        print(printString+answer)
soltion()
