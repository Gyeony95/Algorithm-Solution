def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        mSudoku = [[int(x) for x in input().split()] for y in range(9)]
        isTrue = True
        for i in range(9):
            check1 = []
            check2 = []
            for j in range(9):
                check3 = []
                check1.append(mSudoku[i][j])
                check2.append(mSudoku[j][i])
                if i % 3 ==0 and j % 3 == 0:
                    m = i;n=j
                    for q in range(m,m+3,1):
                        for w in range(n,n+3,1):
                            check3.append(mSudoku[q][w])
                    if checkArr(check3) == False:
                        print ("#" + str(test_case), 0)
                        isTrue = False
                        break
            if isTrue:
                if checkArr(check1) == False:
                    print ("#" + str(test_case), 0)
                    isTrue = False
                    break
                elif checkArr(check2) == False:
                    print ("#" + str(test_case), 0)
                    isTrue = False
                    break
            else:
                break
        if isTrue:
            print ("#" + str(test_case), 1)


def checkArr(arr):
    arr.sort()
    for i in range(1,10,1):
        if i != int(arr[i-1]):
            return False
    return  True
soltion()
