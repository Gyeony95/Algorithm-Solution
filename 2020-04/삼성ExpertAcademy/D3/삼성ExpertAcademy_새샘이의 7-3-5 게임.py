from itertools import combinations
def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        printString ="#"+ str(test_case)
        mArr = list(map(int,input().split()))
        mList = list(combinations(mArr,3))
        answer = []
        for i in mList:
            answer.append(i[1]+i[0]+i[2])
        answer = set(answer)
        answer = list(answer)
        answer.sort(reverse = True)

        print(printString,list(answer)[4])



soltion()




