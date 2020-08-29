#내답안 정답
n = int(input())
arr1 = list(map(int,input().split()))
arr1 = sorted(arr1)
m = int(input())
arr2 = list(map(int,input().split()))

def search(arr, target, start, end):
    while(start <= end):
        mid = (start+end)//2
        if target == arr[mid]:
            return 1
        elif target > arr[mid]:
            start = mid+1
        else:
            end = mid-1
    return 0

for i in arr2:
    print(search(arr1, i, 0, n-1), end=' ')