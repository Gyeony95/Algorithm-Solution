
def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        n = input()
        n = int(n)

        printString ="#"+ str(test_case)
        print(printString)
        mArr = [1]
        for i in range(0, n, 1):
            exArr = []
            for j in range(0, len(mArr), 1):
                if j +1 == len(mArr):
                    mArr.append(1)
                    exArr.append(1)
                    break
                elif j ==0:
                    exArr.append(1)
                else:
                    exArr.append(mArr[j-1]+mArr[j])
            mArr = exArr
            mArr.append(1)
            answr = "1"
            for i in range(1, len(mArr)-1, 1):
                answr = answr + " " + str(mArr[i])
            print (answr)





soltion()




