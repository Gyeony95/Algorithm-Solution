# 100점
def solution(numbers):
    answer = []
    numbers.sort()
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+ numbers[j])
    answer = list(set(answer))
    answer.sort()
    return answer

print(solution([2,5,0,2,7]))