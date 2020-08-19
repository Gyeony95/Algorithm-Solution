def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        n = int(input())
        mArr = list(map(int, input().split()))
        answer = -1
        for i in range(len(mArr)):
            for j in range(i+1, len(mArr), 1):
                x = mArr[i]*mArr[j]
                sArr = list(str(x))
                isDanjo = True
                for i2 in range(len(sArr)):
                    try:
                        if sArr[i2] <= sArr[i2+1]:
                            pass
                        else:
                            isDanjo = False
                    except:
                        pass
                if isDanjo:
                    if answer < x:
                        answer = x
        print("#"+str(test_case),answer)
soltion()
