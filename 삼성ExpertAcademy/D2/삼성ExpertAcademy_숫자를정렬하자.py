def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        n=input()
        mArr = input().split()
        for i in range(len(mArr)):
            mArr[i] = int(mArr[i])
        mArr.sort()
        answer = "#"+str(test_case)
        for i in mArr:
            answer = answer+" "+str(i)
        print (answer)
soltion()
