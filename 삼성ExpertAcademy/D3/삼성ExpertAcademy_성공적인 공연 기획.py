def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        printString ="#"+ str(test_case)
        mArr = list(input())
        count = 0#기립박수 하는사람
        answer = 0#고용한 사람
        if mArr[0] == '0':
            answer = answer+1
            count = count+1
        else:
            count = count + int(mArr[0])
        mArr.pop(0)
        for i in range(len(mArr)):
            if count >= i+1:
                pass
            else:
                answer = answer + 1
                count = count + 1
            count = count+int(mArr[i])
        print (printString,answer)
soltion()