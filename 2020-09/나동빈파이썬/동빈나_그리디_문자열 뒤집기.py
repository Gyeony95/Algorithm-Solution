#내가푼 코드
mList = list(map(int, input()))
one = 0
zero = 0
num = mList[0]

if mList[0] == 0:
    zero += 1
else:
    one += 1


for i in range(len(mList)):
    if mList[i] == num:
        pass
    else:
        print(mList[i],i)
        if mList[i] == 1:
            num = 1
            zero += 1
        else:
            num = 0
            one += 1

print(min(one, zero))