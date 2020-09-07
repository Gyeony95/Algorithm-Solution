n, m = map(int, input().split())
mList = list(map(int, input().split()))
mList.sort()
count = 0

for i in range(len(mList)):
    for j in range(i,len(mList)):
        if i != j and mList[i] != mList[j]:
            count += 1

print(count)
