answer = []  # 정답배열

def solution(progresses, speeds):






    return answer




def reject(progresses):
    count = 0

    copy = progresses[:]
    for i in progresses:
        if i >= 100:
            count += 1
            copy.pop(i)


print(solution([93, 30, 55], [1, 30, 5]))
