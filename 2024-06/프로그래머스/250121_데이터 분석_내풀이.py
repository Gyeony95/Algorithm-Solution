def solution(data, ext, val_ext, sort_by):
    remove_arr = []
    f_index = 0
    s_index = 0
    if ext == 'code':
        f_index = 0
    if ext == 'date':
        f_index = 1
    if ext == 'maximum':
        f_index = 2
    if ext == 'remain':
        f_index = 3
    if sort_by == 'code':
        s_index = 0
    if sort_by == 'date':
        s_index = 1
    if sort_by == 'maximum':
        s_index = 2
    if sort_by == 'remain':
        s_index = 3

    for i, node in enumerate(data):
        if val_ext < node[f_index]:
            remove_arr.append(i)
    remove_arr.reverse()
    for i in remove_arr:
        data.pop(i)

    sorted_data = sorted(data, key=lambda x: x[s_index])

    return sorted_data


data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
print(solution(data, 'date', 20300501, 'remain'))
