n = int(input())
mList = list(map(int, input()))
mList.sort()

target = 1
for i in mList:
    if target < i:
        break
    target += i

print(target)