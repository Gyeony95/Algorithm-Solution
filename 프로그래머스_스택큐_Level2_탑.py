def solution(heights):
    answer = []#정답배열
    stack = []#입시로 쌓을 스택으로 쓸 배열
    for i in heights:#높이만큼 반복하면서
        stack.append(i)#스택에 요소를 쌓고
        answer.append(0)#정답배열을 0으로 채움
    for i in range(len(heights)-1, -1, -1):#배열을 뒤에서부터 순차적으로 모두 순회
        exStack = list(stack)#임시로쓸 배열임 -> 원래배열을 복제
        for j in range(i-1, -1, -1):#스택의 길이보다 한번더 앞에서부터 순환시킴 자기자신은 비교할 필요 없기떄문
            if exStack[j] > stack[i]:#신호를 보낸 탑보다 앞에탑 높이가 더 크면
                answer[i] = j + 1#해당하는 인덱스에 정답배열에 넣음
                stack.pop()#이미 처리해버린 탑은 팝 함
                break
    return answer


print(solution([6,9,5,7,4]))