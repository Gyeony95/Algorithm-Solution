#정답 보고 푼거 복기
def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2+1):
        prev = s[0:step]
        count = 1
        mString = ''
        for i in range(step, len(s), step):
            if prev == s[i:i+step]:
                count +=1
            else:
                if count != 1:
                    mString += str(count) +prev
                else:
                    mString += prev
                prev = s[i:i + step]
                count = 1
        if count != 1:
            mString += str(count) + prev
        else:
            mString += prev
        answer = min(len(mString), answer)
    return answer

print(solution('aabbaccc'))
