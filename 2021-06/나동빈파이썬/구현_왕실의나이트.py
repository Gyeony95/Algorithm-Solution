n = input()
arr = list(n)
count = 0

if arr[0] == 'a':
    arr[0] = '1'
elif arr[0] == 'b':
    arr[0] = '2'
elif arr[0] == 'c':
    arr[0] = '3'
elif arr[0] == 'd':
    arr[0] = '4'
elif arr[0] == 'e':
    arr[0] = '5'
elif arr[0] == 'f':
    arr[0] = '6'
elif arr[0] == 'g':
    arr[0] = '7'
elif arr[0] == 'h':
    arr[0] = '8'

arr[0] = int(arr[0])
arr[1] = int(arr[1])

if (arr[0]-2 > 0) and (arr[1]-1 > 0):
    count +=1
if (arr[0]-2 > 0) and (arr[1]+1 <= 8):
    count +=1
if (arr[0]-1 > 0) and (arr[1]-2 > 0):
    count +=1
if (arr[0]-1 > 0) and (arr[1]+2 <= 8):
    count +=1
if (arr[0]+2 <= 8) and (arr[1]-1 > 0):
    count +=1
if (arr[0]+2 <= 8) and (arr[1]+1 <= 8):
    count +=1
if (arr[0]+1 <= 8) and (arr[1]-2 > 0):
    count +=1
if (arr[0]+1 <= 8) and (arr[1]+2 <= 8):
    count +=1


print(count)