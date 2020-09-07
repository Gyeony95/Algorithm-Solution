#내가푼 코드
mList = list(map(int, input()))
num = 0
for i in range(len(mList)):
    if num + mList[i] >= num * mList[i]:
        num = num + mList[i]
    else:
        num = num * mList[i]

print(num)
