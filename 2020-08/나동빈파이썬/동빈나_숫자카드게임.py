n,m = map(int, input().split())

mArr = []

for i in range(n):
    data = list(map(int, input().split()))
    mArr.append(min(data))
print(max(mArr))
