
def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        n, k = input().split()
        n = int(n)
        k = int(k)
        mArr = [[int(x) for x in input().split()] for y in range(n)]#이차원배열 쉽게 하기

        count = 0
        for i in range(n):
            for j in range(n):
                isTrue = True
                if j <= n-k:#가로로 ㅇㅇ
                  if mArr[i][j] == 1:
                    for m in range(j,j+k,1):
                        if mArr[i][m] == 0:
                            isTrue = False
                    try:
                        if mArr[i][j + k] != 1:
                            pass
                        else:
                            isTrue = False
                    except:
                        pass
                    try:
                        if j-1 >=0:
                            if mArr[i][j - 1] != 1:
                                pass
                            else:
                                isTrue = False

                    except:
                        pass
                    if isTrue:
                        count += 1

                isTrue = True
                if i <= n-k:#세로로 ㅇㅇ
                  if mArr[i][j] == 1:
                    for m in range(i,i+k,1):
                        if mArr[m][j] == 0:
                            isTrue = False
                    try:
                        if mArr[i+k][j] != 1:
                            pass
                        else:
                            isTrue = False
                    except:
                        pass
                    try:
                        if i - 1 >= 0:
                            if mArr[i - 1][j] != 1:
                                pass
                            else:
                                isTrue = False
                    except:
                        pass
                    if isTrue:
                        count += 1

        print ("#"+str(test_case),str(count))



soltion()




