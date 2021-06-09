# 100점
NOTATION = '0123456789ABCDEF'

def solution(n):
    answer = 0
    num = numeral_system(n,3)
    num2 = str(num)[::-1]

    base = 3
    answer = 0
    for idx, i in enumerate(num2[::-1]):
        answer += int(i) * (base ** idx)

    return answer

def numeral_system(number, base):
    q, r = divmod(number, base)
    n = NOTATION[r]
    return numeral_system(q, base) + n if q else n

print(solution(125))
