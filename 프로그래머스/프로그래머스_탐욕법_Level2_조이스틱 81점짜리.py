def solution(name):
    mName = list(name)
    answer = 0
    if mName[1] == 'A':
        mName.pop(1)
    for i in mName:
        if ord(i) > 77:
            answer = answer+ (91-ord(i))
        else:
            answer = answer + (ord(i)-65)
    answer = answer + len(mName)-1
    return answer


print(solution("JEROEN"))