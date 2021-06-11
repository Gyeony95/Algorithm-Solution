n, k = map(int, input().split())
count = 0
while True:
    if n == 1:
        break
    while n != 1:
        if n%k == 0:
            break
        else:
            n = n - 1
            count +=1
    n = n/k
    count += 1

print(count)