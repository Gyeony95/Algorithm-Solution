n = int(input())
arr = []
answer = []

for i in range(n):
    x, y = map(int,input().split())
    arr.append([x,y])
    answer.append(1)

print(arr)
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if i != j:
            if arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
                answer[j] = answer[j]+1
            elif arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                answer[i] = answer[i]+1

for i in range(len(answer)):
    if(i == len(answer)-1):
        print(answer[i])
    else:
        print(answer[i], end=' ')
