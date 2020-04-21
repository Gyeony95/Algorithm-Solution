def soltion():
    T = int(input())
    #1부터 최대값까지의 세제곱들의 해시맵을 만들어놓음
    mDict = {}
    for i in range(pow(10, 6) + 1):
        mDict[pow(i, 3)] = i
    keys = mDict.keys()
    for test_case in range(1, T + 1):
        printString ="#"+ str(test_case)
        n = int(input())
        if n in keys:
            print(printString + " " + str(mDict[n]))
        else:
            print(printString + " " + str(-1))
soltion()