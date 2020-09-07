#내가 푼 코드
n = int(input())
mList = list(map(int, input().split()))
team = 0
mMin = min(mList)
count = 0
while mList:
    for i in range(len(mList)):
        if mList[i] == mMin:
            mList.pop(i)
            count += 1
            break
    if count == mMin:
        count = 0
        team += 1
        mMin = min(mList)
    for i in range(len((mList))):
        if len(mList) <= mMin:
            if mList[i] > mMin:
                print(team)
                mList = []
                break