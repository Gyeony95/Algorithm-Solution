n = int(input())
arr = []
for i in range(n):
    arr.append(str(input()))

count = 0
for i in arr:
    isTrue = True
    arr2 = []
    a = list(i)
    for j in a:
        if(j in arr2):
            if(j != arr2[-1]):
                isTrue = False
        else:
            arr2.append(j)
    if(isTrue):
        count +=1
print(count)