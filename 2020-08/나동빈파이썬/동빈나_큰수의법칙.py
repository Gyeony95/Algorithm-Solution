#55분

n,m,k = map(int, input().split())
data = list(map(int, input().split()))

count = 0
answer = 0
data.sort(reverse=True)

while(True):
    if count == m:
        break
    for i in range(k):
        answer = answer + data[0]
        count = count+1
    if count == m:
        break
    answer = answer + data[1]
    count = count +1

print(str(answer))