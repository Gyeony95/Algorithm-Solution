def solution(name):
    n = len(name)
    answer = 0

    # 알파벳 변환 계산
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    # 커서 이동 최적화
    move = n - 1
    for i in range(n):
        next_index = i + 1
        while next_index < n and name[next_index] == 'A':
            next_index += 1
        move = min(move, i + n - next_index + min(i, n - next_index))

    answer += move
    return answer


print(solution("JEROEN"))
