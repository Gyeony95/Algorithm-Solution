
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
                if mArr[i][j] == 1 and j+k <= n:
                    ex = j
                    flag = True
                    for m in range(ex, j+k-1, 1):
                        if mArr[i][m] == 1:
                            pass
                        else:
                            flag = False
                        try:
                            if mArr[i][j+k] == 1:
                                print("mArr[i][j+k]",mArr[i][j+k],i,j+k)
                                flag = False
                            else:
                                pass
                        except:
                            pass
                    if flag:
                        count = count+1
                        break
                print ("mArr[i][j]"+str(mArr[i][j]), i, j)

                print ("count"+str(count))
                if mArr[i][j] == 1 and i + k - 1 <= n:
                    ex = i
                    flag = True
                    for m in range(ex, i + k-1, 1):
                        if mArr[m][j] == 1:
                            pass
                        else:
                            flag = False
                        try:
                            if mArr[i+k][j] == 1:
                                flag = False
                            else:
                                pass
                        except:
                            pass
                    if flag:
                        count = count + 1
                        break

        print (str(count))





                    




soltion()




