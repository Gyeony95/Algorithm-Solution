#모범 답안 코드
n = int(input())
mList = list(map(int, input().split()))
team = 0
count = 0
mList.sort()

for i in mList:
    count +=1
    if count >= i:
        team +=1
        count = 0

print(team)

