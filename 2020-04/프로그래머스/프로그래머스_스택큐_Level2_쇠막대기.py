def solution(arrangement):
    answer = 0
    arrangement = list(arrangement)#문자열을 리스트로 만듦
    stick_count = 0#총 막대기의 수
    stick_stack = 0#레이저에 관통되는 막대기의 수
    while True:
        if arrangement[-1] == ')':#끝에서부터 )일때
            arrangement.pop()#확인했으니 팝
            if arrangement[-1] == '(':#)다음 (이면 레이저임
                answer += stick_stack#스틱스택의 수만큼 정답에 추가
                arrangement.pop()#레이저는 () 문자 두개짜리니까 하나더 팝
            elif arrangement[-1] == ')':#)다음 )이면 이전 )는 막대기의 끝부분이라는 의미
                stick_stack += 1#관통당할 막대기 +1
                stick_count += 1#총막대기 +1
        elif arrangement[-1] == '(':#끝에서부터 (일때
            arrangement.pop()#확인했으니 팝
            stick_stack += -1#막대기의 왼쪽부분으로 판단하고 관통당할 막대기 카운트에서 -1 해줌
        if len(arrangement) ==0:#더이상 문자열이 존재하지않으면 break
            break
    return answer+stick_count

solution("()(((()())(())()))(())")