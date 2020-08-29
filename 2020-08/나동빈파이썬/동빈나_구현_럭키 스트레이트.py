#내 답안
n = input()
arr = list(n)
a = 0
b = 0
for i in range(len(n)//2):
    a += int(arr[i])
    b += int(arr[i+len(n)//2])

if a == b:
    print('LUCKY')
else:
    print('READY')