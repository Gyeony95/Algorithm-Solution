#내 답안 맞았
n, m = map(int, input().split())
arr = list(map(int, input().split()))


def search(arr, target, start, end):
    count = 0
    mid = (start + end)//2
    for i in arr:
        if i > arr[mid]:
            count = count+ i - arr[mid]
    if count == target:
        return arr[mid]
    elif count > target:
        search(arr, target, mid+1, end)
    else:
        search(arr, target, start, mid-1)
    return None

result = search(arr, m, 0, n-1)

print(result)
