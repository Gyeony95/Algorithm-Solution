from itertools import permutations


def solution(numbers):
    answer = 0

    new_s = list(numbers)
    #최소 길이가 2인 문자열들부터 len(numbers)인 문자열들까지 반복
    for i in range(2, len(numbers) + 1):
        pm = list(permutations(numbers, i))
        #permutations(numbers, i) = numbers로 만들수 있는 i길이의 순열조합을 리턴함
        #ex) "17"이면 [('1', '7'), ('7', '1')]
        for j in pm:#산출된 순열들만큼 반복
            if len(j) <= len(numbers):
                new_s.append(''.join(j))
                #''.join(j) = j가 지금 배열('1', '7')인데 문자열로 붙여버리는 기능
    new_s = list(set([int(x) for x in new_s]))#문자열값을 인트로바꿔서 넣어주는 부분

    #1이나 0이 있으면 다지움, 소수에 해당되지 않기때문
    if new_s.count(1):
        new_s.remove(1)
    if new_s.count(0):
        new_s.remove(0)

    #남은 리스트길이만큼 반복
    for x in new_s:
        i = 2
        while i * i <= x:
            if x % i == 0:#소수판별
                answer -= 1#소수아니면 정답카운트에서 하나뺌, 아래서 늘려주기때문
                break
            i += 1
        answer += 1

    return answer

solution("17")