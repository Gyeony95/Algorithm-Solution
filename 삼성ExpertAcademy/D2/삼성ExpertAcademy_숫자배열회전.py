def soltion():
    T = int(input())

    for test_case in range(1, T + 1):
        print("#"+str(test_case))#맨처음에 몇번째 테스트 케이스인지 출력
        nextCase = int(input())
        mArr = [[int(x) for x in input().split()] for y in range(nextCase)]
        str90 = ""
        str180 = ""
        str270 = ""
        for i in range(0, nextCase, 1):
            for j in range(nextCase-1, -1, -1):
                str90 = str90+str(mArr[j][i])
        for i in range(nextCase-1, -1, -1):
            for j in range(nextCase-1, -1, -1):
                str180 = str180+str(mArr[i][j])
        for i in range(nextCase-1, -1, -1):
            for j in range(0, nextCase, 1):
                str270 = str270+str(mArr[j][i])
        str90 = list(str90)
        str180 = list(str180)
        str270 = list(str270)
        for k in range(nextCase):
            printStr = ""
            for i in range(nextCase):
                for j in range(nextCase):
                    if i == 0:
                        printStr = printStr + str90[j+k*nextCase]
                    elif i == 1:
                        printStr = printStr + str180[j+k*nextCase]
                    elif i == 2:
                        printStr = printStr + str270[j+k*nextCase]
                printStr = printStr + " "
            print(printStr)

soltion()





