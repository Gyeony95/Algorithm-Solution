def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        printString ="#"+ str(test_case)

        mArr = [input() for y in range(5)]

        maxlen = 0
        for i in mArr:
            if len(i) > maxlen:
                maxlen = len(i)

        mArr2 = [["/"]*maxlen for y in range(5)]

        for i in range(5):
            for j in range(maxlen):
                mList = list(mArr[i])
                if len(mList) == maxlen:
                    mArr2[i] = mList
                    break
                else:
                    if j == len(mList):
                        break
                    mArr2[i][j] = mList[j]


        answer = ""
        for k in range(maxlen):
            for i in range(5):
                for j in range(maxlen):
                    if k == j:
                        if mArr2[i][j] != "/":
                            answer = answer + mArr2[i][j]


        print (printString,answer)

soltion()