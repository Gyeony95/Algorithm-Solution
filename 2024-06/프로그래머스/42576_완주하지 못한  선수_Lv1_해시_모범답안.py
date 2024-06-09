from collections import Counter

def solution(participant, completion):
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)

    # 남은 카운터를 구함
    remaining = participant_counter - completion_counter

    # 남은 선수의 이름을 반환 (단 한 명이므로 keys()의 첫 번째 요소)
    return list(remaining.keys())[0]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))