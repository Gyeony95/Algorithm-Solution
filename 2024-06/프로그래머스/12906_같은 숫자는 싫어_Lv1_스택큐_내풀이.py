# 정확성 통과, 효율성 불통과
def solution(arr):
    remove_idx = []
    for i in range(len(arr)):
        if i != 0:
            if arr[i] == arr[i-1]:
                remove_idx.append(i)

    remove_idx.reverse()
    for i in remove_idx:
        arr.pop(i)
    return arr

print(solution([1,1,3,3,0,1,1]))