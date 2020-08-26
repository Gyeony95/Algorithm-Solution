n = int(input())
arr = []

def mSort(data):
    return data[1]

for i in range(n):
    input_data = input().split()
    arr.append((input_data[0], int(input_data[1])))
result = sorted(arr, key = mSort)
for i in range(n):
    print(result[i][0], end=' ')

