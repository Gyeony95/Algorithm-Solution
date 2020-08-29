answer = 0

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer

def dfs(arr, target, i, total):

    if i == len(arr):
        if total == target:
            global answer
            answer += 1
        return
    dfs(arr, target, i+1, total + arr[i])
    dfs(arr, target, i+1, total - arr[i])


print(solution([1,1,1,1,1], 3))