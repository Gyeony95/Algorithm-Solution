def solution(array, commands):
    answer = [None] * len(commands)
    for r in range(0, len(commands), 1):
        arr = []
        i = commands[r][0]
        j = commands[r][1]
        k = commands[r][2]
        for m in range(i-1, j):
            arr.append(array[m])
        arr.sort()
        answer[r] = arr[k - 1]
    return answer

arr1 = [1, 5, 2, 6, 3, 7, 4]
arr2 = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
solution(arr1, arr2)