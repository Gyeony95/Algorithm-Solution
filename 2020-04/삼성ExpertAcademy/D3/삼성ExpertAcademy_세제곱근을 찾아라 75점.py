#75점짜리 코드
def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        printString ="#"+ str(test_case)
        n = int(input())

        if n == 1:
            print(printString +" "+str(1))
            continue
        for i in range(1, n,1):
            if i*i*i == n:
                print(printString +" "+str(i))
                break
            elif i*i*i > n:
                print(printString +" "+str(-1))
                break
soltion()