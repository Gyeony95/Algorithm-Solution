#내 답안
n = input()
arr = list(n)
arr2 = []
arr3 = []
for i in arr:
    arr2.append(ord(i))
arr2.sort()
for i in arr2:
    arr3.append(chr(i))
print(''.join(arr3))