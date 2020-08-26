n, k = map(int, input().split())

arrA = input().split()
arrB = input().split()
arrA.sort()
arrB.sort()

for i in range(k):
    if min(arrA) < max(arrB):
        arrA.pop(0)
        arrA.append(arrB.pop())

#아래코드 sum으로 대체 가능
answer = 0
for i in range(len(arrA)):
    answer = answer + int(arrA[i])

print(answer)
