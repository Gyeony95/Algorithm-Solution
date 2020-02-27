def solution(progresses, speeds):
    answer = []#정답배열
    while True:#무한반복시킴
        toDayReturn = 0#반복문 한번을 하루라고 치고 하루에 리턴되는 작업의 수
        for i in range(0, len(progresses), 1):#매일매일 각 스피드를 각 작업의 진행률에 더해줌, 첫번째꺼 이외가 100을 넘던말던 ㄱㅊ
            progresses[i] = progresses[i] + speeds[i]
        for i in range(0, len(progresses), 1):
            if progresses[i] >= 100:#가장 우선순위 높은 작업의 진행률이 100이상일때
                toDayReturn += 1#오늘 리턴하는 작업에 +1
            else:
                break#맨처음이 100이상이 아니면 의미없으므로 break
        for i in range(0, toDayReturn, 1):#그날 리턴하는거만큼 반복
            progresses.pop(0)#각 배열들의 첫번째값을 pop
            speeds.pop(0)
        if toDayReturn != 0:#오늘 리턴하는 값이 0만 아니면 정답배열에 추가시킴
            answer.append(toDayReturn)
        if len(progresses) == 0:#남은 작업이 0이면 무한반복을 끝냄
            break
    return answer

print(solution([93,30,55], [1,30,5]))