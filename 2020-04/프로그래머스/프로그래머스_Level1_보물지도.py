def solution(n, arr1, arr2):
    answer = []
    mMap = [["a"] * n for i in range(n)]

    for i in range(0, n, 1):
        mList = list(format(arr1[i], 'b'))
        while len(mList) != n:
            mList.insert(0,'0')
        for j in range(n):
            if mList[j] == '1':
                mMap[i][j] = '#'
            else:
                mMap[i][j] = ' '
        mList = list(format(arr2[i], 'b'))
        while len(mList) != n:
            mList.insert(0, '0')
        for j in range(n):
            if mList[j] == '1' or mMap[i][j] == '#':
                mMap[i][j] = '#'
            elif mList[j] == '0':
                mMap[i][j] = ' '
    for i in range(n):
        answerString = ''
        for j in range(n):
            answerString= answerString+mMap[i][j]
        answer.append(answerString)
    return answer
print(solution(6,	[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))

#format(str_ex, 'b'), 이진수로 만드는 법임 01001 이런 식으로 나옴
#format(str_ex, '#b')이렇게 하거나  ,b = bin(value)이렇게 하면  0b111100 이런식으로 나옴
#16진수랑 8진수는 위에 알파벳을 각각 x랑 o로 하면됨