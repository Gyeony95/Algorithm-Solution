n, m = map(int, input().split())
arr = [[int(x) for x in input().split()] for _ in range(n)]

answer = 0
for i in range(n):
    answer = max(answer, min(arr[i]))

print(answer)