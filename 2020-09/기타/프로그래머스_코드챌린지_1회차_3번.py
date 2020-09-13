#0점 ㅜㅜ

mArr = []

def solution(a):
    answer = 0
    dfs(a, True)
    global mArr
    mArr = list(set(mArr))
    answer = len(mArr)

    return answer


def dfs(arr, chance):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            print(i, j, arr)
            if len(arr) == 1:
                mArr.append(arr[0])

            if i == j:
                continue

            if arr[i] > arr[j]:
                if chance:
                    arr1 = list(arr)
                    arr1.pop(i)
                    arr2 = list(arr)
                    arr2.pop(j)
                    dfs(arr1, True)
                    dfs(arr2, False)
                else:
                    arr1 = list(arr)
                    arr1.pop(i)
                    dfs(arr1, False)
            else:
                if chance:
                    arr1 = list(arr)
                    arr1.pop(i)
                    arr2 = list(arr)
                    arr2.pop(j)
                    dfs(arr1, False)
                    dfs(arr2, True)
                else:
                    arr1 = list(arr)
                    arr1.pop(j)
                    dfs(arr1, False)


print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))