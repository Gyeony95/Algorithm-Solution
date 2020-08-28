#모범답안
def binary_search1(arr, target, start ,end):
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            binary_search1(arr, target, start, mid-1)
        else:
            binary_search1(arr, target, mid+1, end)
    return None

n = int(input())
arr = list(map(int,input().split()))
arr.sort()#이진탐색을 위해 정렬
m = int(input())
x = list(map(int,input().split()))

for i in x:
    result = binary_search1(arr, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
