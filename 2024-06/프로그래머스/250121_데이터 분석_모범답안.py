def solution(data, ext, val_ext, sort_by):
    by = ["code", "date", "maximum", "remain"]

    remove_arr = []
    f_index = by.index(ext)
    s_index = by.index(sort_by)

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
