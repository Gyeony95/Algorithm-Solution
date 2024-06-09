
# 정확성 테스트는 통과했으나 효율성 테스트에서 시간초과 나옴 -> 시간복잡도 개선 해야함
def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i)
    return participant[0]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))