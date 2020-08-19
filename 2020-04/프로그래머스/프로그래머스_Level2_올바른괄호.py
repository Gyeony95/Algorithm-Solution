def solution(s):
    answer = True

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    mList = list(s)
    openCount = 0
    closeCount = 0;

    for i in mList:
        if i == '(':
            openCount += 1
        elif i == ')':
            closeCount += 1
            if closeCount > openCount:
                return False

    if openCount == closeCount:
        answer = True
    else:
        answer = False

    return answer

solution("()()")