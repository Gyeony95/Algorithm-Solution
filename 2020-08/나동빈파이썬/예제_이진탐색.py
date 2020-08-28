#재귀함수를 이용한 이진탐색
def binary_search1(arr, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    #찾은경우 중간점 인덱스 반환
    if arr[mid] == target:
        return mid
    #중간값보다 찾고자하는 값이 작을경우
    elif arr[mid] > target:
        return binary_search1(arr, target, start, mid-1)
    #중간값보다 찾고자하는 값이 큰 경우
    else:
        return binary_search1(arr, target, mid+1, end)

#반복문을 이용한 이진탐색
def binary_search2(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        # 찾은경우 중간점 인덱스 반환
        if arr[mid] == target:
            return mid
        # 중간값보다 찾고자하는 값이 작을경우
        elif arr[mid] > target:
            end = mid-1
        # 중간값보다 찾고자하는 값이 큰 경우
        else:
            start = mid+1


# n과 target을 입력받기
n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

# 이진탐색 수행결과 출력
result = binary_search1(arr, target, 0, n - 1)#binary_search2도 똑같이 호출해주면 됨
if result == None:
    print('원소 없음')
else:
    print(result + 1)

