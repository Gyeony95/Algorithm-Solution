def soltion():
    T = int(input())
    month = {}
    month[1] = 31
    month[2] = 29
    month[3] = 31
    month[4] = 30
    month[5] = 31
    month[6] = 30
    month[7] = 31
    month[8] = 31
    month[9] = 30
    month[10] = 31
    month[11] = 30
    month[12] = 31
    for test_case in range(1, T + 1):
        printString ="#"+ str(test_case)
        m,d = map(int, input().split())
        count = 0
        for i in range(1,m,1):
            count = count+ month[i]
        count = count+ d
        while(count > 7):
            count= count -7
        print(count)
        if count ==0:
            print(printString,"3")
        elif count ==1:
            print(printString, "4")
        elif count ==2:
            print(printString, "5")
        elif count ==3:
            print(printString, "6")
        elif count ==4:
            print(printString, "0")
        elif count ==5:
            print(printString, "1")
        elif count ==6:
            print(printString, "2")

soltion()