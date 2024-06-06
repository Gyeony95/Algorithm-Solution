alpabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z', ]


def solution(name):
    current_index = 1
    cursor_index = 0
    answer = 0
    idx_list = []
    period_list = []
    for i in name:
        idx = alpabet.index(i)
        idx_list.append(idx)
    for i in idx_list:
        period_list.append(sorted(idx_list).index(i))

    for i in range(len(period_list)):
        new_cursor = period_list[i]
        # 커서이동
        answer += abs(new_cursor - cursor_index)
        cursor_index = new_cursor
        new_index = idx_list[new_cursor]
        answer += abs(current_index - new_index)
        current_index = new_index


    return answer


print(solution("JEROEN"))
