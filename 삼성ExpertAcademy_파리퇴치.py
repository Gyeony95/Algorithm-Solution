
def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        printString ="#"+ str(test_case)
        n, m = input().split()
        n = int(n)
        m = int(m)
        mArr = [[int(x) for x in input().split()] for y in range(n)]#이차원배열 쉽게 하기
        realAnswer = 0
        if n == m:
            for i in range(0, n, 1):
                for j in range(0, n, 1):
                    realAnswer = realAnswer + mArr[i][j]
            print(printString + " " + str(realAnswer))
        else:
            for i in range(0, n - m+1, 1):
                for j in range(0, n - m+1, 1):
                    answer = 0
                    for k in range(i, i + m, 1):
                        for kk in range(j, j + m, 1):
                            answer = answer + mArr[k][kk]
                    if realAnswer < answer:
                        realAnswer = answer
            print(printString + " " + str(realAnswer))
soltion()




