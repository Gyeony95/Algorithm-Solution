def solution(n, lost, reserve):
    answer = n - len(lost)

    for i in range(len(lost)):

        if lost[i] != 1 and lost[i]-1 in reserve:#앞자리가 여벌 가져왔으면
            for k in range(len(reserve)):
                if reserve[k] == lost[i]-1:
                    reserve.pop(k)
                    answer += 1
                    break
            continue
        elif lost[i] != n and  lost[i]+1 in reserve:#마지막이 아니고 뒷자애가 체육복 가져왔으면
            for k in range(len(reserve)):
                if reserve[k] == lost[i]+1:
                    reserve.pop(k)
                    answer += 1
                    break
            continue


    return answer


print(solution(8, [1,2, 4, 7], [8]))