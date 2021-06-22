
n = int(input())
nList = list(map(int, input().split()))

m = int(input())
mList = list(map(int, input().split()))

nList = sorted(nList)

def binary_search(arr, start, target, end):
    if start > end:
        return None
    mid = (start+end)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, start, target, mid-1)
    elif arr[mid] <target:
        return binary_search(arr, mid+1, target, end)



answer = []
for i in range(m):
    if (binary_search(nList, 0, mList[i], len(nList) - 1)) is None:
        answer.append('no')
    else:
        answer.append('yes')

print(answer)
