array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

#선택정렬
def arrA():
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]  # 스왚

    print(array)

#삽입정렬
def arrB():
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    print(array)

#퀵정렬
def arrC():
    quick_sort1(array, 0, len(array) -1)
    print(array)
    quick_sort2(array)

#일반적인 퀵소트
def quick_sort1(array, start, end):
    if start >= end:#원소가 1개인 경우 종료
        return
    pivot = start #피벗이 첫번쨰 원소
    left = start +1
    right = end
    while left <= right:
        #피벗보다 큰 데이터를 찾을떄 까지 반복
        while left <= end and array[right] <= array[pivot]:
            left -=1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: #엇갈렷다면 작은 right -= 1 데이터와 피벗을 교체
            array[right], array[pivot] = array[right], array[left]
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort1(array, start, right-1)
    quick_sort1(array, right+1, end)

#파이썬의 장점을 살린 퀵소트
def quick_sort2(array):
    #리스트가 하나의 데이터만 담고있으면 종료
    if len(array)<= 1:
        return array
    pivot = array[0]
    tail = array[1:]#피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]#왼쪽부분
    right_side = [x for x in tail if x > pivot]#오른쪽부분

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체 리스트 반환
    return quick_sort2(left_side) + quick_sort2(right_side)

#계수정렬
def arrD():
    #모든 원소의 값의 0보다 크거나 같다고 가정
    arr = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
    #모든 범위를 포함하는 리스트 선언(모든값은 0으로 초기화)
    count = [0] * (max(arr)+1)

    for i in range(len(arr)):
        count[arr[i]] += 1 #각 데이터에 해당하는 인덱스의 값 증가

    for i in range(len(count)): #리스트에 기록된 정렬 정보 확인
        for j in range(count[i]):
            print(i, end='')#띄어쓰기를 구문으로 등장한 횟수만큼 인덱스 출력


#key를 사용한 정렬
def arrE():
    arr = [('바나나', 2),('사과', 5),('당근', 1)]
    result = sorted(arr, key = setting)

def setting(data):
    return data[1]
