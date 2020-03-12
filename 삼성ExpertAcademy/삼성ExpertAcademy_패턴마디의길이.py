def soltion():
    T = int(input())

    for test_case in range(1, T + 1):
        printString ="#"+ str(test_case)
        mStr = str(input())
        mStr = list(mStr)
        testArr  = []
        for i in range(0, len(mStr), 1):
            testArr.append(mStr[i])
            testArrcount = len(testArr)
            isTrue = True
            for j in range(0, len(mStr), 1):
                k = j % testArrcount
                if mStr[j] == testArr[k]:
                    pass
                else:
                    isTrue = False
            if isTrue:
                a = len(testArr)
                printString = printString+ " "+str(a)
                print(printString)
                break

soltion()




