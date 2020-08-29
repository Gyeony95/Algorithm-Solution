n = int(input())
arr1 = list(map(int,input().split()))
arr1 = sorted(arr1)
m = int(input())
arr2 = list(map(int,input().split()))

def search(target, start, end):
    mid = (start+end)//2
    if start> end:
        return False

    if arr1[mid] > target:
        return search(target, start, mid-1)
    elif arr1[mid] < target:
        return search(target, mid+1, end)
    else:
        return True


for i in arr2:
    if search(i, 0, len(arr2) - 1):
        print(1)
    else:
        print(0)

