
def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        n = input().split()
        mList = []
        for i in range(len(n)):
            mList.append(int(n[i]))

        mList.sort()
        mList.pop()
        mList.pop(0)
        answerInt = 0
        for i in range(0,len(mList),1):
            answerInt = answerInt+ mList[i]
        print("#"+str(test_case)+" "+str(round(answerInt/len(mList))))




soltion()




