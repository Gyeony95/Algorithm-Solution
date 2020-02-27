def solution(priorities, location):
    count =0 #정답 파라미터
    priorities = list(priorities)#스택으로 쓰기위해 리스트로 만듦
    while True:
        while True:
            flag = False#플래그
            for i in range(0, len(priorities), 1):
                if i != 0 and priorities[0] < priorities[i]:#인덱스 0값 뒤에 더 큰수가 있으면
                    flag = True#플래그 트루
                    priorities.append(priorities[0])#앞에꺼 뒤에 추가하고
                    priorities.pop(0)#앞에꺼 뺌
                    if location != 0:#인덱스가 0이면 맨뒤 인덱스로 넣어줌
                        location += -1
                    else:#아니면 그냥 -1
                        location = len(priorities) - 1
            if flag:#플래그 트루면 와일문 다시반복
                pass
            else:#의미없는 반복 하고있으면 와일문 깨고나감
                break
        if location == 0:#맨앞이 가장 큰값인데 로케이션이 0이면 리턴
            return count+1
        else:#아니면 그냥 앞에꺼 빼주고 카운트 올려줌
            priorities.pop(0)
            location += -1
            count += 1
print (solution([1, 1, 9, 1, 1, 1], 0))